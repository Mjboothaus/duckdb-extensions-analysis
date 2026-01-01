-- Get extensions with highest star growth in recent period
-- Parameter: {limit} - maximum number of results
WITH latest_trends AS (
    SELECT 
        extension_name,
        extension_type,
        star_delta,
        stars,
        analysis_date
    FROM v_extension_star_trends
    WHERE star_delta IS NOT NULL
        AND analysis_date >= CURRENT_DATE - INTERVAL '7 days'
    ORDER BY star_delta DESC
    LIMIT {limit}
)
SELECT * FROM latest_trends
ORDER BY star_delta DESC;
