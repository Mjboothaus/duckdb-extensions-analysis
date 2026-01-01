-- Get ecosystem growth trends over time
SELECT 
    analysis_date,
    total_extensions,
    total_delta,
    community_count,
    community_delta,
    active_30d,
    active_30d_delta,
    active_percentage,
    avg_days_since_update
FROM v_ecosystem_growth
ORDER BY analysis_date DESC;
