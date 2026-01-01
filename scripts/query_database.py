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


# SQL query directory
SQL_QUERIES_DIR = Path(__file__).parent.parent / "sql" / "queries"


def load_sql_query(query_name: str, **params) -> str:
    """Load SQL query from file and substitute parameters."""
    query_file = SQL_QUERIES_DIR / f"{query_name}.sql"
    if not query_file.exists():
        raise FileNotFoundError(f"SQL query file not found: {query_file}")
    
    query = query_file.read_text()
    
    # Substitute parameters
    for key, value in params.items():
        query = query.replace(f"{{{key}}}", str(value))
    
    return query


def get_ecosystem_growth_trends(db_path: str = "data/extensions.duckdb") -> list:
    """Get ecosystem growth trends over time."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("ecosystem_growth_trends")
    result = conn.execute(query).fetchall()
    conn.close()
    return result


def get_recent_extensions(db_path: str = "data/extensions.duckdb", days: int = 30) -> list:
    """Get extensions first seen in the last N days."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("recent_extensions", days=days)
    result = conn.execute(query).fetchall()
    conn.close()
    return result


def get_trending_extensions(db_path: str = "data/extensions.duckdb", limit: int = 10) -> list:
    """Get extensions with highest star growth in recent period."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("trending_extensions", limit=limit)
    result = conn.execute(query).fetchall()
    conn.close()
    return result


def get_extension_trend_summary(db_path: str = "data/extensions.duckdb") -> dict:
    """Get latest trend summary with deltas."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("latest_trend_summary")
    result = conn.execute(query).fetchall()
    conn.close()
    
    if not result:
        return {}
    
    latest = result[0]
    previous = result[1] if len(result) > 1 else None
    
    summary = {
        'date': latest[0],
        'total_extensions': latest[1],
        'core_count': latest[2],
        'community_count': latest[3],
        'active_30d': latest[4],
        'active_7d': latest[5],
        'new_extensions': latest[6] or [],
        'removed_extensions': latest[7] or [],
        'avg_days_since_update': latest[8],
        'total_stars': latest[9],
        'total_forks': latest[10],
        'archived_count': latest[11],
    }
    
    # Calculate deltas if we have previous data
    if previous:
        summary['total_delta'] = latest[1] - previous[1]
        summary['community_delta'] = latest[3] - previous[3]
        summary['active_30d_delta'] = latest[4] - previous[4]
        summary['stars_delta'] = latest[9] - previous[9] if latest[9] and previous[9] else None
    
    return summary


def get_extension_star_history(extension_name: str, db_path: str = "data/extensions.duckdb") -> list:
    """Get star growth history for a specific extension."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("extension_star_history", extension_name=extension_name)
    result = conn.execute(query).fetchall()
    conn.close()
    return result


def get_activity_changes(db_path: str = "data/extensions.duckdb", days: int = 7) -> list:
    """Get extensions that changed activity status recently."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("activity_changes", days=days)
    result = conn.execute(query).fetchall()
    conn.close()
    return result


def get_top_extensions_by_stars(db_path: str = "data/extensions.duckdb", limit: int = 20) -> list:
    """Get top community extensions by stars."""
    conn = duckdb.connect(db_path)
    query = load_sql_query("top_extensions_by_stars", limit=limit)
    result = conn.execute(query).fetchall()
    conn.close()
    return result


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

    # 6. Show ecosystem growth trends
    print("\n📈 Ecosystem Growth Trends:")
    print("-" * 40)
    try:
        trends = get_ecosystem_growth_trends(db_path)
        if trends:
            print(f"{'Date':<12} {'Total':<7} {'Delta':<7} {'Active 30d':<12} {'Avg Days':<10}")
            print("-" * 50)
            for row in trends[:5]:  # Show last 5 analysis runs
                date = row[0]
                total = row[1]
                delta = f"+{row[2]}" if row[2] and row[2] > 0 else str(row[2]) if row[2] else "-"
                active = row[5]
                active_delta = f"(+{row[6]})" if row[6] and row[6] > 0 else f"({row[6]})" if row[6] else ""
                avg_days = f"{row[8]:.1f}" if row[8] else "N/A"
                print(f"{date} {total:<7} {delta:<7} {active:<4} {active_delta:<7} {avg_days}")
        else:
            print("No trend data available yet. Run analysis multiple times to build history.")
    except Exception as e:
        print(f"⚠️  Trend data not available: {e}")

    # 7. Show recent extensions
    print("\n🆕 Recently Added Extensions (Last 30 Days):")
    print("-" * 45)
    try:
        recent = get_recent_extensions(db_path, days=30)
        if recent:
            for row in recent[:10]:
                ext_name = row[0]
                ext_type = row[1]
                first_seen = row[2]
                stars = f"⭐{row[3]}" if row[3] else "⭐0"
                print(f"{first_seen} | {ext_type:<10} | {ext_name:<20} | {stars}")
        else:
            print("No new extensions in the last 30 days.")
    except Exception as e:
        print(f"⚠️  Recent extensions data not available: {e}")

    # 8. Show trending extensions
    print("\n🔥 Trending Extensions (Star Growth):")
    print("-" * 40)
    try:
        trending = get_trending_extensions(db_path, limit=10)
        if trending:
            for row in trending:
                ext_name = row[0]
                star_delta = row[2]
                stars = row[3]
                print(f"{ext_name:<20} | +{star_delta} stars (total: {stars})")
        else:
            print("No trending data available yet. Needs multiple analysis runs.")
    except Exception as e:
        print(f"⚠️  Trending data not available: {e}")

    # 9. Show trend summary
    print("\n📊 Latest Trend Summary:")
    print("-" * 30)
    try:
        summary = get_extension_trend_summary(db_path)
        if summary:
            print(f"Date: {summary['date']}")
            print(f"Total Extensions: {summary['total_extensions']}")
            if 'total_delta' in summary:
                delta = summary['total_delta']
                print(f"  Change: {'+' if delta > 0 else ''}{delta} from previous analysis")
            print(f"\nCommunity Extensions: {summary['community_count']}")
            if 'community_delta' in summary:
                delta = summary['community_delta']
                print(f"  Change: {'+' if delta > 0 else ''}{delta} from previous analysis")
            print(f"\nActive (30d): {summary['active_30d']}")
            if 'active_30d_delta' in summary:
                delta = summary['active_30d_delta']
                print(f"  Change: {'+' if delta > 0 else ''}{delta} from previous analysis")
            
            if summary['new_extensions']:
                print(f"\n🆕 New Extensions: {', '.join(summary['new_extensions'])}")
            if summary['removed_extensions']:
                print(f"\n🗑️  Removed: {', '.join(summary['removed_extensions'])}")
        else:
            print("No trend summary available yet.")
    except Exception as e:
        print(f"⚠️  Trend summary not available: {e}")

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
