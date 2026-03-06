import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import duckdb


VALID_LABELS = {"yes", "no", "unsure"}
VALID_DISTRIBUTIONS = {
    "core",
    "community",
    "releases",
    "custom_repo",
    "local_file",
    "remote_url",
    "source_build",
    "unknown",
}


@dataclass
class LabelRow:
    repo: str
    is_extension: str
    distribution: str
    notes: str


def ensure_schema(con: duckdb.DuckDBPyConnection) -> None:
    """Ensure label schema exists.

    This helper is used by both interactive labelling and report rendering.
    It must tolerate databases that do not have the discovery tables/views yet.
    """

    con.execute(
        """
        CREATE TABLE IF NOT EXISTS extension_discovery_labels (
            repo VARCHAR PRIMARY KEY,
            is_extension VARCHAR NOT NULL,
            distribution VARCHAR NOT NULL DEFAULT 'unknown',
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    # Optional convenience view (only if the validated view exists).
    try:
        exists = con.execute(
            """
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'latest_extension_discovery_validated'
            LIMIT 1
            """
        ).fetchone()
    except Exception:
        exists = None

    if exists:
        con.execute(
            """
            CREATE OR REPLACE VIEW latest_extension_discovery_labeled AS
            SELECT
                v.*, 
                l.is_extension,
                l.distribution,
                l.notes AS label_notes,
                l.updated_at AS label_updated_at
            FROM latest_extension_discovery_validated v
            LEFT JOIN extension_discovery_labels l
                ON v.repo = l.repo;
            """
        )


def upsert_label(con: duckdb.DuckDBPyConnection, row: LabelRow) -> None:
    if row.is_extension not in VALID_LABELS:
        raise ValueError(f"Invalid is_extension={row.is_extension} (expected one of {sorted(VALID_LABELS)})")
    if row.distribution not in VALID_DISTRIBUTIONS:
        raise ValueError(f"Invalid distribution={row.distribution} (expected one of {sorted(VALID_DISTRIBUTIONS)})")

    con.execute(
        """
        INSERT INTO extension_discovery_labels (repo, is_extension, distribution, notes, created_at, updated_at)
        VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        ON CONFLICT(repo)
        DO UPDATE SET
            is_extension = excluded.is_extension,
            distribution = excluded.distribution,
            notes = excluded.notes,
            updated_at = CURRENT_TIMESTAMP;
        """,
        [row.repo, row.is_extension, row.distribution, row.notes],
    )


def export_csv(
    con: duckdb.DuckDBPyConnection,
    path: Path,
    *,
    unlabeled_only: bool,
    source_view: str,
    min_score: int | None,
    has_release_assets: bool,
    only_promoted: bool,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    # Defensive: prevent arbitrary SQL injection via view name.
    allowed_views = {
        "latest_extension_discovery_validated",
        "recent_extension_discovery_validated",
        "extension_discovery_validated_with_run",
    }
    if source_view not in allowed_views:
        raise ValueError(f"Invalid source view: {source_view}")

    where_bits: list[str] = []
    if unlabeled_only:
        where_bits.append("l.repo IS NULL")
    if min_score is not None:
        where_bits.append("v.score >= ?")
    if has_release_assets:
        where_bits.append("COALESCE(v.release_asset_count, 0) > 0")
    if only_promoted:
        where_bits.append("p.repo IS NOT NULL")

    where = f"WHERE {' AND '.join(where_bits)}" if where_bits else ""

    params: list = []
    if min_score is not None:
        params.append(int(min_score))

    rows = con.execute(
        f"""
        SELECT
            v.repo,
            v.url AS repo_url,
            v.score,
            v.stars,
            v.pushed,
            v.release_asset_count,
            v.release_asset_name,
            v.release_asset_url AS release_asset_url,
            COALESCE(l.is_extension, '') AS is_extension,
            COALESCE(l.distribution, '') AS distribution,
            COALESCE(l.notes, '') AS notes
        FROM (
            SELECT *
            FROM {source_view}
            QUALIFY row_number() OVER (
                PARTITION BY repo
                ORDER BY pushed DESC NULLS LAST, score DESC, stars DESC
            ) = 1
        ) v
        LEFT JOIN extension_discovery_labels l
            ON v.repo = l.repo
        LEFT JOIN recent_extension_discovery_promoted p
            ON v.repo = p.repo
        {where}
        ORDER BY v.score DESC, v.stars DESC;
        """,
        params,
    ).fetchall()

    fieldnames = [
        "repo",
        "repo_url",
        "score",
        "stars",
        "pushed",
        "release_asset_count",
        "release_asset_name",
        "release_asset_url",
        "is_extension",
        "distribution",
        "notes",
    ]

    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(dict(zip(fieldnames, r, strict=True)))


def import_csv(con: duckdb.DuckDBPyConnection, path: Path) -> tuple[int, int]:
    with path.open() as f:
        reader = csv.DictReader(f)
        updated = 0
        skipped = 0

        for row in reader:
            repo = (row.get("repo") or "").strip()
            if not repo:
                skipped += 1
                continue

            is_extension = (row.get("is_extension") or "").strip().lower()
            distribution = (row.get("distribution") or "unknown").strip().lower()
            notes = (row.get("notes") or "").strip()

            if not is_extension:
                skipped += 1
                continue

            if is_extension not in VALID_LABELS:
                raise ValueError(f"Row {repo}: invalid is_extension={is_extension}")
            if distribution not in VALID_DISTRIBUTIONS:
                raise ValueError(f"Row {repo}: invalid distribution={distribution}")

            upsert_label(con, LabelRow(repo=repo, is_extension=is_extension, distribution=distribution, notes=notes))
            updated += 1

    return updated, skipped


def interactive_label(
    con: duckdb.DuckDBPyConnection,
    *,
    limit: int,
    include_already_labelled: bool,
    source_view: str,
    min_score: int | None,
    has_release_assets: bool,
    only_promoted: bool,
) -> None:
    # Preload known core/community repo identifiers for fast display during the loop.
    known_core = {
        r[0]
        for r in con.execute(
            "select distinct repository from core_extensions where repository is not null"
        ).fetchall()
        if isinstance(r[0], str)
    }
    known_community = {
        r[0]
        for r in con.execute(
            "select distinct repository from community_extensions where repository is not null"
        ).fetchall()
        if isinstance(r[0], str)
    }
    # Normalise community GitHub URLs too.
    for (u,) in con.execute(
        "select distinct github_url from community_extensions where github_url is not null"
    ).fetchall():
        if not isinstance(u, str):
            continue
        if "github.com/" not in u:
            continue
        tail = u.split("github.com/", 1)[1]
        parts = tail.split("/")
        if len(parts) >= 2:
            known_community.add(f"{parts[0]}/{parts[1]}")
    allowed_views = {
        "latest_extension_discovery_validated",
        "recent_extension_discovery_validated",
        "extension_discovery_validated_with_run",
    }
    if source_view not in allowed_views:
        raise ValueError(f"Invalid source view: {source_view}")

    where_bits: list[str] = []
    params: list = []

    if not include_already_labelled:
        where_bits.append("l.repo IS NULL")
    if min_score is not None:
        where_bits.append("v.score >= ?")
        params.append(int(min_score))
    if has_release_assets:
        where_bits.append("COALESCE(v.release_asset_count, 0) > 0")
    if only_promoted:
        where_bits.append("p.repo IS NOT NULL")

    where = f"WHERE {' AND '.join(where_bits)}" if where_bits else ""

    # limit param last
    params.append(int(limit))

    rows = con.execute(
        f"""
        SELECT
            v.repo,
            v.score,
            v.stars,
            v.pushed,
            v.release_asset_count,
            v.release_asset_name,
            COALESCE(l.is_extension, '') AS is_extension,
            COALESCE(l.distribution, '') AS distribution
        FROM (
            SELECT *
            FROM {source_view}
            QUALIFY row_number() OVER (
                PARTITION BY repo
                ORDER BY pushed DESC NULLS LAST, score DESC, stars DESC
            ) = 1
        ) v
        LEFT JOIN extension_discovery_labels l
            ON v.repo = l.repo
        LEFT JOIN recent_extension_discovery_promoted p
            ON v.repo = p.repo
        {where}
        ORDER BY v.score DESC, v.stars DESC
        LIMIT ?;
        """,
        params,
    ).fetchall()

    print("Interactive labelling")
    print("- enter: y/n/u (yes/no/unsure)")
    print("- optionally: y releases  (distribution)")
    print("- commands: skip, quit")

    for (repo, score, stars, pushed, asset_count, asset_name, existing_label, existing_dist) in rows:
        url = f"https://github.com/{repo}"
        print("\n---")
        print(f"Repo:  {repo}")
        print(f"URL:   {url}")
        print(f"Score: {score}   Stars: {stars}   Pushed: {pushed}")
        print(f"Assets: {asset_count}   Sample: {asset_name or ''}")

        # Helpful context: whether your *current DB* already tracks it as core/community.
        in_core = repo in known_core
        in_community = repo in known_community
        print(f"Known in DB: core={in_core} community={in_community}")

        if existing_label:
            print(f"Current label: {existing_label} (distribution={existing_dist})")

        while True:
            raw = input("Label [y/n/u] [distribution] (or skip/quit): ").strip().lower()
            if raw in {"quit", "q", "exit"}:
                return
            if raw in {"skip", "s", ""}:
                break

            parts = raw.split()

            # Convenience: allow entering a distribution directly, interpreted as "yes <distribution>".
            # Example: "community" => yes community
            if parts and parts[0] in VALID_DISTRIBUTIONS and parts[0] not in {"unknown"}:
                label = "yes"
                dist = parts[0]
            else:
                short = parts[0] if parts else ""
                label = {"y": "yes", "n": "no", "u": "unsure"}.get(short)
                if label is None:
                    print("Invalid label. Use y/n/u, or a distribution like 'community', or skip/quit.")
                    continue

                dist = parts[1] if len(parts) > 1 else "unknown"

            if dist not in VALID_DISTRIBUTIONS:
                print(f"Invalid distribution. Choose from: {', '.join(sorted(VALID_DISTRIBUTIONS))}")
                continue

            notes = ""
            if label != "no":
                notes = input("Notes (optional): ").strip()

            upsert_label(con, LabelRow(repo=repo, is_extension=label, distribution=dist, notes=notes))
            print("Saved.")
            break


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Label extension candidates (yes/no/unsure) and optionally distribution type"
    )
    parser.add_argument("--db", default="data/extensions.duckdb")

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_export = sub.add_parser("export", help="Export candidates+labels to CSV")
    p_export.add_argument("--out", default="data/discovery/labels_export.csv")
    p_export.add_argument(
        "--source",
        choices=[
            "latest_extension_discovery_validated",
            "recent_extension_discovery_validated",
            "extension_discovery_validated_with_run",
        ],
        default="latest_extension_discovery_validated",
        help="Which discovery dataset to export",
    )
    p_export.add_argument(
        "--unlabeled-only",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Export only repos that have no label yet",
    )
    p_export.add_argument("--min-score", type=int, default=None)
    p_export.add_argument(
        "--has-release-assets",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Only include repos that have one or more .duckdb_extension release assets",
    )
    p_export.add_argument(
        "--only-promoted",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Only include repos that appear in recent_extension_discovery_promoted",
    )

    p_import = sub.add_parser("import", help="Import labels from a CSV")
    p_import.add_argument("path")

    p_loop = sub.add_parser("loop", help="Interactive labelling loop")
    p_loop.add_argument("--limit", type=int, default=50)
    p_loop.add_argument(
        "--source",
        choices=[
            "latest_extension_discovery_validated",
            "recent_extension_discovery_validated",
            "extension_discovery_validated_with_run",
        ],
        default="latest_extension_discovery_validated",
        help="Which discovery dataset to label from",
    )
    p_loop.add_argument(
        "--include-already-labelled",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Include already labelled repos in the loop",
    )
    p_loop.add_argument("--min-score", type=int, default=None)
    p_loop.add_argument(
        "--has-release-assets",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Only include repos that have one or more .duckdb_extension release assets",
    )
    p_loop.add_argument(
        "--only-promoted",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Only include repos that appear in recent_extension_discovery_promoted",
    )

    args = parser.parse_args()

    con = duckdb.connect(args.db)
    ensure_schema(con)

    if args.cmd == "export":
        export_csv(
            con,
            Path(args.out),
            unlabeled_only=bool(args.unlabeled_only),
            source_view=str(args.source),
            min_score=args.min_score,
            has_release_assets=bool(args.has_release_assets),
            only_promoted=bool(args.only_promoted),
        )
        print(f"Wrote: {args.out}")
        return 0

    if args.cmd == "import":
        updated, skipped = import_csv(con, Path(args.path))
        print(f"Imported labels. Updated: {updated}, skipped: {skipped}")
        return 0

    if args.cmd == "loop":
        interactive_label(
            con,
            limit=int(args.limit),
            include_already_labelled=bool(args.include_already_labelled),
            source_view=str(args.source),
            min_score=args.min_score,
            has_release_assets=bool(args.has_release_assets),
            only_promoted=bool(args.only_promoted),
        )
        return 0

    raise SystemExit("Unknown command")


if __name__ == "__main__":
    raise SystemExit(main())
