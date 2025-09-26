#!/usr/bin/env python3
"""
DuckDB Extensions Database Query Examples

This script demonstrates querying the historical extension data stored in the DuckDB database.
It also provides back-filling capabilities for historical data.
"""

import duckdb
from pathlib import Path
import sys
from datetime import datetime, timedelta


def query_database(db_path: str = "data/extensions.duckdb"):
    """Run example queries on the extensions database."""
    if not Path(db_path).exists():
        print(f"❌ Database not found: {db_path}")
        print("Run 'just database' first to create the database")
        return

    conn = duckdb.connect(db_path)

    print("🔍 DuckDB Extensions Database Analysis")
    print("=" * 50)

    # 1. Show analysis runs history
    print("\n📊 Analysis Runs History:")
    print("-" * 30)
    result = conn.execute("""
        SELECT 
            run_timestamp, 
            duckdb_version,
            script_version,
            total_core_extensions,
            total_community_extensions,
            featured_extensions_count,
            notes
        FROM analysis_runs 
        ORDER BY run_timestamp DESC
    """).fetchall()

    for row in result:
        print(
            f"📅 {row[0]} | DuckDB: {row[1]} | Script: {row[2]} | Core: {row[3]} | Community: {row[4]} | Featured: {row[5]}"
        )
        if row[6]:
            print(f"   💬 {row[6]}")

    # 2. Show current featured extensions
    print("\n⭐ Featured Community Extensions:")
    print("-" * 35)
    result = conn.execute("""
        SELECT name, stars, last_push_days, description
        FROM community_extensions 
        WHERE featured = true
        ORDER BY stars DESC NULLS LAST, last_push_days ASC
        LIMIT 10
    """).fetchall()

    for row in result:
        stars = f"⭐{row[1]}" if row[1] else "⭐0"
        days = f"{row[2]}d ago" if row[2] is not None else "Unknown"
        desc = (
            row[3][:50] + "..."
            if row[3] and len(row[3]) > 50
            else (row[3] or "No description")
        )
        print(f"{row[0]:<15} | {stars:<8} | {days:<10} | {desc}")

    # 3. Show extensions with improved descriptions
    print("\n🔧 Extensions with Enhanced Descriptions:")
    print("-" * 40)
    result = conn.execute("""
        SELECT name, description, improved_description
        FROM community_extensions 
        WHERE improved_description IS NOT NULL 
        AND (description IS NULL OR description = '' OR description = 'No description')
        ORDER BY name
        LIMIT 5
    """).fetchall()

    for row in result:
        print(f"📦 {row[0]}")
        print(f"   Original: {row[1] or 'None'}")
        print(f"   Enhanced: {row[2]}")
        print()

    # 4. Show extension activity trends
    print("\n📈 Extension Activity Summary:")
    print("-" * 30)
    result = conn.execute("""
        SELECT 
            CASE 
                WHEN last_push_days <= 7 THEN 'Very Active (≤ 7d)'
                WHEN last_push_days <= 30 THEN 'Active (≤ 30d)'
                WHEN last_push_days <= 90 THEN 'Moderate (≤ 90d)'
                WHEN last_push_days <= 365 THEN 'Low (≤ 1y)'
                ELSE 'Inactive (>1y)'
            END AS activity_level,
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percentage
        FROM community_extensions 
        WHERE last_push_days IS NOT NULL
        GROUP BY activity_level
        ORDER BY MIN(last_push_days)
    """).fetchall()

    for row in result:
        bar = "█" * int(row[2] / 5)  # Scale bar to max 20 chars
        print(f"{row[0]:<20} | {row[1]:>3} extensions ({row[2]:>4}%) {bar}")

    # 5. Show DuckDB version correlation
    print("\n🦆 DuckDB Version Analysis:")
    print("-" * 25)
    result = conn.execute("""
        SELECT 
            duckdb_version,
            COUNT(DISTINCT name) as total_extensions,
            SUM(CASE WHEN featured THEN 1 ELSE 0 END) as featured_count,
            MIN(analysis_date) as first_analysis,
            MAX(analysis_date) as last_analysis
        FROM community_extensions_history
        GROUP BY duckdb_version
        ORDER BY first_analysis DESC
    """).fetchall()

    for row in result:
        print(
            f"Version {row[0]}: {row[1]} extensions ({row[2]} featured) | {row[3]} to {row[4]}"
        )

    conn.close()


def simulate_historical_backfill(db_path: str = "data/extensions.duckdb"):
    """Simulate historical data by creating entries with older dates (for demonstration)."""
    if not Path(db_path).exists():
        print(f"❌ Database not found: {db_path}")
        return

    print("🔄 Simulating Historical Data Back-fill")
    print("=" * 40)

    conn = duckdb.connect(db_path)

    # Simulate older analysis runs
    older_dates = [
        datetime.now() - timedelta(days=30),
        datetime.now() - timedelta(days=60),
        datetime.now() - timedelta(days=90),
    ]

    versions = ["v1.3.1", "v1.3.0", "v1.2.0"]

    for i, (date, version) in enumerate(zip(older_dates, versions)):
        # Simulate slightly different extension counts for historical data
        core_count = 24 - i  # Fewer core extensions in older versions
        community_count = 75 - (i * 5)  # Fewer community extensions historically
        featured_count = 20 - (i * 3)  # Fewer featured extensions historically

        conn.execute(
            """
            INSERT INTO analysis_runs 
            (run_timestamp, duckdb_version, script_version, total_core_extensions, 
             total_community_extensions, featured_extensions_count, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            [
                date,
                version,
                f"1.{2 - i}.0",
                core_count,
                community_count,
                featured_count,
                f"Historical back-fill simulation for {version}",
            ],
        )

        print(
            f"📅 Added historical run: {date.strftime('%Y-%m-%d')} | {version} | {community_count} extensions"
        )

    # Simulate historical community extension snapshots
    # Get some current extensions to create historical versions of
    current_extensions = conn.execute("""
        SELECT name, repository, featured, stars, forks, language
        FROM community_extensions 
        WHERE repository != 'N/A'
        LIMIT 10
    """).fetchall()

    for date, version in zip(older_dates, versions):
        for ext in current_extensions:
            # Simulate slightly lower stars/forks for historical data
            historical_stars = max(0, (ext[3] or 0) - 50)
            historical_forks = max(0, (ext[4] or 0) - 10)

            conn.execute(
                """
                INSERT INTO community_extensions_history 
                (name, repository, status, stars, forks, language, featured, 
                 duckdb_version, analysis_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                [
                    ext[0],
                    ext[1],
                    "✅ Ongoing",
                    historical_stars,
                    historical_forks,
                    ext[5],
                    ext[2],
                    version,
                    date,
                ],
            )

    print(
        f"✅ Historical back-fill completed! Added data for {len(older_dates)} time periods"
    )
    conn.close()


def main():
    """Main function with command line interface."""
    if len(sys.argv) > 1 and sys.argv[1] == "backfill":
        simulate_historical_backfill()
    else:
        query_database()


if __name__ == "__main__":
    main()
