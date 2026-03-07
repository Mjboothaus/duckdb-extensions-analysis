import argparse
import base64
import gzip
import hashlib
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import duckdb
import requests


GITHUB_API_VERSION = "2022-11-28"
DEFAULT_ACCEPT_HEADER = "application/vnd.github+json"

DEFAULT_CACHE_DIR = ".cache/extension_candidate_validation"
DEFAULT_CACHE_TTL_SECONDS = 7 * 24 * 60 * 60
DEFAULT_TIMEOUT_SECONDS = 30
DEFAULT_TREE_CMAKE_MAX = 3
DEFAULT_CHECKPOINT_EVERY = 10

DEFAULT_RELEASE_SCAN = True
DEFAULT_RELEASE_MAX = 10
DEFAULT_RELEASE_DOWNLOAD = False
DEFAULT_RELEASE_DOWNLOAD_DIR = ".cache/extension_candidate_validation/assets"
DEFAULT_RELEASE_MAX_MB = 80

GITHUB_REPO_RE = re.compile(r"^(?P<owner>[^/]+)/(?P<repo>[^/]+)$")
GITHUB_REPO_IN_URL_RE = re.compile(r"github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)")


def get_github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token.strip()

    result = subprocess.run(
        ["gh", "auth", "token"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError("Unable to obtain GitHub token. Set GITHUB_TOKEN or run `gh auth login`.")

    token = result.stdout.strip()
    if not token:
        raise RuntimeError("No token returned from `gh auth token`.")

    return token


def build_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"token {token}",
        "Accept": DEFAULT_ACCEPT_HEADER,
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }


class JsonFileCache:
    def __init__(self, cache_dir: str, *, ttl_seconds: int):
        self.cache_dir = cache_dir
        self.ttl_seconds = ttl_seconds

    def _key_for_url(self, url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

    def _path_for_key(self, key: str) -> Path:
        return Path(self.cache_dir) / f"{key}.json"

    def get(self, url: str) -> dict | None:
        path = self._path_for_key(self._key_for_url(url))
        if not path.exists():
            return None

        try:
            payload = json.loads(path.read_text())
        except Exception:
            return None

        saved_at = payload.get("saved_at")
        if not isinstance(saved_at, (int, float)):
            return None

        if (time.time() - float(saved_at)) > self.ttl_seconds:
            return None

        data = payload.get("data")
        return data if isinstance(data, dict) else None

    def set(self, url: str, data: dict) -> None:
        Path(self.cache_dir).mkdir(parents=True, exist_ok=True)
        path = self._path_for_key(self._key_for_url(url))
        payload = {"saved_at": time.time(), "data": data}
        path.write_text(json.dumps(payload))


@dataclass
class CachedResponse:
    json_data: dict

    def json(self) -> dict:
        return self.json_data


def _sleep_until_rate_limit_reset(resp: requests.Response) -> None:
    reset = resp.headers.get("X-RateLimit-Reset")
    if not reset:
        return

    try:
        reset_epoch = int(reset)
    except ValueError:
        return

    now = int(time.time())
    sleep_for = max(0, reset_epoch - now) + 2
    print(f"    Rate limit hit. Sleeping {sleep_for}s until reset...")
    time.sleep(sleep_for)


def request_json(
    url: str,
    headers: dict[str, str],
    *,
    cache: JsonFileCache | None,
    timeout_seconds: int,
    max_attempts: int = 5,
    verbose: bool = False,
) -> requests.Response:
    if cache is not None:
        cached = cache.get(url)
        if cached is not None:
            if verbose:
                print(f"    Cache hit: {url}")
            return CachedResponse(cached)  # type: ignore[return-value]

    for attempt in range(1, max_attempts + 1):
        if verbose:
            print(f"    GET {url} (attempt {attempt}/{max_attempts})")

        try:
            resp = requests.get(url, headers=headers, timeout=timeout_seconds)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as exc:
            sleep_for = 1.0 * (2 ** (attempt - 1))
            if verbose:
                print(f"    WARN: request error ({exc}); retrying in {sleep_for:.1f}s")
            time.sleep(sleep_for)
            continue

        if resp.status_code == 200:
            if cache is not None:
                try:
                    cache.set(url, resp.json())
                except Exception:
                    pass
            return resp

        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            _sleep_until_rate_limit_reset(resp)
            continue

        if resp.status_code in {403, 429, 500, 502, 503, 504}:
            try:
                msg = resp.json().get("message")
            except Exception:
                msg = resp.text.strip()[:200]
            sleep_for = 1.0 * (2 ** (attempt - 1))
            print(f"    WARN: {resp.status_code} ({msg}); retrying in {sleep_for:.1f}s")
            time.sleep(sleep_for)
            continue

        try:
            msg = resp.json().get("message")
        except Exception:
            msg = resp.text.strip()[:200]
        raise RuntimeError(f"GitHub API error {resp.status_code}: {msg}")

    raise RuntimeError(f"GitHub API failed after {max_attempts} attempts")


def normalise_repo(repo: str | None) -> str | None:
    if not repo:
        return None
    repo = repo.strip()
    if not repo:
        return None

    if repo.startswith("http://") or repo.startswith("https://"):
        m = GITHUB_REPO_IN_URL_RE.search(repo)
        if not m:
            return None
        return f"{m.group('owner')}/{m.group('repo')}"

    if not GITHUB_REPO_RE.match(repo):
        return None

    return repo


def guess_extension_names_from_repo(repo: str) -> list[str]:
    _, repo_name = repo.split("/", 1)

    candidates: list[str] = []

    def add(name: str) -> None:
        name = name.strip().lower()
        if not name:
            return
        if name not in candidates:
            candidates.append(name)

    add(repo_name)

    if repo_name.startswith("duckdb-"):
        add(repo_name.removeprefix("duckdb-"))
    if repo_name.endswith("-duckdb"):
        add(repo_name.removesuffix("-duckdb"))
    if repo_name.endswith("_duckdb"):
        add(repo_name.removesuffix("_duckdb"))
    if repo_name.startswith("duckdb_"):
        add(repo_name.removeprefix("duckdb_"))

    if repo_name.endswith("-extension"):
        add(repo_name.removesuffix("-extension"))
    if repo_name.startswith("duckdb-extension-"):
        add(repo_name.removeprefix("duckdb-extension-"))

    for c in list(candidates):
        add(c.replace("-", "_"))

    return candidates[:6]


def repo_api(owner_repo: str) -> str:
    return f"https://api.github.com/repos/{owner_repo}"


def readme_api(owner_repo: str) -> str:
    return f"https://api.github.com/repos/{owner_repo}/readme"


def releases_api(owner_repo: str, *, per_page: int = 10, page: int = 1) -> str:
    return (
        f"https://api.github.com/repos/{owner_repo}/releases"
        f"?per_page={int(per_page)}&page={int(page)}"
    )


def contents_api(owner_repo: str, path: str) -> str:
    return f"https://api.github.com/repos/{owner_repo}/contents/{quote(path)}"


def git_ref_api(owner_repo: str, branch: str) -> str:
    return f"https://api.github.com/repos/{owner_repo}/git/ref/heads/{quote(branch)}"


def git_commit_api(owner_repo: str, sha: str) -> str:
    return f"https://api.github.com/repos/{owner_repo}/git/commits/{quote(sha)}"


def git_tree_api(owner_repo: str, tree_sha: str) -> str:
    return f"https://api.github.com/repos/{owner_repo}/git/trees/{quote(tree_sha)}?recursive=1"


def try_get_contents(
    owner_repo: str,
    path: str,
    headers: dict[str, str],
    *,
    cache: JsonFileCache | None,
    timeout_seconds: int,
    verbose: bool,
) -> dict | None:
    url = contents_api(owner_repo, path)
    try:
        resp = request_json(url, headers, cache=cache, timeout_seconds=timeout_seconds, verbose=verbose)
        return resp.json()
    except RuntimeError as exc:
        # Missing file comes back as 404, but our request_json will raise for non-retryable.
        # Convert obvious 404s into None.
        if "404" in str(exc):
            return None
        return None


def get_repo_tree_recursive(
    owner_repo: str,
    headers: dict[str, str],
    *,
    cache: JsonFileCache | None,
    timeout_seconds: int,
    default_branch: str,
    verbose: bool,
) -> dict | None:
    """Return the recursive git tree JSON for the repo's default branch.

    We try a fast path first (using the branch name as the tree identifier), then
    fall back to resolving branch -> commit -> tree.
    """

    # Fast path: many GitHub APIs accept a branch name here.
    try:
        url = git_tree_api(owner_repo, default_branch)
        return request_json(url, headers, cache=cache, timeout_seconds=timeout_seconds, verbose=verbose).json()
    except Exception:
        pass

    # Fallback: resolve to an actual tree SHA.
    try:
        ref = request_json(
            git_ref_api(owner_repo, default_branch),
            headers,
            cache=cache,
            timeout_seconds=timeout_seconds,
            verbose=verbose,
        ).json()
        sha = (ref.get("object") or {}).get("sha")
        if not isinstance(sha, str) or not sha:
            return None

        commit = request_json(
            git_commit_api(owner_repo, sha),
            headers,
            cache=cache,
            timeout_seconds=timeout_seconds,
            verbose=verbose,
        ).json()
        tree_sha = ((commit.get("tree") or {}).get("sha"))
        if not isinstance(tree_sha, str) or not tree_sha:
            return None

        return request_json(
            git_tree_api(owner_repo, tree_sha),
            headers,
            cache=cache,
            timeout_seconds=timeout_seconds,
            verbose=verbose,
        ).json()
    except Exception:
        return None


def decode_content(contents_json: dict) -> str | None:
    if contents_json.get("encoding") != "base64":
        return None
    content = contents_json.get("content")
    if not isinstance(content, str):
        return None

    try:
        return base64.b64decode(content).decode("utf-8", errors="replace")
    except Exception:
        return None


def looks_like_duckdb_extension_cmake(text: str) -> bool:
    t = text.lower()
    needles = [
        "duckdb_extension",
        "duckdb extension",
        "build_duckdb_extension",
        "duckdb_extension_init",
        "duckdb_loadable_extension",
    ]
    return any(n in t for n in needles)


def source_entrypoint_signals(text: str) -> dict[str, bool]:
    """Signals from scanning repository source files.

    This is a lightweight heuristic intended to improve validation precision.
    """

    t = text.lower()
    needles = [
        "duckdb_extension_init",
        "duckdb_init",
        "duckdb_loadable_extension",
        "build_duckdb_extension",
    ]
    return {
        "source_mentions_duckdb_extension_api": any(n in t for n in needles),
        "source_mentions_duckdb": "duckdb" in t,
    }


def readme_signals(text: str) -> dict[str, bool]:
    t = text.lower()
    return {
        "readme_mentions_duckdb": "duckdb" in t,
        "readme_mentions_extension": "extension" in t,
        "readme_mentions_install": "install" in t and "install" in t,
        "readme_mentions_load": "load" in t,
        "readme_mentions_duckdb_extension_file": ".duckdb_extension" in t,
        "readme_mentions_install_command": "install " in t,
        "readme_mentions_load_command": "load " in t,
        "readme_mentions_from_syntax": " from " in t and "install" in t,
        "readme_mentions_custom_repo": "custom_extension_repository" in t,
        # Template/noise hints.
        "readme_mentions_template": "template" in t,
        "readme_mentions_extension_template": "extension template" in t,
    }


def is_likely_template_clone(*, repo: str, topics: list[str], signals: dict[str, bool], paths: list[str]) -> bool:
    """Heuristic to flag likely template/scaffold repos.

    This is intentionally conservative: it only *flags* candidates to reduce reviewer time.
    We do not exclude automatically (promotion/labelling can decide what to do).
    """

    repo_l = repo.lower()
    topics_l = [t.lower() for t in topics if isinstance(t, str)]
    paths_l = [p.lower() for p in paths if isinstance(p, str)]

    name_hint = any(k in repo_l for k in ["template", "scaffold", "example"]) and "duckdb" in repo_l
    topic_hint = any(t in {"template", "duckdb-template", "duckdb-extension-template"} for t in topics_l)

    readme_hint = bool(
        signals.get("readme_mentions_template")
        and signals.get("readme_mentions_duckdb")
        and (signals.get("readme_mentions_extension_template") or "duckdb" in repo_l)
    )

    path_hint = any(
        k in p
        for p in paths_l
        for k in [
            "extension-template",
            "extension_template",
            "duckdb-extension-template",
            "duckdb_extension_template",
        ]
    )

    return bool(name_hint or topic_hint or readme_hint or path_hint)


@dataclass
class ValidationRow:
    repo: str
    stars: int
    pushed: str | None
    archived: bool | None
    topics: list[str]
    signals: dict[str, bool]
    score: int
    install_name: str | None
    install_ok: bool
    load_ok: bool
    install_error: str | None


def compute_score_with_breakdown(
    topics: list[str],
    signals: dict[str, bool],
) -> tuple[int, dict[str, int]]:
    score = 0
    breakdown: dict[str, int] = {}

    def add(key: str, points: int, *, enabled: bool) -> None:
        nonlocal score
        if not enabled:
            return
        score += points
        breakdown[key] = breakdown.get(key, 0) + points

    add("topic:duckdb-extension", 4, enabled=("duckdb-extension" in topics))
    add("topic:duckdb", 1, enabled=("duckdb" in topics))

    # Root-path signals
    add("root:extension_config.cmake", 6, enabled=bool(signals.get("has_extension_config_cmake")))
    add("root:extension_dir", 2, enabled=bool(signals.get("has_extension_dir")))
    add("root:.duckdb_extension", 6, enabled=bool(signals.get("has_dot_duckdb_extension")))
    add(
        "root:CMakeLists mentions extension",
        3,
        enabled=bool(signals.get("cmake_mentions_duckdb_extension")),
    )

    # Tree-scan signals (help find files nested in subdirs)
    add(
        "tree:extension_config.cmake",
        5,
        enabled=bool(signals.get("tree_has_extension_config_cmake"))
        and not bool(signals.get("has_extension_config_cmake")),
    )
    add(
        "tree:.duckdb_extension",
        5,
        enabled=bool(signals.get("tree_has_dot_duckdb_extension"))
        and not bool(signals.get("has_dot_duckdb_extension")),
    )

    # Strong positive: nested CMakeLists appears to contain DuckDB extension markers.
    add(
        "tree:CMakeLists mentions extension",
        3,
        enabled=bool(signals.get("tree_cmake_mentions_duckdb_extension")),
    )

    # Source scanning signals
    add(
        "tree:source mentions extension API",
        4,
        enabled=bool(signals.get("tree_source_mentions_duckdb_extension_api")),
    )

    # README signals (lighter weight; helps ranking rather than strict validation)
    add("readme:duckdb", 1, enabled=bool(signals.get("readme_mentions_duckdb")))
    add("readme:extension", 1, enabled=bool(signals.get("readme_mentions_extension")))
    add("readme:install command", 1, enabled=bool(signals.get("readme_mentions_install_command")))
    add(
        "readme:.duckdb_extension",
        1,
        enabled=bool(signals.get("readme_mentions_duckdb_extension_file")),
    )

    return score, breakdown


def duckdb_install_load_smoke_test(
    con: duckdb.DuckDBPyConnection,
    *,
    candidates: list[str],
    verbose: bool,
) -> tuple[bool, bool, str | None, str | None]:
    last_error: str | None = None

    for name in candidates:
        try:
            if verbose:
                print(f"    DuckDB: INSTALL/LOAD {name}")
            con.execute(f"INSTALL {name}")
            con.execute(f"LOAD {name}")
            return True, True, name, None
        except Exception as exc:
            last_error = str(exc)
            continue

    return False, False, None, last_error


def find_release_extension_assets(releases: list[dict]) -> list[dict]:
    assets: list[dict] = []
    for rel in releases:
        if not isinstance(rel, dict):
            continue
        for a in rel.get("assets") or []:
            if not isinstance(a, dict):
                continue
            name = a.get("name")
            if not isinstance(name, str):
                continue
            lower = name.lower()
            if lower.endswith(".duckdb_extension") or lower.endswith(".duckdb_extension.gz"):
                assets.append(a)
    return assets


def download_asset(
    asset: dict,
    headers: dict[str, str],
    *,
    download_dir: Path,
    timeout_seconds: int,
    max_mb: int,
    verbose: bool,
) -> Path | None:
    url = asset.get("browser_download_url")
    name = asset.get("name")
    size = asset.get("size")

    if not isinstance(url, str) or not isinstance(name, str):
        return None

    if isinstance(size, int) and size > max_mb * 1024 * 1024:
        return None

    download_dir.mkdir(parents=True, exist_ok=True)
    out_path = download_dir / name
    if out_path.exists() and out_path.stat().st_size > 0:
        return out_path

    if verbose:
        print(f"    Downloading asset: {url}")

    resp = requests.get(url, headers=headers, timeout=timeout_seconds)
    if resp.status_code != 200:
        return None

    out_path.write_bytes(resp.content)
    return out_path


def maybe_decompress_gz(path: Path) -> Path:
    if not path.name.lower().endswith(".gz"):
        return path

    out_path = path.with_suffix("")
    if out_path.exists() and out_path.stat().st_size > 0:
        return out_path

    with gzip.open(path, "rb") as f:
        out_path.write_bytes(f.read())

    return out_path


def duckdb_load_from_file(
    con: duckdb.DuckDBPyConnection,
    *,
    path: Path,
    verbose: bool,
) -> tuple[bool, str | None]:
    try:
        if verbose:
            print(f"    DuckDB: LOAD '{path.as_posix()}'")
        con.execute(f"LOAD '{path.as_posix()}'")
        return True, None
    except Exception as exc:
        return False, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate extension candidates using GitHub API signals and optional DuckDB INSTALL/LOAD"
    )
    parser.add_argument("input", help="JSON list with at least a 'repo' field")
    parser.add_argument(
        "--output",
        default="data/discovery/validated_extension_candidates.json",
        help="Where to write JSON output",
    )
    parser.add_argument("--max", type=int, default=200, help="Max repos to validate")
    parser.add_argument(
        "--resume",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="If output exists, resume by skipping repos already present in the output",
    )
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=DEFAULT_CHECKPOINT_EVERY,
        help="Write output JSON every N validated repos (helps with long runs)",
    )

    parser.add_argument("--cache-dir", default=DEFAULT_CACHE_DIR)
    parser.add_argument("--cache-ttl-seconds", type=int, default=DEFAULT_CACHE_TTL_SECONDS)
    parser.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument(
        "--tree-cmake-max",
        type=int,
        default=DEFAULT_TREE_CMAKE_MAX,
        help="Max nested CMakeLists.txt files to fetch and scan per repo when using git tree scan",
    )

    parser.add_argument(
        "--duckdb-smoke-test",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Attempt DuckDB INSTALL/LOAD using guessed extension names",
    )
    parser.add_argument(
        "--release-scan",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_RELEASE_SCAN,
        help="Scan GitHub releases for .duckdb_extension assets",
    )
    parser.add_argument(
        "--release-max",
        type=int,
        default=DEFAULT_RELEASE_MAX,
        help="Max releases to scan per repo",
    )
    parser.add_argument(
        "--release-download",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_RELEASE_DOWNLOAD,
        help="Download a matching release asset (if present) and attempt DuckDB LOAD from file",
    )
    parser.add_argument(
        "--release-download-dir",
        default=DEFAULT_RELEASE_DOWNLOAD_DIR,
        help="Directory to store downloaded release assets",
    )
    parser.add_argument(
        "--release-max-mb",
        type=int,
        default=DEFAULT_RELEASE_MAX_MB,
        help="Skip downloading release assets larger than this size (MB)",
    )
    parser.add_argument(
        "--duckdb-smoke-max",
        type=int,
        default=50,
        help="Max repos to run DuckDB smoke test for (keeps runtime bounded)",
    )
    parser.add_argument(
        "--duckdb-extension-dir",
        default=".cache/duckdb_extension_smoke",
        help="Extension directory for DuckDB smoke tests",
    )

    parser.add_argument("--verbose", action="store_true", default=False)

    args = parser.parse_args()

    rows = json.loads(Path(args.input).read_text())
    if not isinstance(rows, list):
        raise SystemExit("Input must be a JSON array")

    token = get_github_token()
    headers = build_headers(token)
    cache = JsonFileCache(args.cache_dir, ttl_seconds=args.cache_ttl_seconds)

    con = duckdb.connect(database=":memory:")
    ext_dir = Path(args.duckdb_extension_dir)
    ext_dir.mkdir(parents=True, exist_ok=True)
    con.execute(f"SET extension_directory='{ext_dir.as_posix()}'")

    output_path = Path(args.output)

    out: list[dict] = []
    already_done: set[str] = set()

    if args.resume and output_path.exists():
        try:
            existing = json.loads(output_path.read_text())
            if isinstance(existing, list):
                out = [x for x in existing if isinstance(x, dict)]
                already_done = {x.get("repo") for x in out if isinstance(x.get("repo"), str)}
                already_done.discard("")
                print(f"Resuming: loaded {len(out)} existing rows from {args.output}")
        except Exception:
            pass

    validated = 0
    smoke_tested = 0

    for r in rows:
        if validated >= args.max:
            break

        input_repo = normalise_repo(r.get("repo"))
        if not input_repo:
            continue

        if input_repo in already_done:
            continue

        validated += 1
        if args.verbose or validated == 1 or validated % 25 == 0:
            print(f"Validating {validated}/{args.max}: {input_repo}")

        try:
            repo_details = request_json(
                repo_api(input_repo),
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            ).json()
        except RuntimeError as exc:
            # Repo missing / renamed / access denied. Record and continue.
            out.append(
                {
                    "repo": input_repo,
                    "input_repo": input_repo,
                    "canonical_repo": input_repo,
                    "error": str(exc),
                    "score": 0,
                    "stars": 0,
                    "pushed": None,
                    "archived": None,
                    "topics": [],
                    "signals": {},
                    "duckdb_install_name": None,
                    "duckdb_install_ok": False,
                    "duckdb_load_ok": False,
                    "duckdb_error": None,
                    "release_asset_count": 0,
                    "release_asset_name": None,
                    "release_asset_url": None,
                    "release_load_ok": False,
                    "release_load_error": None,
                }
            )
            continue

        canonical_repo = input_repo
        if isinstance(repo_details, dict) and repo_details.get("fork") is True:
            source = repo_details.get("source") or repo_details.get("parent") or {}
            full_name = source.get("full_name") if isinstance(source, dict) else None
            if isinstance(full_name, str) and full_name:
                canonical_repo = normalise_repo(full_name) or canonical_repo

        # If this is a fork and we have a canonical upstream, re-fetch details for the canonical repo.
        # This avoids duplicate review/label effort.
        if canonical_repo != input_repo:
            if canonical_repo in already_done:
                continue
            try:
                repo_details = request_json(
                    repo_api(canonical_repo),
                    headers,
                    cache=cache,
                    timeout_seconds=args.timeout_seconds,
                    verbose=args.verbose,
                ).json()
            except Exception:
                # Keep fork details if canonical fetch fails.
                pass

        repo = canonical_repo

        topics = repo_details.get("topics") or []
        topics = [t.lower() for t in topics if isinstance(t, str)]

        signals: dict[str, bool] = {
            "is_fork": bool(isinstance(repo_details, dict) and repo_details.get("fork") is True),
        }

        # README keyword signals (fast-ish, cached)
        try:
            rj = request_json(
                readme_api(repo),
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            ).json()
            rt = decode_content(rj) if isinstance(rj, dict) else None
            if rt:
                signals.update(readme_signals(rt))
        except Exception:
            pass

        # Quick checks (cheap) at common root paths
        signals["has_extension_config_cmake"] = (
            try_get_contents(
                repo,
                "extension_config.cmake",
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            )
            is not None
        )

        signals["has_extension_dir"] = (
            try_get_contents(
                repo,
                "extension",
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            )
            is not None
        )

        signals["has_dot_duckdb_extension"] = (
            try_get_contents(
                repo,
                ".duckdb_extension",
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            )
            is not None
        )

        cmake_json = try_get_contents(
            repo,
            "CMakeLists.txt",
            headers,
            cache=cache,
            timeout_seconds=args.timeout_seconds,
            verbose=args.verbose,
        )
        cmake_text = decode_content(cmake_json) if isinstance(cmake_json, dict) else None
        signals["cmake_mentions_duckdb_extension"] = (
            (cmake_text is not None) and looks_like_duckdb_extension_cmake(cmake_text)
        )

        # Git tree scan (better recall): find artefacts anywhere in the repo.
        default_branch = repo_details.get("default_branch")
        tree = None
        if isinstance(default_branch, str) and default_branch:
            tree = get_repo_tree_recursive(
                repo,
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                default_branch=default_branch,
                verbose=args.verbose,
            )

        tree_entries = tree.get("tree") if isinstance(tree, dict) else None
        paths: list[str] = []
        if isinstance(tree_entries, list):
            for e in tree_entries:
                p = e.get("path") if isinstance(e, dict) else None
                if isinstance(p, str):
                    paths.append(p)

        # Flag likely template clones (noise reduction hint).
        signals["is_template_clone"] = is_likely_template_clone(
            repo=repo,
            topics=topics,
            signals=signals,
            paths=paths,
        )

        def _has_suffix(suffix: str) -> bool:
            return any(p.endswith(suffix) for p in paths)

        signals["tree_has_extension_config_cmake"] = _has_suffix("extension_config.cmake")
        signals["tree_has_dot_duckdb_extension"] = _has_suffix(".duckdb_extension")
        signals["tree_has_cmakelists"] = _has_suffix("CMakeLists.txt")

        # Fetch & scan a few nested CMakeLists.txt files (heuristic ordering) for DuckDB extension markers.
        nested_cmake_paths = [p for p in paths if p.endswith("CMakeLists.txt")]

        def _cmake_rank(p: str) -> tuple[int, int, str]:
            # Prefer cmake files near extension-related directories and shallow depth.
            lower = p.lower()
            preference = 2
            if "extension" in lower or lower.startswith("extension/"):
                preference = 0
            elif "/ext/" in f"/{lower}" or lower.startswith("ext/"):
                preference = 1
            depth = p.count("/")
            return (preference, depth, p)

        nested_cmake_paths.sort(key=_cmake_rank)
        nested_cmake_paths = nested_cmake_paths[: max(0, int(args.tree_cmake_max))]

        tree_cmake_mentions = False
        for cmake_path in nested_cmake_paths:
            contents = try_get_contents(
                repo,
                cmake_path,
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            )
            text = decode_content(contents) if isinstance(contents, dict) else None
            if text and looks_like_duckdb_extension_cmake(text):
                tree_cmake_mentions = True
                break

        signals["tree_cmake_mentions_duckdb_extension"] = tree_cmake_mentions

        # Fetch & scan a few likely source files for extension entrypoint markers.
        source_paths = [
            p
            for p in paths
            if p.lower().endswith(
                (
                    ".c",
                    ".cc",
                    ".cpp",
                    ".cxx",
                    ".h",
                    ".hpp",
                    ".rs",
                    ".go",
                    ".py",
                )
            )
        ]

        def _source_rank(p: str) -> tuple[int, int, str]:
            lower = p.lower()
            preference = 3
            if any(k in lower for k in ["extension", "duckdb", "ext/"]):
                preference = 0
            elif lower.startswith("src/"):
                preference = 1
            depth = p.count("/")
            return (preference, depth, p)

        source_paths.sort(key=_source_rank)
        source_paths = source_paths[:5]

        tree_source_mentions = False
        for sp in source_paths:
            contents = try_get_contents(
                repo,
                sp,
                headers,
                cache=cache,
                timeout_seconds=args.timeout_seconds,
                verbose=args.verbose,
            )
            text = decode_content(contents) if isinstance(contents, dict) else None
            if not text:
                continue
            sigs = source_entrypoint_signals(text)
            if sigs.get("source_mentions_duckdb_extension_api"):
                tree_source_mentions = True
                break

        signals["tree_source_mentions_duckdb_extension_api"] = tree_source_mentions

        score, score_breakdown = compute_score_with_breakdown(topics, signals)

        # Optional DuckDB smoke test (INSTALL/LOAD)
        install_ok = False
        load_ok = False
        install_name = None
        install_error = None

        if args.duckdb_smoke_test and smoke_tested < args.duckdb_smoke_max:
            smoke_tested += 1
            candidates = guess_extension_names_from_repo(repo)
            install_ok, load_ok, install_name, install_error = duckdb_install_load_smoke_test(
                con,
                candidates=candidates,
                verbose=args.verbose,
            )

        # Optional: scan releases for binary assets and optionally attempt LOAD from file.
        release_assets: list[dict] = []
        release_asset_name = None
        release_asset_url = None
        release_load_ok = False
        release_load_error = None

        if args.release_scan:
            rels: list[dict] = []
            page = 1
            per_page = 10
            while len(rels) < int(args.release_max):
                resp = request_json(
                    releases_api(repo, per_page=per_page, page=page),
                    headers,
                    cache=cache,
                    timeout_seconds=args.timeout_seconds,
                    verbose=args.verbose,
                ).json()
                if not isinstance(resp, list) or not resp:
                    break
                rels.extend([x for x in resp if isinstance(x, dict)])
                if len(resp) < per_page:
                    break
                page += 1

            rels = rels[: int(args.release_max)]
            release_assets = find_release_extension_assets(rels)

            if release_assets:
                # Pick the smallest asset to avoid huge downloads by default.
                release_assets.sort(key=lambda a: a.get("size") if isinstance(a.get("size"), int) else 10**18)
                chosen = release_assets[0]
                release_asset_name = chosen.get("name") if isinstance(chosen.get("name"), str) else None
                release_asset_url = (
                    chosen.get("browser_download_url") if isinstance(chosen.get("browser_download_url"), str) else None
                )

                if args.release_download and release_asset_url and release_asset_name:
                    downloaded = download_asset(
                        chosen,
                        headers,
                        download_dir=Path(args.release_download_dir),
                        timeout_seconds=args.timeout_seconds,
                        max_mb=int(args.release_max_mb),
                        verbose=args.verbose,
                    )
                    if downloaded is not None:
                        ext_path = maybe_decompress_gz(downloaded)
                        release_load_ok, release_load_error = duckdb_load_from_file(
                            con,
                            path=ext_path,
                            verbose=args.verbose,
                        )

        out.append(
            {
                "repo": repo,
                "input_repo": input_repo,
                "canonical_repo": repo,
                "stars": int(repo_details.get("stargazers_count") or 0),
                "pushed": repo_details.get("pushed_at"),
                "archived": repo_details.get("archived"),
                "topics": topics,
                "signals": signals,
                "score": score,
                "score_breakdown": score_breakdown,
                "duckdb_install_name": install_name,
                "duckdb_install_ok": install_ok,
                "duckdb_load_ok": load_ok,
                "duckdb_error": install_error,
                "release_asset_count": len(release_assets),
                "release_asset_name": release_asset_name,
                "release_asset_url": release_asset_url,
                "release_load_ok": release_load_ok,
                "release_load_error": release_load_error,
                "error": None,
            }
        )

        # Periodic checkpoint writes so we can resume after failures/timeouts.
        if args.checkpoint_every > 0 and (validated % int(args.checkpoint_every) == 0):
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(out, indent=2))
            if args.verbose:
                print(f"Checkpoint: wrote {len(out)} rows to {args.output}")

    # Sort by score then stars.
    out.sort(key=lambda x: (x.get("score", 0), x.get("stars", 0)), reverse=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(out, indent=2))

    ok = sum(1 for r in out if r.get("duckdb_install_ok") and r.get("duckdb_load_ok"))
    print("Validation summary")
    print(f"- validated: {len(out)}")
    print(f"- duckdb smoke tested: {min(len(out), args.duckdb_smoke_max) if args.duckdb_smoke_test else 0}")
    print(f"- duckdb install+load ok: {ok}")
    print(f"- wrote: {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
