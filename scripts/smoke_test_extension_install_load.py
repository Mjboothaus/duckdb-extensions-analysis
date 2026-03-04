import argparse
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path

import duckdb


GITHUB_REPO_RE = re.compile(r"^(?P<owner>[^/]+)/(?P<repo>[^/]+)$")


def load_json_array(path: Path) -> list[dict]:
    with path.open() as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Expected JSON array")
    return [x for x in data if isinstance(x, dict)]


def write_json(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump(rows, f, indent=2)


def normalise_repo(repo: str | None) -> str | None:
    if not repo:
        return None
    repo = repo.strip()
    if repo.startswith("http://") or repo.startswith("https://"):
        # Best-effort parse for already-enriched inputs.
        m = re.search(r"github\.com/([^/]+)/([^/]+)", repo)
        if not m:
            return None
        return f"{m.group(1)}/{m.group(2)}"

    m = GITHUB_REPO_RE.match(repo)
    if not m:
        return None
    return repo


def guess_extension_names_from_repo(repo: str) -> list[str]:
    """Generate a small set of likely DuckDB extension names from a repo slug."""

    _, repo_name = repo.split("/", 1)

    candidates: list[str] = []

    def add(name: str) -> None:
        name = name.strip().lower()
        if not name:
            return
        if name not in candidates:
            candidates.append(name)

    add(repo_name)

    # Common patterns.
    if repo_name.startswith("duckdb-"):
        add(repo_name.removeprefix("duckdb-"))
    if repo_name.endswith("-duckdb"):
        add(repo_name.removesuffix("-duckdb"))
    if repo_name.endswith("_duckdb"):
        add(repo_name.removesuffix("_duckdb"))
    if repo_name.startswith("duckdb_"):
        add(repo_name.removeprefix("duckdb_"))

    # Some repos use an extension prefix/suffix.
    if repo_name.endswith("-extension"):
        add(repo_name.removesuffix("-extension"))
    if repo_name.startswith("duckdb-extension-"):
        add(repo_name.removeprefix("duckdb-extension-"))

    # Replace hyphens with underscores as a common install-name variant.
    for c in list(candidates):
        add(c.replace("-", "_"))

    return candidates[:6]


@dataclass
class SmokeTestResult:
    repo: str
    tried_names: list[str]
    install_name: str | None
    install_ok: bool
    load_ok: bool
    error: str | None
    seconds: float


def duckdb_smoke_test(
    con: duckdb.DuckDBPyConnection,
    *,
    ext_name_candidates: list[str],
    sleep_seconds: float,
    verbose: bool,
) -> SmokeTestResult:
    start = time.time()
    last_error: str | None = None

    for name in ext_name_candidates:
        try:
            if verbose:
                print(f"  Trying INSTALL/LOAD {name}")

            con.execute(f"INSTALL {name}")
            con.execute(f"LOAD {name}")

            elapsed = time.time() - start
            return SmokeTestResult(
                repo="",
                tried_names=ext_name_candidates,
                install_name=name,
                install_ok=True,
                load_ok=True,
                error=None,
                seconds=elapsed,
            )
        except Exception as exc:
            last_error = str(exc)
            # DuckDB might have partially installed; keep going.
            time.sleep(sleep_seconds)
            continue

    elapsed = time.time() - start
    return SmokeTestResult(
        repo="",
        tried_names=ext_name_candidates,
        install_name=None,
        install_ok=False,
        load_ok=False,
        error=last_error,
        seconds=elapsed,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Attempt DuckDB INSTALL/LOAD for discovered extension candidates (best-effort, heuristic)"
    )
    parser.add_argument(
        "input",
        help="JSON list with at least a 'repo' field (e.g. owner/repo) - typically novel candidates output",
    )
    parser.add_argument(
        "--output",
        default="data/discovery/duckdb_install_load_smoke_test.json",
        help="Where to write results JSON",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=50,
        help="Max repos to test",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.2,
        help="Sleep between candidate name attempts",
    )
    parser.add_argument(
        "--extension-dir",
        default=".cache/duckdb_extension_smoke",
        help="Local extension directory used for installs (keeps test installs isolated)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Verbose output",
    )

    args = parser.parse_args()

    rows = load_json_array(Path(args.input))

    # Ensure local extension dir.
    ext_dir = Path(args.extension_dir)
    ext_dir.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(database=":memory:")
    # Keep installs isolated to the repo.
    con.execute(f"SET extension_directory='{ext_dir.as_posix()}'")

    results: list[dict] = []

    tested = 0
    for idx, r in enumerate(rows, start=1):
        if tested >= args.max:
            break

        repo = normalise_repo(r.get("repo"))
        if not repo:
            continue

        tested += 1
        candidates = guess_extension_names_from_repo(repo)

        if args.verbose or tested == 1 or tested % 10 == 0:
            print(f"Testing {tested}/{args.max}: {repo} (candidates={candidates})")

        res = duckdb_smoke_test(
            con,
            ext_name_candidates=candidates,
            sleep_seconds=args.sleep,
            verbose=args.verbose,
        )
        res.repo = repo

        results.append(
            {
                "repo": res.repo,
                "tried_names": res.tried_names,
                "install_name": res.install_name,
                "install_ok": res.install_ok,
                "load_ok": res.load_ok,
                "error": res.error,
                "seconds": res.seconds,
            }
        )

    write_json(Path(args.output), results)

    ok = sum(1 for r in results if r.get("install_ok") and r.get("load_ok"))
    print("Smoke test summary")
    print(f"- tested: {len(results)}")
    print(f"- install+load ok: {ok}")
    print(f"- wrote: {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
