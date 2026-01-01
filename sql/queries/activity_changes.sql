-- Get extensions that changed activity status recently
-- Parameter: {days} - number of days to look back
SELECT 
    extension_name,
    extension_type,
    analysis_date,
    activity_change,
    is_active,
    days_since_update
FROM v_extension_activity_trends
WHERE activity_change != 'no_change'
    AND analysis_date >= CURRENT_DATE - INTERVAL '{days} days'
ORDER BY analysis_date DESC;
