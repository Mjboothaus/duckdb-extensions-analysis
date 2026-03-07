import argparse
import hashlib
import json
import os
import subprocess
import time
from dataclasses import dataclass
from urllib.parse import quote

import requests

# Notes
# - This script is intentionally stand-alone (no project imports).
# - Uses GitHub Search APIs:
#   - Repo search: /search/repositories
#   - Code search: /search/code
# - Code search is much more likely to find repos that *contain* extension artefacts,
#   even if they are not tagged with the duckdb-extension topic.

DEFAULT_TEST_MODE = False
DEFAULT_EARLY_STOP_COUNT_TEST = 200
DEFAULT_EARLY_STOP_COUNT = 3000
DEFAULT_MAX_PAGES_TEST = 1
DEFAULT_MAX_PAGES = 10
DEFAULT_PER_PAGE_TEST = 20
DEFAULT_PER_PAGE = 100  # GitHub Search API max
DEFAULT_SLEEP_SECONDS = 1.0
DEFAULT_OUTPUT_PATH = "duckdb_extension_candidates.json"
DEFAULT_ENRICH_MISSING = True
DEFAULT_ENRICH_LIMIT = 200
DEFAULT_DISCOVERY_MODE = "precision"  # precision|broad

DEFAULT_CACHE_ENABLED = True
DEFAULT_CACHE_DIR = ".cache/github_extension_discovery"
DEFAULT_CACHE_TTL_SECONDS = 24 * 60 * 60
DEFAULT_REQUEST_TIMEOUT_SECONDS = 30
DEFAULT_VERBOSE = False

GITHUB_API_VERSION = "2022-11-28"
DEFAULT_ACCEPT_HEADER = "application/vnd.github+json"


def get_github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token.strip()

    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            check=True,
        )
        token = result.stdout.strip()
        if not token:
            raise ValueError("No token returned from `gh auth token`.")
        return token
    except Exception as exc:
        raise RuntimeError(
            "Unable to obtain a GitHub token. Set GITHUB_TOKEN or authenticate with `gh auth login`."
        ) from exc


def build_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"token {token}",
        "Accept": DEFAULT_ACCEPT_HEADER,
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }


@dataclass
class CachedResponse:
    json_data: dict
    status_code: int = 200
    headers: dict[str, str] | None = None

    def json(self) -> dict:
        return self.json_data


class JsonFileCache:
    def __init__(self, cache_dir: str, *, ttl_seconds: int):
        self.cache_dir = cache_dir
        self.ttl_seconds = ttl_seconds

    def _path_for_key(self, key: str) -> str:
        return os.path.join(self.cache_dir, f"{key}.json")

    def _key_for_url(self, url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

    def get(self, url: str) -> dict | None:
        key = self._key_for_url(url)
        path = self._path_for_key(key)
        if not os.path.exists(path):
            return None

        try:
            with open(path) as f:
                payload = json.load(f)
        except Exception:
            return None

        saved_at = payload.get("saved_at")
        if not isinstance(saved_at, (int, float)):
            return None

        if (time.time() - float(saved_at)) > self.ttl_seconds:
            return None

        return payload.get("data")

    def set(self, url: str, data: dict) -> None:
        os.makedirs(self.cache_dir, exist_ok=True)
        key = self._key_for_url(url)
        path = self._path_for_key(key)
        payload = {"saved_at": time.time(), "data": data}
        with open(path, "w") as f:
            json.dump(payload, f)


def _sleep_until_rate_limit_reset(resp: requests.Response) -> None:
    reset = resp.headers.get("X-RateLimit-Reset")
    if not reset:
        return

    try:
        reset_epoch = int(reset)
    except ValueError:
        return

    now = int(time.time())
    # Add a small buffer to avoid immediately re-triggering.
    sleep_for = max(0, reset_epoch - now) + 2
    print(f"    Rate limit hit. Sleeping {sleep_for}s until reset...")
    time.sleep(sleep_for)


def request_with_retries(
    url: str,
    headers: dict[str, str],
    *,
    cache: JsonFileCache | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
    max_attempts: int = 5,
    base_sleep_seconds: float = 1.0,
    verbose: bool = False,
) -> requests.Response:
    """GET with basic backoff and rate-limit handling.

    If cache is provided, successful JSON responses are cached by URL.
    """

    if cache is not None:
        cached = cache.get(url)
        if isinstance(cached, dict):
            if verbose:
                print(f"    Cache hit: {url}")
            return CachedResponse(cached, headers={})

    for attempt in range(1, max_attempts + 1):
        if verbose:
            print(f"    GET {url} (attempt {attempt}/{max_attempts})")
        resp = requests.get(url, headers=headers, timeout=timeout_seconds)

        if resp.status_code == 200:
            if cache is not None:
                try:
                    cache.set(url, resp.json())
                except Exception:
                    pass
            return resp

        # Rate limit (primary) usually comes back as 403 with specific headers.
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            print("ERROR 403 (rate limit)")
            _sleep_until_rate_limit_reset(resp)
            continue

        # Secondary rate limit / abuse detection often returns 403 as well.
        # Back off and retry a few times.
        if resp.status_code in {403, 429, 500, 502, 503, 504}:
            try:
                msg = resp.json().get("message")
            except Exception:
                msg = resp.text.strip()[:200]
            sleep_for = base_sleep_seconds * (2 ** (attempt - 1))
            print(f"ERROR {resp.status_code} ({msg}); retrying in {sleep_for:.1f}s")
            time.sleep(sleep_for)
            continue

        # Non-retryable
        try:
            msg = resp.json().get("message")
        except Exception:
            msg = resp.text.strip()[:200]
        raise RuntimeError(f"GitHub API error {resp.status_code}: {msg}")

    raise RuntimeError(f"GitHub API failed after {max_attempts} attempts")


def search_repositories(
    query: str,
    headers: dict[str, str],
    *,
    per_page: int,
    max_pages: int,
    sleep_seconds: float,
    cache: JsonFileCache | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> list[dict]:
    results: list[dict] = []

    print(f"\nSearching repos: '{query}'")
    for page in range(1, max_pages + 1):
        url = (
            "https://api.github.com/search/repositories"
            f"?q={quote(query)}&sort=updated&order=desc&per_page={per_page}&page={page}"
        )
        print(f"  Page {page} ... ", end="")

        resp = request_with_retries(
            url,
            headers,
            cache=cache,
            timeout_seconds=timeout_seconds,
            verbose=False,
        )
        data = resp.json()
        items = data.get("items", [])
        print(f"got {len(items)} items")

        results.extend(items)
        if len(items) < per_page:
            break

        time.sleep(sleep_seconds)

    return results


def search_code(
    query: str,
    headers: dict[str, str],
    *,
    per_page: int,
    max_pages: int,
    sleep_seconds: float,
    cache: JsonFileCache | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> list[dict]:
    results: list[dict] = []

    print(f"\nSearching code: '{query}'")
    for page in range(1, max_pages + 1):
        url = (
            "https://api.github.com/search/code"
            f"?q={quote(query)}&sort=indexed&order=desc&per_page={per_page}&page={page}"
        )
        print(f"  Page {page} ... ", end="")

        resp = request_with_retries(
            url,
            headers,
            cache=cache,
            timeout_seconds=timeout_seconds,
            verbose=False,
        )
        data = resp.json()
        items = data.get("items", [])
        print(f"got {len(items)} items")

        results.extend(items)
        if len(items) < per_page:
            break

        time.sleep(sleep_seconds)

    return results


def get_repo_details(
    full_name: str,
    headers: dict[str, str],
    *,
    cache: JsonFileCache | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
    verbose: bool = False,
) -> dict:
    url = f"https://api.github.com/repos/{full_name}"
    resp = request_with_retries(
        url,
        headers,
        cache=cache,
        timeout_seconds=timeout_seconds,
        verbose=verbose,
    )
    return resp.json()


def enrich_repos_in_place(
    repos_by_full_name: dict[str, dict],
    headers: dict[str, str],
    *,
    sleep_seconds: float,
    limit: int,
    cache: JsonFileCache | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
    verbose: bool = False,
) -> None:
    """Fill missing fields on repo dicts using /repos/{owner}/{repo}.

    GitHub code search returns an embedded `repository` object, but it does not
    always include fields like `stargazers_count`.
    """

    needs_enrichment = [
        (full_name, repo)
        for full_name, repo in repos_by_full_name.items()
        if repo.get("stargazers_count") is None or repo.get("html_url") is None
    ]

    if not needs_enrichment:
        return

    if limit < len(needs_enrichment):
        needs_enrichment = needs_enrichment[:limit]

    total = len(needs_enrichment)
    enriched = 0
    start_ts = time.time()

    print(
        f"Enrichment: {total} repos to enrich (limit={limit}, cache={cache is not None})"
    )

    for idx, (full_name, repo) in enumerate(needs_enrichment, start=1):
        if verbose or idx == 1 or idx % 25 == 0:
            elapsed = time.time() - start_ts
            rate = (idx / elapsed) if elapsed > 0 else 0.0
            eta = ((total - idx) / rate) if rate > 0 else None
            eta_str = f"~{int(eta)}s" if eta is not None else "?"
            print(
                f"  Enriching {idx}/{total}: {full_name} (elapsed {elapsed:.1f}s, eta {eta_str})"
            )

        try:
            details = get_repo_details(
                full_name,
                headers,
                cache=cache,
                timeout_seconds=timeout_seconds,
                verbose=verbose,
            )
        except Exception as exc:
            print(f"    WARN: failed to enrich {full_name}: {exc}")
            continue

        # Shallow merge: preserve anything we already have, fill missing.
        for k, v in details.items():
            repo.setdefault(k, v)

        enriched += 1
        time.sleep(sleep_seconds)

    if enriched:
        print(f"Enriched {enriched}/{total} repos with missing fields")


def dedupe_repos_by_full_name(
    repos: list[dict],
    *,
    seen_full_names: set[str] | None = None,
    early_stop_count: int | None = None,
) -> list[dict]:
    if seen_full_names is None:
        seen_full_names = set()

    out: list[dict] = []
    for r in repos:
        full_name = r.get("full_name")
        if not full_name:
            continue
        if full_name in seen_full_names:
            continue
        seen_full_names.add(full_name)
        out.append(r)

        if early_stop_count is not None and len(seen_full_names) >= early_stop_count:
            return out

    return out


def print_repo_table(
    repos: list[dict], title: str, *, max_rows: int | None = None
) -> None:
    if not repos:
        print(f"\n{title}: nothing found")
        return

    rows = sorted(repos, key=lambda x: x.get("pushed_at", ""), reverse=True)
    if max_rows is not None:
        rows = rows[:max_rows]

    print(f"\n{title} ({len(repos)} total)")
    print("-" * 90)
    print(f"{'Repo':<35} {'Stars':<6} {'Lang':<10} {'Pushed':<12} Description")
    print("-" * 90)

    for r in rows:
        full_name = r.get("full_name") or "—"
        stars = r.get("stargazers_count")
        stars = stars if isinstance(stars, int) else 0
        lang = r.get("language") or "N/A"
        pushed = (r.get("pushed_at") or "—")[:10]
        desc = (r.get("description") or "—")[:60]

        print(f"{full_name:<35} {stars:<6} {lang:<10} {pushed:<12} {desc}")


def to_output_rows(repos: list[dict]) -> list[dict]:
    out: list[dict] = []
    for r in repos:
        out.append(
            {
                "repo": r.get("full_name") or "",
                "url": r.get("html_url") or "",
                "stars": r.get("stargazers_count")
                if isinstance(r.get("stargazers_count"), int)
                else 0,
                "lang": r.get("language"),
                "pushed": r.get("pushed_at"),
                "desc": r.get("description") or "",
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Discover additional DuckDB extension repositories via GitHub search"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        default=DEFAULT_TEST_MODE,
        help="Use conservative limits for smoke testing",
    )
    parser.add_argument(
        "--early-stop",
        type=int,
        default=None,
        help="Stop after this many unique repos are found (across all searches)",
    )
    parser.add_argument(
        "--max-pages", type=int, default=None, help="Max pages to fetch per search"
    )
    parser.add_argument(
        "--per-page", type=int, default=None, help="Results per page (max 100)"
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=DEFAULT_SLEEP_SECONDS,
        help="Delay between API calls",
    )
    parser.add_argument(
        "--output", default=DEFAULT_OUTPUT_PATH, help="Path to write JSON output"
    )
    parser.add_argument(
        "--mode",
        choices=["precision", "broad"],
        default=DEFAULT_DISCOVERY_MODE,
        help="Discovery mode: precision uses higher-signal queries; broad uses wider but noisier queries",
    )
    parser.add_argument(
        "--enrich-missing",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_ENRICH_MISSING,
        help="Fetch /repos/{owner}/{repo} details when search results are missing fields",
    )
    parser.add_argument(
        "--enrich-limit",
        type=int,
        default=DEFAULT_ENRICH_LIMIT,
        help="Max repos to enrich (controls extra API calls)",
    )
    parser.add_argument(
        "--cache",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_CACHE_ENABLED,
        help="Cache GitHub API responses by URL to speed up re-runs and reduce rate limit pressure",
    )
    parser.add_argument(
        "--cache-dir",
        default=DEFAULT_CACHE_DIR,
        help="Directory for cached GitHub API responses",
    )
    parser.add_argument(
        "--cache-ttl-seconds",
        type=int,
        default=DEFAULT_CACHE_TTL_SECONDS,
        help="Cache TTL in seconds",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=DEFAULT_REQUEST_TIMEOUT_SECONDS,
        help="HTTP request timeout in seconds",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=DEFAULT_VERBOSE,
        help="Verbose logging (prints request URLs, cache hits, and enrichment progress)",
    )

    args = parser.parse_args()

    is_test = bool(args.test)
    per_page = args.per_page or (DEFAULT_PER_PAGE_TEST if is_test else DEFAULT_PER_PAGE)
    max_pages = args.max_pages or (
        DEFAULT_MAX_PAGES_TEST if is_test else DEFAULT_MAX_PAGES
    )
    early_stop = args.early_stop
    if early_stop is None:
        early_stop = (
            DEFAULT_EARLY_STOP_COUNT_TEST if is_test else DEFAULT_EARLY_STOP_COUNT
        )

    token = get_github_token()
    headers = build_headers(token)
    print("Authenticated OK")

    cache = None
    if args.cache:
        cache = JsonFileCache(args.cache_dir, ttl_seconds=args.cache_ttl_seconds)

    print("Starting extension discovery...")
    print(
        "Config: "
        f"test={is_test}, per_page={per_page}, max_pages={max_pages}, early_stop={early_stop}, "
        f"cache={bool(cache)}, enrich_missing={args.enrich_missing}"
    )

    seen_full_names: set[str] = set()
    repos_by_full_name: dict[str, dict] = {}

    def _add_repos(repos: list[dict]) -> None:
        nonlocal repos_by_full_name
        for r in repos:
            full_name = r.get("full_name")
            if not full_name:
                continue
            if full_name in repos_by_full_name:
                continue
            repos_by_full_name[full_name] = r

    # 1) Topic-based search (fast, good precision)
    topic_items = search_repositories(
        "topic:duckdb-extension",
        headers,
        per_page=per_page,
        max_pages=max_pages,
        sleep_seconds=args.sleep,
        cache=cache,
        timeout_seconds=args.timeout_seconds,
    )
    topic_repos = dedupe_repos_by_full_name(
        topic_items, seen_full_names=seen_full_names, early_stop_count=early_stop
    )
    _add_repos(topic_repos)

    if len(seen_full_names) < early_stop:
        # 2) Code-based search (better recall)
        # These are heuristic signals; add more queries as needed.
        if args.mode == "precision":
            # Higher-signal queries: fewer results, better precision.
            code_queries = [
                "filename:extension_config.cmake",
                '"build_duckdb_extension" filename:CMakeLists.txt',
                '"duckdb_extension_init" filename:CMakeLists.txt',
                '"duckdb_loadable_extension" filename:CMakeLists.txt',
                '".duckdb_extension" filename:.duckdb_extension',
                '".duckdb_extension" path:extension',
            ]
        else:
            # Broader queries: better recall, more noise.
            code_queries = [
                '".duckdb_extension" path:extension',
                '"duckdb_extension" path:extension',
                '"duckdb_extension" filename:duckdb_extension.json',
                '"duckdb_extension" filename:extension_config.cmake',
                '"DUCKDB_EXTENSION" path:src',
            ]

        for q in code_queries:
            if len(seen_full_names) >= early_stop:
                break

            code_items = search_code(
                q,
                headers,
                per_page=per_page,
                max_pages=max_pages,
                sleep_seconds=args.sleep,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
            )
            code_repos = [item.get("repository") for item in code_items]
            code_repos = [r for r in code_repos if isinstance(r, dict)]

            new_repos = dedupe_repos_by_full_name(
                code_repos,
                seen_full_names=seen_full_names,
                early_stop_count=early_stop,
            )
            _add_repos(new_repos)

    if args.enrich_missing:
        enrich_repos_in_place(
            repos_by_full_name,
            headers,
            sleep_seconds=args.sleep,
            limit=args.enrich_limit,
            cache=cache,
            timeout_seconds=args.timeout_seconds,
            verbose=args.verbose,
        )

    found_repos = list(repos_by_full_name.values())

    # Final filter
    found_repos = [
        r for r in found_repos if r.get("full_name") != "duckdb/community-extensions"
    ]

    print_repo_table(found_repos, "DuckDB extension candidates")

    with open(args.output, "w") as f:
        json.dump(to_output_rows(found_repos), f, indent=2)

    print(f"\nSaved to {args.output}")
    if is_test:
        print(
            "Tip: re-run without --test (or set higher --max-pages/--early-stop) to discover more."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
