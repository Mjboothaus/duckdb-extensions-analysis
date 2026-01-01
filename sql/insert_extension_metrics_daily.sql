-- Insert or update extension metrics daily
INSERT INTO extension_metrics_daily (
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
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT (extension_name, extension_type, analysis_date) 
DO UPDATE SET
    stars = EXCLUDED.stars,
    forks = EXCLUDED.forks,
    days_since_update = EXCLUDED.days_since_update,
    status = EXCLUDED.status,
    is_active = EXCLUDED.is_active,
    is_archived = EXCLUDED.is_archived,
    repository = EXCLUDED.repository;
