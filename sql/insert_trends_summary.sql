-- Insert or replace extension trends summary
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
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
