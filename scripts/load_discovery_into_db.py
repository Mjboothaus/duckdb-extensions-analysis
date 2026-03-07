import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import duckdb


@dataclass
class Inputs:
    validated_json: Path
    promoted_json: Path | None


def load_json_array(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON array: {path}")
    return [x for x in data if isinstance(x, dict)]


def ensure_schema(con: duckdb.DuckDBPyConnection) -> None:
    con.execute(
        """
        CREATE SEQUENCE IF NOT EXISTS extension_discovery_runs_seq;

        CREATE TABLE IF NOT EXISTS extension_discovery_runs (
            id BIGINT PRIMARY KEY DEFAULT nextval('extension_discovery_runs_seq'),
            run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            notes TEXT
        );

        CREATE TABLE IF NOT EXISTS extension_discovery_validated (
            run_id BIGINT,
            repo VARCHAR,
            url VARCHAR,
            score INTEGER,
            stars INTEGER,
            pushed TIMESTAMP,
            archived BOOLEAN,
            topics VARCHAR[],
            signals JSON,
            release_asset_count INTEGER,
            release_asset_name VARCHAR,
            release_asset_url VARCHAR,
            release_load_ok BOOLEAN,
            release_load_error VARCHAR,
            error VARCHAR,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS extension_discovery_promoted (
            run_id BIGINT,
            repo VARCHAR,
            url VARCHAR,
            score INTEGER,
            stars INTEGER,
            pushed TIMESTAMP,
            release_asset_count INTEGER,
            release_asset_name VARCHAR,
            release_load_ok BOOLEAN,
            reason VARCHAR,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE OR REPLACE VIEW latest_extension_discovery_run AS
        SELECT *
        FROM extension_discovery_runs
        ORDER BY run_timestamp DESC
        LIMIT 1;

        CREATE OR REPLACE VIEW latest_extension_discovery_validated AS
        SELECT v.*
        FROM extension_discovery_validated v
        JOIN latest_extension_discovery_run r ON v.run_id = r.id;

        CREATE OR REPLACE VIEW latest_extension_discovery_promoted AS
        SELECT p.*
        FROM extension_discovery_promoted p
        JOIN latest_extension_discovery_run r ON p.run_id = r.id;

        -- Convenience views for tooling that expects a "recent" dataset.
        -- For now, treat "recent" as "latest" (latest discovery run).
        CREATE OR REPLACE VIEW recent_extension_discovery_validated AS
        SELECT *
        FROM latest_extension_discovery_validated;

        CREATE OR REPLACE VIEW recent_extension_discovery_promoted AS
        SELECT *
        FROM latest_extension_discovery_promoted;

        -- Views that include run metadata for cross-run analysis.
        CREATE OR REPLACE VIEW extension_discovery_validated_with_run AS
        SELECT v.*, r.run_timestamp
        FROM extension_discovery_validated v
        JOIN extension_discovery_runs r ON v.run_id = r.id;

        CREATE OR REPLACE VIEW extension_discovery_promoted_with_run AS
        SELECT p.*, r.run_timestamp
        FROM extension_discovery_promoted p
        JOIN extension_discovery_runs r ON p.run_id = r.id;
        """
    )


def insert_run(con: duckdb.DuckDBPyConnection, notes: str | None) -> int:
    # DuckDB does not expose a universal lastval() like Postgres.
    # Use a RETURNING clause to retrieve the generated ID.
    run_id = con.execute(
        "INSERT INTO extension_discovery_runs(notes) VALUES (?) RETURNING id",
        [notes],
    ).fetchone()[0]
    return int(run_id)


def main() -> int:
    parser = argparse.ArgumentParser(description="Load extension discovery outputs into DuckDB")
    parser.add_argument(
        "--db",
        default="data/extensions.duckdb",
        help="DuckDB database path (default: data/extensions.duckdb)",
    )
    parser.add_argument(
        "--validated-json",
        default="data/discovery/validated_extension_candidates_release_load_2026-03-01.json",
        help="Validated candidates JSON (output of scripts/validate_extension_candidates.py)",
    )
    parser.add_argument(
        "--promoted-json",
        default="data/discovery/promoted_candidates_2026-03-01.json",
        help="Promoted candidates JSON (output of scripts/promote_extension_candidates.py)",
    )
    parser.add_argument(
        "--no-promoted",
        action="store_true",
        help="Do not load promoted candidates",
    )
    parser.add_argument(
        "--notes",
        default=None,
        help="Optional notes for this run (stored in extension_discovery_runs)",
    )

    args = parser.parse_args()

    inputs = Inputs(
        validated_json=Path(args.validated_json),
        promoted_json=None if args.no_promoted else Path(args.promoted_json),
    )

    con = duckdb.connect(args.db)
    ensure_schema(con)

    run_id = insert_run(con, args.notes)

    validated = load_json_array(inputs.validated_json)

    validated_rows: list[tuple] = []
    for r in validated:
        repo = r.get("repo") or ""
        validated_rows.append(
            (
                run_id,
                repo,
                f"https://github.com/{repo}" if repo else None,
                r.get("score") if isinstance(r.get("score"), int) else 0,
                r.get("stars") if isinstance(r.get("stars"), int) else 0,
                r.get("pushed"),
                r.get("archived"),
                r.get("topics") if isinstance(r.get("topics"), list) else [],
                json.dumps(r.get("signals") or {}),
                r.get("release_asset_count") or 0,
                r.get("release_asset_name"),
                r.get("release_asset_url"),
                bool(r.get("release_load_ok")),
                r.get("release_load_error"),
                r.get("error"),
            )
        )

    con.executemany(
        """
        INSERT INTO extension_discovery_validated (
            run_id,
            repo,
            url,
            score,
            stars,
            pushed,
            archived,
            topics,
            signals,
            release_asset_count,
            release_asset_name,
            release_asset_url,
            release_load_ok,
            release_load_error,
            error
        ) VALUES (?, ?, ?, ?, ?, TRY_CAST(? AS TIMESTAMP), ?, ?, TRY_CAST(? AS JSON), ?, ?, ?, ?, ?, ?)
        """,
        validated_rows,
    )

    if inputs.promoted_json is not None:
        promoted = load_json_array(inputs.promoted_json)
        promoted_rows: list[tuple] = []
        for r in promoted:
            repo = r.get("repo") or ""
            promoted_rows.append(
                (
                    run_id,
                    repo,
                    f"https://github.com/{repo}" if repo else None,
                    r.get("score") if isinstance(r.get("score"), int) else 0,
                    r.get("stars") if isinstance(r.get("stars"), int) else 0,
                    r.get("pushed"),
                    r.get("release_asset_count") or 0,
                    r.get("release_asset_name"),
                    bool(r.get("release_load_ok")),
                    r.get("reason"),
                )
            )

        con.executemany(
            """
            INSERT INTO extension_discovery_promoted (
                run_id,
                repo,
                url,
                score,
                stars,
                pushed,
                release_asset_count,
                release_asset_name,
                release_load_ok,
                reason
            ) VALUES (?, ?, ?, ?, ?, TRY_CAST(? AS TIMESTAMP), ?, ?, ?, ?)
            """,
            promoted_rows,
        )

    print("Loaded discovery outputs into DuckDB")
    print(f"- db: {args.db}")
    print(f"- run_id: {run_id}")
    print(f"- validated rows: {len(validated_rows)}")
    if inputs.promoted_json is not None:
        print(f"- promoted rows: {len(promoted_rows)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
