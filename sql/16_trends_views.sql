-- Views for trend analysis

-- View: Extension star trends over time
CREATE OR REPLACE VIEW v_extension_star_trends AS
SELECT 
    extension_name,
    extension_type,
    analysis_date,
    stars,
    LAG(stars) OVER (PARTITION BY extension_name ORDER BY analysis_date) as prev_stars,
    stars - LAG(stars) OVER (PARTITION BY extension_name ORDER BY analysis_date) as star_delta
FROM extension_metrics_daily
WHERE stars IS NOT NULL
ORDER BY extension_name, analysis_date;

-- View: Extension activity trends
CREATE OR REPLACE VIEW v_extension_activity_trends AS
SELECT 
    extension_name,
    extension_type,
    analysis_date,
    days_since_update,
    is_active,
    LAG(is_active) OVER (PARTITION BY extension_name ORDER BY analysis_date) as prev_active,
    CASE 
        WHEN is_active AND NOT LAG(is_active, 1, FALSE) OVER (PARTITION BY extension_name ORDER BY analysis_date) 
            THEN 'became_active'
        WHEN NOT is_active AND LAG(is_active, 1, TRUE) OVER (PARTITION BY extension_name ORDER BY analysis_date) 
            THEN 'became_inactive'
        ELSE 'no_change'
    END as activity_change
FROM extension_metrics_daily
ORDER BY extension_name, analysis_date;

-- View: Ecosystem growth metrics
CREATE OR REPLACE VIEW v_ecosystem_growth AS
SELECT 
    analysis_date,
    total_extensions,
    core_count,
    community_count,
    active_30d,
    active_7d,
    LAG(total_extensions) OVER (ORDER BY analysis_date) as prev_total,
    total_extensions - LAG(total_extensions) OVER (ORDER BY analysis_date) as total_delta,
    LAG(community_count) OVER (ORDER BY analysis_date) as prev_community,
    community_count - LAG(community_count) OVER (ORDER BY analysis_date) as community_delta,
    LAG(active_30d) OVER (ORDER BY analysis_date) as prev_active_30d,
    active_30d - LAG(active_30d) OVER (ORDER BY analysis_date) as active_30d_delta,
    avg_days_since_update,
    ROUND(CAST(active_30d AS FLOAT) / NULLIF(total_extensions, 0) * 100, 1) as active_percentage
FROM extension_trends_summary
ORDER BY analysis_date;

-- View: Recent extension additions (last 30 days)
CREATE OR REPLACE VIEW v_recent_extensions AS
WITH first_appearances AS (
    SELECT 
        extension_name,
        extension_type,
        MIN(analysis_date) as first_seen
    FROM extension_metrics_daily
    GROUP BY extension_name, extension_type
)
SELECT 
    fa.extension_name,
    fa.extension_type,
    fa.first_seen,
    emd.stars,
    emd.repository,
    emd.status
FROM first_appearances fa
JOIN extension_metrics_daily emd 
    ON fa.extension_name = emd.extension_name 
    AND fa.extension_type = emd.extension_type
    AND fa.first_seen = emd.analysis_date
WHERE fa.first_seen >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY fa.first_seen DESC;

-- View: Extension popularity rankings
CREATE OR REPLACE VIEW v_extension_popularity AS
WITH latest_date AS (
    SELECT MAX(analysis_date) as max_date
    FROM extension_metrics_daily
)
SELECT 
    emd.extension_name,
    emd.extension_type,
    emd.stars,
    emd.forks,
    emd.is_active,
    emd.days_since_update,
    ROW_NUMBER() OVER (PARTITION BY emd.extension_type ORDER BY emd.stars DESC NULLS LAST) as popularity_rank
FROM extension_metrics_daily emd
CROSS JOIN latest_date ld
WHERE emd.analysis_date = ld.max_date
    AND emd.extension_type = 'community'  -- Only rank community extensions (core don't have separate repos)
ORDER BY emd.stars DESC NULLS LAST;
