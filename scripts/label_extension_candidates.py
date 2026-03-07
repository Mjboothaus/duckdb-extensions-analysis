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


def _relation_exists(con: duckdb.DuckDBPyConnection, name: str) -> bool:
    try:
        row = con.execute(
            """
            SELECT 1
            FROM information_schema.tables
            WHERE table_schema = 'main'
              AND table_name = ?
            LIMIT 1
            """,
            [name],
        ).fetchone()
        return row is not None
    except Exception:
        return False


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
        raise ValueError(
            f"Invalid is_extension={row.is_extension} (expected one of {sorted(VALID_LABELS)})"
        )
    if row.distribution not in VALID_DISTRIBUTIONS:
        raise ValueError(
            f"Invalid distribution={row.distribution} (expected one of {sorted(VALID_DISTRIBUTIONS)})"
        )

    # DuckDB's CURRENT_TIMESTAMP keyword can behave unexpectedly in some contexts.
    # Rely on defaults for created_at/updated_at on insert, and use now() on update.
    con.execute(
        """
        INSERT INTO extension_discovery_labels (repo, is_extension, distribution, notes)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(repo)
        DO UPDATE SET
            is_extension = excluded.is_extension,
            distribution = excluded.distribution,
            notes = excluded.notes,
            updated_at = now();
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
    only_new_or_changed: bool,
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

    # Graceful fallback if the requested view doesn't exist in this DB snapshot.
    if not _relation_exists(con, source_view):
        fallback_order = [
            "recent_extension_discovery_validated",
            "latest_extension_discovery_validated",
            "extension_discovery_validated_with_run",
            "extension_discovery_validated",
        ]
        for fb in fallback_order:
            if _relation_exists(con, fb):
                print(f"⚠️  Missing view '{source_view}'. Falling back to '{fb}'.")
                source_view = fb
                break
        else:
            print(
                f"❌ Missing discovery relation '{source_view}'.\n"
                "Load discovery data into DuckDB first, e.g.:\n"
                "  just discover-load-db <validated.json> <promoted.json>\n"
                "If you're using the separate third-party labelling DB, use:\n"
                "  just thirdparty-load-db <validated.json> <promoted.json>\n"
                "Then retry the label loop."
            )
            return

    promoted_view = "recent_extension_discovery_promoted"
    if only_promoted and not _relation_exists(con, promoted_view):
        promoted_fallbacks = [
            "recent_extension_discovery_promoted",
            "latest_extension_discovery_promoted",
            "extension_discovery_promoted_with_run",
            "extension_discovery_promoted",
        ]
        for fb in promoted_fallbacks:
            if _relation_exists(con, fb):
                print(f"⚠️  Missing view '{promoted_view}'. Falling back to '{fb}'.")
                promoted_view = fb
                break
        else:
            print(
                "⚠️  only-promoted requested but no promoted discovery relation exists; disabling only-promoted."
            )
            only_promoted = False
            promoted_view = (
                "extension_discovery_promoted"  # unused when only_promoted=False
            )

    # If using incremental mode, we need run timestamps.
    if only_new_or_changed and source_view != "extension_discovery_validated_with_run":
        if _relation_exists(con, "extension_discovery_validated_with_run"):
            print(
                f"⚠️  only-new-or-changed requires run metadata; using extension_discovery_validated_with_run instead of {source_view}."
            )
            source_view = "extension_discovery_validated_with_run"
        else:
            print(
                "⚠️  only-new-or-changed requested but extension_discovery_validated_with_run is not available; disabling incremental filter."
            )
            only_new_or_changed = False

    where_bits: list[str] = []
    if unlabeled_only:
        where_bits.append("l.repo IS NULL")
    if only_new_or_changed:
        where_bits.append("l.repo IS NULL OR v.run_timestamp > l.updated_at")
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
        LEFT JOIN {promoted_view} p
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

            upsert_label(
                con,
                LabelRow(
                    repo=repo,
                    is_extension=is_extension,
                    distribution=distribution,
                    notes=notes,
                ),
            )
            updated += 1

    return updated, skipped


def export_labels_only_csv(con: duckdb.DuckDBPyConnection, path: Path) -> None:
    """Export the labels table alone.

    This is used as a low-friction way to persist interactive labelling progress.
    The output schema matches the discovery export schema (extra columns blank), so it
    can be imported by the existing CSV importer.
    """

    path.parent.mkdir(parents=True, exist_ok=True)

    rows = con.execute(
        """
        SELECT repo, is_extension, distribution, COALESCE(notes, '') AS notes
        FROM extension_discovery_labels
        ORDER BY updated_at DESC
        """
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
        for repo, is_extension, distribution, notes in rows:
            w.writerow(
                {
                    "repo": repo,
                    "repo_url": f"https://github.com/{repo}",
                    "score": "",
                    "stars": "",
                    "pushed": "",
                    "release_asset_count": "",
                    "release_asset_name": "",
                    "release_asset_url": "",
                    "is_extension": is_extension,
                    "distribution": distribution,
                    "notes": notes,
                }
            )


def interactive_label(
    con: duckdb.DuckDBPyConnection,
    *,
    limit: int,
    include_already_labelled: bool,
    source_view: str,
    min_score: int | None,
    has_release_assets: bool,
    only_promoted: bool,
    only_new_or_changed: bool,
    autosave_csv: Path | None,
) -> None:
    # Preload known core/community repo identifiers for fast display during the loop.
    # In a discovery-only DB (e.g. third-party labelling DB), these tables won't exist.
    try:
        known_core = {
            r[0]
            for r in con.execute(
                "select distinct repository from core_extensions where repository is not null"
            ).fetchall()
            if isinstance(r[0], str)
        }
    except Exception:
        known_core = set()

    try:
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
    except Exception:
        known_community = set()
    allowed_views = {
        "latest_extension_discovery_validated",
        "recent_extension_discovery_validated",
        "extension_discovery_validated_with_run",
    }
    if source_view not in allowed_views:
        raise ValueError(f"Invalid source view: {source_view}")

    # Graceful fallback if the requested view doesn't exist in this DB snapshot.
    if not _relation_exists(con, source_view):
        fallback_order = [
            "recent_extension_discovery_validated",
            "latest_extension_discovery_validated",
            "extension_discovery_validated_with_run",
            "extension_discovery_validated",
        ]
        for fb in fallback_order:
            if _relation_exists(con, fb):
                print(f"⚠️  Missing view '{source_view}'. Falling back to '{fb}'.")
                source_view = fb
                break
        else:
            print(
                f"❌ Missing discovery relation '{source_view}'.\n"
                "Load discovery data into DuckDB first, e.g.:\n"
                "  just discover-load-db <validated.json> <promoted.json>\n"
                "Then retry the label loop."
            )
            return

    promoted_view = "recent_extension_discovery_promoted"
    if only_promoted:
        if not _relation_exists(con, promoted_view):
            promoted_fallbacks = [
                "recent_extension_discovery_promoted",
                "latest_extension_discovery_promoted",
                "extension_discovery_promoted_with_run",
                "extension_discovery_promoted",
            ]
            for fb in promoted_fallbacks:
                if _relation_exists(con, fb):
                    print(f"⚠️  Missing view '{promoted_view}'. Falling back to '{fb}'.")
                    promoted_view = fb
                    break
            else:
                print(
                    "⚠️  only-promoted requested but no promoted discovery relation exists; disabling only-promoted."
                )
                only_promoted = False

    # If using incremental mode, we need run timestamps.
    if only_new_or_changed and source_view != "extension_discovery_validated_with_run":
        if _relation_exists(con, "extension_discovery_validated_with_run"):
            print(
                f"⚠️  only-new-or-changed requires run metadata; using extension_discovery_validated_with_run instead of {source_view}."
            )
            source_view = "extension_discovery_validated_with_run"
        else:
            print(
                "⚠️  only-new-or-changed requested but extension_discovery_validated_with_run is not available; disabling incremental filter."
            )
            only_new_or_changed = False

    where_bits: list[str] = []
    params: list = []

    if not include_already_labelled:
        where_bits.append("l.repo IS NULL")
    if only_new_or_changed:
        where_bits.append("l.repo IS NULL OR v.run_timestamp > l.updated_at")
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
        LEFT JOIN {promoted_view} p
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
    print("- shortcuts: t (template clone => no + note 'template clone')")
    if autosave_csv is not None:
        print(f"- autosave: {autosave_csv}")

    total = len(rows)

    for idx, (
        repo,
        score,
        stars,
        pushed,
        asset_count,
        asset_name,
        existing_label,
        existing_dist,
    ) in enumerate(rows, start=1):
        url = f"https://github.com/{repo}"
        print("\n---")
        print(f"Progress: {idx}/{total}")
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
            try:
                raw = (
                    input("Label [y/n/u] [distribution] (or skip/quit): ")
                    .strip()
                    .lower()
                )
            except KeyboardInterrupt:
                print("\nInterrupted. Exiting labelling loop without error.")
                return

            if raw in {"quit", "q", "exit"}:
                return
            if raw in {"skip", "s", ""}:
                break

            parts = raw.split()

            # Convenience shortcut: template clones.
            # Entering 't'/'template' labels the repo as a non-extension with a standard note.
            if parts and parts[0] in {"t", "template"}:
                label = "no"
                dist = "unknown"
                notes = "template clone"
            # Convenience: allow entering a distribution directly, interpreted as "yes <distribution>".
            # Example: "community" => yes community
            elif (
                parts
                and parts[0] in VALID_DISTRIBUTIONS
                and parts[0] not in {"unknown"}
            ):
                label = "yes"
                dist = parts[0]
                notes = input("Notes (optional): ").strip()
            else:
                short = parts[0] if parts else ""
                label = {"y": "yes", "n": "no", "u": "unsure"}.get(short)
                if label is None:
                    print(
                        "Invalid label. Use y/n/u, 't' for template clone, or a distribution like 'community', or skip/quit."
                    )
                    continue

                dist = parts[1] if len(parts) > 1 else "unknown"

                if dist not in VALID_DISTRIBUTIONS:
                    print(
                        f"Invalid distribution. Choose from: {', '.join(sorted(VALID_DISTRIBUTIONS))}"
                    )
                    continue

                notes = ""
                if label != "no":
                    notes = input("Notes (optional): ").strip()

            upsert_label(
                con,
                LabelRow(repo=repo, is_extension=label, distribution=dist, notes=notes),
            )

            if autosave_csv is not None:
                export_labels_only_csv(con, autosave_csv)

            print("Saved.")
            break


def print_label_stats(
    con: duckdb.DuckDBPyConnection,
    *,
    source_view: str | None,
    only_promoted: bool,
) -> None:
    total_labels = con.execute(
        "select count(*) from extension_discovery_labels"
    ).fetchone()[0]
    by_label = con.execute(
        "select is_extension, count(*) from extension_discovery_labels group by 1 order by 1"
    ).fetchall()

    template_clones = con.execute(
        """
        select count(*)
        from extension_discovery_labels
        where is_extension = 'no'
          and lower(coalesce(notes, '')) like '%template clone%'
        """
    ).fetchone()[0]

    print("Labelling stats")
    print(f"- labels: {int(total_labels)}")
    if by_label:
        for k, n in by_label:
            print(f"  - {k}: {int(n)}")
    print(f"- template clones (no): {int(template_clones)}")

    if source_view is None:
        return

    if not _relation_exists(con, source_view):
        print(f"- coverage: source view '{source_view}' not available")
        return

    # Total candidates in source.
    total_candidates = con.execute(
        f"select count(*) from (select distinct repo from {source_view})"
    ).fetchone()[0]

    labelled_in_source = con.execute(
        f"""
        select count(*)
        from (select distinct repo from {source_view}) v
        join extension_discovery_labels l on v.repo = l.repo
        """
    ).fetchone()[0]

    if only_promoted:
        promoted_view = "recent_extension_discovery_promoted"
        if not _relation_exists(con, promoted_view):
            promoted_view = "extension_discovery_promoted"

        if _relation_exists(con, promoted_view):
            total_promoted = con.execute(
                f"select count(*) from (select distinct repo from {promoted_view})"
            ).fetchone()[0]
            labelled_promoted = con.execute(
                f"""
                select count(*)
                from (select distinct repo from {promoted_view}) p
                join extension_discovery_labels l on p.repo = l.repo
                """
            ).fetchone()[0]
            print(f"- promoted candidates: {int(total_promoted)}")
            print(f"- promoted labelled: {int(labelled_promoted)}")

    pct = (100.0 * labelled_in_source / total_candidates) if total_candidates else 0.0
    print(f"- candidates in {source_view}: {int(total_candidates)}")
    print(f"- labelled in {source_view}: {int(labelled_in_source)} ({pct:.1f}%)")


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
    p_export.add_argument(
        "--only-new-or-changed",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Only include repos that are new since last label, or whose discovery run is newer than the last label update",
    )

    p_import = sub.add_parser("import", help="Import labels from a CSV")
    p_import.add_argument("path")

    p_stats = sub.add_parser("stats", help="Show labelling coverage and progress")
    p_stats.add_argument(
        "--source",
        choices=[
            "latest_extension_discovery_validated",
            "recent_extension_discovery_validated",
            "extension_discovery_validated_with_run",
        ],
        default="recent_extension_discovery_validated",
        help="Which discovery dataset to use for coverage metrics",
    )
    p_stats.add_argument(
        "--only-promoted",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Also compute coverage for promoted candidates (if promoted view exists)",
    )

    p_loop = sub.add_parser("loop", help="Interactive labelling loop")
    p_loop.add_argument("--limit", type=int, default=50)
    p_loop.add_argument(
        "--autosave-csv",
        default="labels/third_party_extension_labels.csv",
        help="Write a labels-only CSV after each saved label (prevents losing work)",
    )
    p_loop.add_argument(
        "--no-autosave-csv",
        action="store_true",
        help="Disable labels-only CSV autosave",
    )
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
    p_loop.add_argument(
        "--only-new-or-changed",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Only include repos that are new since last label, or whose discovery run is newer than the last label update",
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
            only_new_or_changed=bool(args.only_new_or_changed),
        )
        print(f"Wrote: {args.out}")
        return 0

    if args.cmd == "stats":
        print_label_stats(
            con,
            source_view=str(args.source) if args.source else None,
            only_promoted=bool(args.only_promoted),
        )
        return 0

    if args.cmd == "import":
        updated, skipped = import_csv(con, Path(args.path))
        print(f"Imported labels. Updated: {updated}, skipped: {skipped}")
        return 0

    if args.cmd == "loop":
        autosave_csv = None
        if not bool(args.no_autosave_csv):
            autosave_csv = Path(str(args.autosave_csv))

        interactive_label(
            con,
            limit=int(args.limit),
            include_already_labelled=bool(args.include_already_labelled),
            source_view=str(args.source),
            min_score=args.min_score,
            has_release_assets=bool(args.has_release_assets),
            only_promoted=bool(args.only_promoted),
            only_new_or_changed=bool(args.only_new_or_changed),
            autosave_csv=autosave_csv,
        )
        return 0

    raise SystemExit("Unknown command")


if __name__ == "__main__":
    raise SystemExit(main())
