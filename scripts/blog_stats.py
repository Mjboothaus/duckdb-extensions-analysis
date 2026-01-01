#!/usr/bin/env python3
"""
Quick statistics for blog post reference.

Run this to get key numbers for your blog post about the DuckDB ecosystem.
"""

import duckdb
from pathlib import Path
from datetime import date

db_path = Path(__file__).parent.parent / "data" / "extensions.duckdb"

if not db_path.exists():
    print("❌ Database not found. Run 'just database' first.")
    exit(1)

conn = duckdb.connect(str(db_path))

print("=" * 70)
print("DuckDB Extensions Ecosystem - Blog Post Quick Stats")
print("=" * 70)

# Date range
result = conn.execute("""
    SELECT 
        MIN(analysis_date) as first_date,
        MAX(analysis_date) as latest_date,
        COUNT(DISTINCT analysis_date) as total_snapshots
    FROM extension_trends_summary
""").fetchone()

first_date, latest_date, snapshots = result
days_tracked = (latest_date - first_date).days if latest_date and first_date else 0

print(f"\n📅 TRACKING PERIOD")
print(f"   First recorded: {first_date}")
print(f"   Latest: {latest_date}")
print(f"   Days tracked: {days_tracked}")
print(f"   Snapshots: {snapshots}")

# Growth since beginning (use latest COMPLETE data - skip today if core_count is 0)
result = conn.execute("""
    WITH first_record AS (
        SELECT * FROM extension_trends_summary 
        ORDER BY analysis_date ASC LIMIT 1
    ),
    latest_record AS (
        SELECT * FROM extension_trends_summary 
        WHERE core_count > 0  -- Skip incomplete data
        ORDER BY analysis_date DESC LIMIT 1
    )
    SELECT 
        f.analysis_date as first_date,
        f.total_extensions as first_total,
        f.core_count as first_core,
        f.community_count as first_community,
        f.active_30d as first_active,
        l.analysis_date as latest_date,
        l.total_extensions as latest_total,
        l.core_count as latest_core,
        l.community_count as latest_community,
        l.active_30d as latest_active
    FROM first_record f, latest_record l
""").fetchone()

if result:
    first_date, first_total, first_core, first_comm, first_active, latest_date, latest_total, latest_core, latest_comm, latest_active = result
    
    print(f"\n📊 ECOSYSTEM GROWTH ({first_date} to {latest_date})")
    print(f"   Total extensions:")
    print(f"      Started with: {first_total} ({first_core} core + {first_comm} community)")
    print(f"      Current: {latest_total} ({latest_core} core + {latest_comm} community)")
    print(f"      Growth: +{latest_total - first_total} ({(latest_total - first_total) / first_total * 100:.1f}%)")
    
    print(f"\n   Community extensions:")
    print(f"      Started with: {first_comm}")
    print(f"      Current: {latest_comm}")
    print(f"      Growth: +{latest_comm - first_comm}")
    
    print(f"\n   Active extensions (≤30d):")
    print(f"      Started with: {first_active}")
    print(f"      Current: {latest_active}")
    print(f"      Activity rate: {latest_active / latest_total * 100:.1f}%")

# Top extensions by stars
print(f"\n⭐ TOP 10 EXTENSIONS BY STARS")
result = conn.execute("""
    SELECT 
        emd.extension_name,
        emd.stars,
        emd.is_active,
        emd.repository,
        emd.days_since_update
    FROM extension_metrics_daily emd
    WHERE emd.analysis_date = (SELECT MAX(analysis_date) FROM extension_metrics_daily)
        AND emd.extension_type = 'community'
        AND emd.stars > 0
    ORDER BY emd.stars DESC
    LIMIT 10
""").fetchall()

for i, (name, stars, active, repo, days) in enumerate(result, 1):
    status = "active" if active else f"{days}d ago"
    # Build proper GitHub URL
    if repo and repo.startswith('http'):
        repo_link = repo
    elif repo and '/' in repo:
        repo_link = f"https://github.com/{repo}"
    else:
        repo_link = f"https://github.com/duckdb/{name}"
    print(f"   {i:2}. [{name}]({repo_link}) - {stars:,} stars ({status})")

# Recently added - use trend summary which has historical data
print(f"\n🆕 EXTENSIONS ADDED OVER TIME")
result = conn.execute("""
    SELECT 
        analysis_date,
        new_extensions_since_last,
        total_extensions
    FROM extension_trends_summary
    WHERE new_extensions_since_last IS NOT NULL 
        AND array_length(new_extensions_since_last) > 0
    ORDER BY analysis_date DESC
    LIMIT 10
""").fetchall()

if result:
    print(f"   Recent additions (last 10 snapshots with new extensions):")
    for date, new_exts, total in result:
        count = len(new_exts) if new_exts else 0
        if count > 0:
            if count <= 5:
                print(f"   {date}: +{count} ({', '.join(new_exts)}) - total: {total}")
            else:
                print(f"   {date}: +{count} ({', '.join(new_exts[:3])}...) - total: {total}")
else:
    print(f"   No new extension data available")

# Most active
print(f"\n⚡ MOST ACTIVE (Updated in last 7 days)")
result = conn.execute("""
    WITH latest_date AS (
        SELECT MAX(analysis_date) as max_date
        FROM extension_metrics_daily
    )
    SELECT 
        emd.extension_name,
        emd.days_since_update,
        emd.stars,
        emd.repository
    FROM extension_metrics_daily emd
    CROSS JOIN latest_date ld
    WHERE emd.analysis_date = ld.max_date
        AND emd.days_since_update <= 7
        AND emd.extension_type = 'community'
    ORDER BY emd.days_since_update ASC, emd.stars DESC
""").fetchall()

if result:
    print(f"   {len(result)} extensions updated in last 7 days:")
    for name, days, stars, repo in result:
        # Build proper GitHub URL
        if repo and repo.startswith('http'):
            repo_link = repo
        elif repo and '/' in repo:
            repo_link = f"https://github.com/{repo}"
        else:
            repo_link = f"https://github.com/duckdb/{name}"
        stars_str = f"{stars:,} stars" if stars else "no stars yet"
        days_str = "today" if days == 0 else f"{days}d ago"
        print(f"   - [{name}]({repo_link}) - {days_str} ({stars_str})")

# Language breakdown
print(f"\n🔧 LANGUAGE BREAKDOWN (Community)")
result = conn.execute("""
    WITH latest_metrics AS (
        SELECT DISTINCT ON (extension_name) 
            extension_name,
            repository
        FROM extension_metrics_daily
        WHERE extension_type = 'community'
        ORDER BY extension_name, analysis_date DESC
    )
    SELECT 
        CASE 
            WHEN repository LIKE '%/%.cpp' OR repository LIKE '%/%.c' THEN 'C++'
            WHEN repository LIKE '%/%.rs' THEN 'Rust'
            WHEN repository LIKE '%/%.go' THEN 'Go'
            ELSE 'Other'
        END as language,
        COUNT(*) as count
    FROM latest_metrics
    GROUP BY language
    ORDER BY count DESC
""").fetchall()

for lang, count in result:
    print(f"   {lang:<15} {count:>3} extensions")

print("\n" + "=" * 70)
print("💡 Use these stats as reference for your blog post!")
print("=" * 70)

conn.close()
