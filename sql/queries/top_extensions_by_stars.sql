-- Get top community extensions by stars
-- Parameter: {limit} - maximum number of results
SELECT 
    extension_name,
    extension_type,
    stars,
    forks,
    is_active,
    days_since_update,
    popularity_rank
FROM v_extension_popularity
WHERE extension_type = 'community'
ORDER BY popularity_rank
LIMIT {limit};
