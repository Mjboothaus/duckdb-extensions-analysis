#!/usr/bin/env python3
"""
Backfill Trend Data from Git History

This script extracts historical extension data from git commits and populates
the trend tables (extension_metrics_daily and extension_trends_summary) with
historical data from all daily analysis runs.
"""

import re
import subprocess
import duckdb
from pathlib import Path
from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_daily_analysis_commits() -> List[Tuple[str, str]]:
    """Get all commits that modified reports/latest.md, one per date."""
    cmd = [
        'git', 'log', 'origin/main', '--format=%H %ad', 
        '--date=short', '--', 'reports/latest.md'
    ]
    result = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True, 
        cwd=Path(__file__).parent.parent
    )
    
    commits = []
    seen_dates = set()
    
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
        parts = line.split(' ', 1)
        if len(parts) >= 2:
            commit_hash, date = parts[0], parts[1]
            # Only keep one commit per date (the first/latest one)
            if date not in seen_dates:
                commits.append((commit_hash, date))
                seen_dates.add(date)
    
    # Sort by date ascending (oldest first)
    commits.sort(key=lambda x: x[1])
    return commits


def extract_report_at_commit(commit_hash: str) -> str:
    """Extract the latest.md report content at a specific commit."""
    cmd = ['git', 'show', f'{commit_hash}:reports/latest.md']
    result = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True, 
        cwd=Path(__file__).parent.parent
    )
    
    if result.returncode != 0:
        logger.warning(f"Failed to extract report at {commit_hash}")
        return ""
    
    return result.stdout


def parse_report_summary(report_content: str, analysis_date: str) -> Dict:
    """Parse key metrics from report content."""
    data = {
        'analysis_date': analysis_date,
        'total_extensions': 0,
        'core_count': 0,
        'community_count': 0,
        'active_30d': 0,
        'active_7d': 0,
        'total_stars': 0,
        'archived_count': 0,
    }
    
    # Extract total extensions
    patterns = [
        r'\*\*Total Extensions\*\*:\s*(\d+)',
        r'Total Extensions.*?:\s*(\d+)',
        r'total.*?extensions.*?:?\s*(\d+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, report_content, re.IGNORECASE)
        if match:
            data['total_extensions'] = int(match.group(1))
            break
    
    # Extract core count - table format and text format
    patterns = [
        r'\|\s*\*\*Core Extensions\*\*\s*\|\s*(\d+)\s*\|',  # Table format
        r'\*\*Core Extensions\*\*:\s*(\d+)',
        r'Core Extensions.*?:\s*(\d+)',
        r'(\d+)\s+core\s+extensions',
    ]
    for pattern in patterns:
        match = re.search(pattern, report_content, re.IGNORECASE)
        if match:
            data['core_count'] = int(match.group(1))
            break
    
    # Extract community count - table format and text format
    patterns = [
        r'\|\s*\*\*Community Extensions\*\*\s*\|\s*(\d+)\s*\|',  # Table format
        r'\*\*Community Extensions\*\*:\s*(\d+)',
        r'Community Extensions.*?:\s*(\d+)',
        r'(\d+)\s+community\s+extensions',
    ]
    for pattern in patterns:
        match = re.search(pattern, report_content, re.IGNORECASE)
        if match:
            data['community_count'] = int(match.group(1))
            break
    
    # Extract active counts - try multiple patterns
    patterns_30d = [
        r'\|\s*\*\*Recently Active\*\*.*?\|\s*(\d+)\s*\|',  # Table format
        r'(\d+)\s+recently active.*?\(.*?30.*?days?\)',
        r'(\d+)\s+extensions.*?recently active',
        r'Active \(≤ 30d\).*?(\d+)',
    ]
    for pattern in patterns_30d:
        match = re.search(pattern, report_content, re.IGNORECASE)
        if match:
            data['active_30d'] = int(match.group(1))
            break
    
    patterns_7d = [
        r'\|\s*\*\*Very Active\*\*.*?\|\s*(\d+)\s*\|',  # Table format
        r'(\d+)\s+very active.*?\(.*?7.*?days?\)',
        r'(\d+)\s+extensions.*?very active',
        r'Very Active \(≤ 7d\).*?(\d+)',
    ]
    for pattern in patterns_7d:
        match = re.search(pattern, report_content, re.IGNORECASE)
        if match:
            data['active_7d'] = int(match.group(1))
            break
    
    # Try to extract total stars
    patterns = [
        r'\*\*Total Stars\*\*:\s*([\d,]+)',
        r'Total Stars.*?:\s*([\d,]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, report_content, re.IGNORECASE)
        if match:
            data['total_stars'] = int(match.group(1).replace(',', ''))
            break
    
    return data


def backfill_trends_summary(conn: duckdb.DuckDBPyConnection, historical_data: List[Dict]) -> None:
    """Backfill the extension_trends_summary table."""
    logger.info(f"Backfilling {len(historical_data)} trend summaries")
    
    for data in historical_data:
        try:
            conn.execute("""
                INSERT OR REPLACE INTO extension_trends_summary (
                    analysis_date,
                    total_extensions,
                    core_count,
                    community_count,
                    active_30d,
                    active_7d,
                    new_extensions_since_last,
                    removed_extensions_since_last,
                    avg_days_since_update,
                    total_stars,
                    total_forks,
                    archived_count
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [
                data['analysis_date'],
                data['total_extensions'],
                data['core_count'],
                data['community_count'],
                data['active_30d'],
                data['active_7d'],
                [],  # new_extensions_since_last
                [],  # removed_extensions_since_last
                None,  # avg_days_since_update
                data['total_stars'] if data['total_stars'] > 0 else None,
                None,  # total_forks
                data['archived_count']
            ])
            logger.debug(
                f"✓ {data['analysis_date']}: "
                f"Total={data['total_extensions']}, "
                f"Core={data['core_count']}, "
                f"Community={data['community_count']}, "
                f"Active(30d)={data['active_30d']}"
            )
        except Exception as e:
            logger.error(f"Failed to backfill {data['analysis_date']}: {e}")


def main():
    """Main backfill process."""
    logger.info("🔄 Starting historical trend data backfill from git history")
    
    # Get all commits that modified reports
    commits = get_daily_analysis_commits()
    
    if not commits:
        logger.warning("No report commits found")
        return
    
    logger.info(
        f"Found {len(commits)} report commits from {commits[0][1]} to {commits[-1][1]}"
    )
    
    # Extract and parse historical data
    historical_data = []
    for i, (commit_hash, date) in enumerate(commits, 1):
        logger.info(f"Processing {i}/{len(commits)}: {date} ({commit_hash[:7]})")
        report_content = extract_report_at_commit(commit_hash)
        
        if not report_content:
            logger.warning(f"Skipping {date} - no report content")
            continue
        
        data = parse_report_summary(report_content, date)
        
        if data['total_extensions'] > 0:
            historical_data.append(data)
        else:
            logger.warning(f"Skipping {date} - no valid data extracted")
    
    if not historical_data:
        logger.warning("No historical data extracted")
        return
    
    logger.info(f"\n📈 Successfully extracted {len(historical_data)} historical data points")
    
    # Connect to database and backfill
    db_path = Path(__file__).parent.parent / "data" / "extensions.duckdb"
    if not db_path.exists():
        logger.error(f"Database not found: {db_path}")
        logger.info("Please run 'just database' first to create the database")
        return
    
    conn = duckdb.connect(str(db_path))
    try:
        backfill_trends_summary(conn, historical_data)
        logger.info("\n✅ Historical trend data backfill completed!")
        
        # Show summary
        result = conn.execute("""
            SELECT 
                COUNT(*) as total_records,
                MIN(analysis_date) as earliest_date,
                MAX(analysis_date) as latest_date
            FROM extension_trends_summary
        """).fetchone()
        
        logger.info(f"\n📊 Trend summary now contains {result[0]} records")
        logger.info(f"   Date range: {result[1]} to {result[2]}")
        
        # Show growth trend summary
        logger.info(f"\n📈 Ecosystem growth trend:")
        growth = conn.execute("""
            SELECT 
                analysis_date,
                total_extensions,
                community_count,
                active_30d
            FROM extension_trends_summary
            ORDER BY analysis_date
            LIMIT 5
        """).fetchall()
        
        logger.info("   First 5 entries:")
        for row in growth:
            logger.info(
                f"   {row[0]}: {row[1]} total "
                f"({row[2]} community, {row[3]} active)"
            )
        
        # Show latest entries
        growth = conn.execute("""
            SELECT 
                analysis_date,
                total_extensions,
                community_count,
                active_30d
            FROM extension_trends_summary
            ORDER BY analysis_date DESC
            LIMIT 5
        """).fetchall()
        
        logger.info("   Latest 5 entries:")
        for row in growth:
            logger.info(
                f"   {row[0]}: {row[1]} total "
                f"({row[2]} community, {row[3]} active)"
            )
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
