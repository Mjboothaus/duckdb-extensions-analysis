import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path

import duckdb


GITHUB_REPO_RE = re.compile(r"github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)")


def normalise_repo_identifier(value: str | None) -> str | None:
    """Normalise various repo identifiers to `owner/repo`.

    Inputs may be:
    - owner/repo
    - https://github.com/owner/repo
    - https://github.com/owner/repo/tree/main/...
    """

    if not value:
        return None

    value = value.strip()
    if not value:
        return None

    if value.startswith("http://") or value.startswith("https://"):
        m = GITHUB_REPO_RE.search(value)
        if not m:
            return None
        return f"{m.group('owner')}/{m.group('repo')}"

    # Basic guard for non-repo strings.
    if "/" not in value:
        return None

    owner, repo, *_rest = value.split("/")
    if not owner or not repo:
        return None

    return f"{owner}/{repo}"


def load_json(path: Path) -> list[dict]:
    with path.open() as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON array")
    return [x for x in data if isinstance(x, dict)]


@dataclass
class KnownRepos:
    repos: set[str]


def load_known_repos_from_db(db_path: Path) -> KnownRepos:
    con = duckdb.connect(str(db_path), read_only=True)

    # Both tables and views exist depending on config; core/community are stable names.
    # We read a union of repository-style columns.
    known: set[str] = set()

    def add_many(values: list[str | None]) -> None:
        for v in values:
            norm = normalise_repo_identifier(v)
            if norm:
                known.add(norm)

    # Community
    for col in ["repository", "github_url", "community_repo_url"]:
        try:
            rows = con.execute(f"select {col} from community_extensions where {col} is not null").fetchall()
            add_many([r[0] for r in rows])
        except Exception:
            pass

    # Core
    try:
        rows = con.execute("select repository from core_extensions where repository is not null").fetchall()
        add_many([r[0] for r in rows])
    except Exception:
        pass

    return KnownRepos(repos=known)


def write_json(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump(rows, f, indent=2)


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["repo", "url", "stars", "lang", "pushed", "desc"]
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyse discovered GitHub repos vs known DuckDB extension repos and output novel candidates"
    )
    parser.add_argument("input", help="JSON produced by scripts/discover_additional_extensions.py")
    parser.add_argument(
        "--db",
        default="data/extensions.duckdb",
        help="DuckDB database path used by the main pipeline (to identify already-known repos)",
    )
    parser.add_argument(
        "--output-json",
        default="data/discovery/novel_extension_candidates.json",
        help="Where to write filtered candidate repos (JSON)",
    )
    parser.add_argument(
        "--output-csv",
        default="data/discovery/novel_extension_candidates.csv",
        help="Where to write filtered candidate repos (CSV)",
    )
    parser.add_argument(
        "--exclude-owner",
        action="append",
        default=[],
        help="Exclude repos owned by this GitHub account/org (repeatable)",
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=0,
        help="Exclude repos with fewer than this many stars",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    db_path = Path(args.db)

    discovered = load_json(input_path)
    known = load_known_repos_from_db(db_path)

    exclude_owners = set(args.exclude_owner)

    unique_by_repo: dict[str, dict] = {}
    for r in discovered:
        repo = normalise_repo_identifier(r.get("repo"))
        if not repo:
            continue

        owner = repo.split("/", 1)[0]
        if owner in exclude_owners:
            continue

        stars = r.get("stars")
        stars = stars if isinstance(stars, int) else 0
        if stars < args.min_stars:
            continue

        # Keep the best row if we see duplicates.
        existing = unique_by_repo.get(repo)
        if existing is None or stars > (existing.get("stars") if isinstance(existing.get("stars"), int) else 0):
            unique_by_repo[repo] = {
                "repo": repo,
                "url": r.get("url") or "",
                "stars": stars,
                "lang": r.get("lang"),
                "pushed": r.get("pushed"),
                "desc": r.get("desc") or "",
            }

    unique_discovered = list(unique_by_repo.values())

    overlap = [r for r in unique_discovered if r["repo"] in known.repos]
    novel = [r for r in unique_discovered if r["repo"] not in known.repos]

    # Sort novel candidates by stars then last pushed (best-effort).
    novel.sort(key=lambda x: (x.get("stars", 0), x.get("pushed") or ""), reverse=True)

    out_json = Path(args.output_json)
    out_csv = Path(args.output_csv)

    write_json(out_json, novel)
    write_csv(out_csv, novel)

    print("Discovery analysis summary")
    print(f"- input rows: {len(discovered)}")
    print(f"- unique repos: {len(unique_discovered)}")
    print(f"- known repos (db): {len(known.repos)}")
    print(f"- overlap with known: {len(overlap)}")
    print(f"- novel candidates: {len(novel)}")
    print(f"- wrote: {out_json}")
    print(f"- wrote: {out_csv}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
