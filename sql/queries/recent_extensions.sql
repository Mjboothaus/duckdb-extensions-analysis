-- Get extensions first seen in the last N days
-- Parameter: {days} - number of days to look back
SELECT 
    extension_name,
    extension_type,
    first_seen,
    stars,
    repository,
    status
FROM v_recent_extensions
WHERE first_seen >= CURRENT_DATE - INTERVAL '{days} days'
ORDER BY first_seen DESC;
