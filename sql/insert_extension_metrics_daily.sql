-- Insert or update extension metrics daily
INSERT OR REPLACE INTO extension_metrics_daily (
    extension_name,
    extension_type,
    analysis_date,
    stars,
    forks,
    days_since_update,
    status,
    is_active,
    is_archived,
    repository
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
