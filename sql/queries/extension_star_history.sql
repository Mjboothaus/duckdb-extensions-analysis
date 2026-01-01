-- Get star growth history for a specific extension
-- Parameter: {extension_name} - name of the extension
SELECT 
    analysis_date,
    stars,
    prev_stars,
    star_delta
FROM v_extension_star_trends
WHERE extension_name = '{extension_name}'
ORDER BY analysis_date DESC;
