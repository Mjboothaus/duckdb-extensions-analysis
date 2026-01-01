-- Create extension trends summary table for daily aggregate metrics
CREATE TABLE IF NOT EXISTS extension_trends_summary (
    analysis_date DATE PRIMARY KEY,
    total_extensions INTEGER,
    core_count INTEGER,
    community_count INTEGER,
    active_30d INTEGER,
    active_7d INTEGER,
    new_extensions_since_last VARCHAR[],
    removed_extensions_since_last VARCHAR[],
    avg_days_since_update FLOAT,
    total_stars INTEGER,
    total_forks INTEGER,
    archived_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
