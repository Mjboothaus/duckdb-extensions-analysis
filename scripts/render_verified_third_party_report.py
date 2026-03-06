"""Render a report of labelled third-party DuckDB extensions.

This report is driven by *labels* in `data/extensions.duckdb`, but (by default)
refreshes GitHub metadata at render time so it stays aligned with the main
core/community reports.

The intent is that you can iteratively label candidates as you discover them,
then generate a local "verified third-party" report that looks and feels like
the primary report output.

This script is designed to be runnable in GitHub Actions.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from datetime import UTC, datetime
from pathlib import Path

import duckdb
import httpx
from loguru import logger

# Ensure repo-root imports work when executing as a script.
sys.path.insert(0, str(Path(__file__).parent.parent))

from conf.config import Config  # noqa: E402
from scripts.analyse_discovered_extensions import normalise_repo_identifier  # noqa: E402
from scripts.label_extension_candidates import ensure_schema  # noqa: E402
from src.analyzers.github_api import GitHubAPIClient  # noqa: E402
from src.templates import TemplateEngine  # noqa: E402


def _load_known_repos_from_con(con: duckdb.DuckDBPyConnection) -> set[str]:
    """Load known core/community repo identifiers from the current DB connection."""

    known: set[str] = set()

    def add_many(values: list[object]) -> None:
        for v in values:
            if v is None or not isinstance(v, str):
                continue
            norm = normalise_repo_identifier(v)
            if norm:
                known.add(norm)

    for col in ["repository", "github_url", "community_repo_url"]:
        try:
            rows = con.execute(
                f"select {col} from community_extensions where {col} is not null"
            ).fetchall()
            add_many([r[0] for r in rows])
        except Exception:
            pass

    try:
        rows = con.execute(
            "select repository from core_extensions where repository is not null"
        ).fetchall()
        add_many([r[0] for r in rows])
    except Exception:
        pass

    return known


def _relation_exists(con: duckdb.DuckDBPyConnection, name: str) -> bool:
    """Return True if a table/view exists in the current connection."""

    try:
        row = con.execute(
            """
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = ?
            LIMIT 1
            """,
            [name],
        ).fetchone()
        return row is not None
    except Exception:
        return False


def _get_candidate_repos(
    con: duckdb.DuckDBPyConnection,
    *,
    source: str,
    known_repos: set[str],
) -> list[dict[str, str]]:
    """Return candidate repos (labelled yes) not already tracked as core/community."""

    if source == "latest":
        validated_view = "latest_extension_discovery_validated"
        fallback_view = "extension_discovery_validated_with_run"
    elif source == "recent":
        validated_view = "recent_extension_discovery_validated"
        fallback_view = "extension_discovery_validated_with_run"
    else:
        validated_view = "extension_discovery_validated_with_run"
        fallback_view = "extension_discovery_validated_with_run"

    if not _relation_exists(con, validated_view):
        if validated_view != fallback_view and _relation_exists(con, fallback_view):
            logger.warning(
                f"Missing relation '{validated_view}', falling back to '{fallback_view}'"
            )
            validated_view = fallback_view
        else:
            logger.warning(
                f"Missing relation '{validated_view}'. No discovery data available; third-party report will be empty."
            )
            return []

    rows = con.execute(
        f"""
        WITH v AS (
            SELECT *
            FROM {validated_view}
            QUALIFY row_number() OVER (
                PARTITION BY repo
                ORDER BY pushed DESC NULLS LAST, score DESC, stars DESC
            ) = 1
        )
        SELECT
            v.repo,
            v.url AS repo_url,
            l.distribution,
            l.notes
        FROM v
        JOIN extension_discovery_labels l
            ON v.repo = l.repo
        WHERE l.is_extension = 'yes'
        """
    ).fetchall()

    results: list[dict[str, str]] = []
    for repo, repo_url, distribution, notes in rows:
        if repo in known_repos:
            continue
        results.append(
            {
                "repo": repo,
                "repo_url": repo_url or f"https://github.com/{repo}",
                "distribution": distribution or "unknown",
                "notes": (notes or "").strip(),
            }
        )

    return results


def _parse_pushed_at(pushed_at: object) -> datetime | None:
    if pushed_at is None:
        return None
    if isinstance(pushed_at, datetime):
        return pushed_at
    if isinstance(pushed_at, str):
        try:
            return datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def _days_ago(ts: datetime | None, *, now: datetime) -> int | None:
    if ts is None:
        return None
    return (now - ts).days


def _status_from_repo_info(repo_info: dict) -> str:
    if repo_info.get("archived") is True:
        return "archived"
    return "ongoing"


async def _build_third_party_extensions(
    config: Config,
    candidates: list[dict[str, str]],
    *,
    cache_hours: int,
) -> list[dict[str, object]]:
    """Fetch GitHub info for labelled repos and shape it for template rendering."""

    api = GitHubAPIClient(config, cache_hours=cache_hours)
    now = datetime.now(UTC)

    extensions: list[dict[str, object]] = []
    async with httpx.AsyncClient() as client:
        for cand in candidates:
            repo_path = cand["repo"]
            repo_info = await api.get_repository_info(client, repo_path)

            if not repo_info:
                extensions.append(
                    {
                        "name": repo_path,
                        "repository": repo_path,
                        "docs_url": cand["repo_url"],
                        "status": "unknown",
                        "last_push_days": None,
                        "last_push": None,
                        "stars": 0,
                        "language": "N/A",
                        "description": cand["notes"] or "No description available",
                        "topics": [],
                        "distribution": cand["distribution"],
                    }
                )
                continue

            pushed_at = _parse_pushed_at(repo_info.get("pushed_at"))
            last_push_days = _days_ago(pushed_at, now=now)

            extensions.append(
                {
                    "name": repo_info.get("name") or repo_path,
                    "repository": repo_path,
                    # No canonical docs URL; link extension name to the repo.
                    "docs_url": cand["repo_url"],
                    "status": _status_from_repo_info(repo_info),
                    "last_push_days": last_push_days,
                    "last_push": pushed_at.isoformat().replace("+00:00", "Z") if pushed_at else None,
                    "stars": repo_info.get("stargazers_count") or 0,
                    "language": repo_info.get("language") or "N/A",
                    "description": (
                        repo_info.get("description")
                        or cand["notes"]
                        or "No description available"
                    ),
                    "topics": repo_info.get("topics") or [],
                    "distribution": cand["distribution"],
                }
            )

    # Most-recent activity first.
    extensions.sort(
        key=lambda e: (e.get("last_push_days") is None, e.get("last_push_days") or 10**9)
    )
    return extensions


async def _render_report(*, args: argparse.Namespace) -> int:
    config = Config()
    config.ensure_directories()

    db_path = Path(args.db)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(str(db_path))
    ensure_schema(con)

    known_repos = _load_known_repos_from_con(con)
    candidates = _get_candidate_repos(con, source=args.source, known_repos=known_repos)

    cache_hours = 0 if args.no_cache else config.default_cache_hours

    if args.refresh_github:
        third_party_extensions = await _build_third_party_extensions(
            config, candidates, cache_hours=cache_hours
        )
    else:
        third_party_extensions = [
            {
                "name": c["repo"],
                "repository": c["repo"],
                "docs_url": c["repo_url"],
                "status": "unknown",
                "last_push_days": None,
                "last_push": None,
                "stars": 0,
                "language": "N/A",
                "description": c["notes"] or "No description available",
                "topics": [],
                "distribution": c["distribution"],
            }
            for c in candidates
        ]

    engine = TemplateEngine(config, Path(config.project_root) / "templates")

    analysis_result: dict[str, object] = {
        "core_extensions": [],
        "community_extensions": [],
        "third_party_extensions": third_party_extensions,
        "duckdb_version_info": {"version": None, "release_date": None},
        "analysis_timestamp": datetime.now(UTC),
        "url_validation_results": {},
        "stats": {},
    }

    rendered = engine.render_report("third_party_verified", analysis_result)
    out_path.write_text(rendered.strip() + "\n", encoding="utf-8")
    logger.info(f"Wrote: {out_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a Markdown report of labelled third-party DuckDB extensions"
    )
    parser.add_argument("--db", default="data/extensions.duckdb")
    parser.add_argument(
        "--out",
        default="reports/third_party_extensions_verified.md",
        help="Where to write the Markdown report",
    )
    parser.add_argument(
        "--source",
        choices=["latest", "recent", "all_runs"],
        default="latest",
        help="Which discovery dataset to base the report on",
    )
    parser.add_argument(
        "--refresh-github",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Fetch fresh GitHub metadata at render time",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Bypass HTTP caching for GitHub API requests",
    )

    args = parser.parse_args()
    return asyncio.run(_render_report(args=args))


if __name__ == "__main__":
    raise SystemExit(main())
