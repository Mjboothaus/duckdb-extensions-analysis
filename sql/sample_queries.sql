-- Sample Queries for DuckDB Extension Analysis
-- Run after creating the views in extension_views.sql

-- 1. Ecosystem Overview
SELECT 
    extension_type,
    total_extensions,
    very_active_7d,
    active_30d,
    popular_extensions,
    ROUND(avg_stars, 1) as avg_stars
FROM extensions.activity_analysis;

-- 2. Top 10 Most Popular Extensions (by stars)
SELECT 
    name,
    extension_type,
    stars,
    primary_language,
    is_featured,
    LEFT(description, 80) || '...' as description_preview
FROM extensions.popular_extensions
LIMIT 10;

-- 3. Featured vs Non-Featured Community Extensions
SELECT 
    is_featured,
    COUNT(*) as extension_count,
    AVG(stars) as avg_stars,
    COUNT(*) FILTER (WHERE last_activity <= '7 days') as very_active,
    COUNT(*) FILTER (WHERE last_activity <= '30 days') as active_30d
FROM extensions.community_extensions
GROUP BY is_featured;

-- 4. Language Distribution Across Extension Types
SELECT 
    primary_language,
    COUNT(*) FILTER (WHERE extension_type = 'core') as core_count,
    COUNT(*) FILTER (WHERE extension_type = 'community') as community_count,
    COUNT(*) as total_count,
    ROUND(AVG(stars), 1) as avg_stars
FROM extensions.all_extensions
GROUP BY primary_language
ORDER BY total_count DESC;

-- 5. Maintenance Health Distribution
SELECT 
    health_status,
    COUNT(*) as extension_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percentage
FROM extensions.maintenance_health
GROUP BY health_status
ORDER BY 
    CASE health_status
        WHEN '🟢 Very Active' THEN 1
        WHEN '🟡 Active' THEN 2
        WHEN '🟠 Moderate' THEN 3
        ELSE 4
    END;

-- 6. Extensions by Activity Level (detailed breakdown)
WITH activity_buckets AS (
    SELECT 
        name,
        extension_type,
        stars,
        last_activity,
        CASE 
            WHEN last_activity = 'today' THEN 'Today'
            WHEN last_activity LIKE '%day%' AND last_activity::INT <= 7 THEN '≤ 7 days'
            WHEN last_activity LIKE '%day%' AND last_activity::INT <= 30 THEN '8-30 days'
            WHEN last_activity LIKE '%day%' AND last_activity::INT <= 90 THEN '31-90 days'
            ELSE '> 90 days'
        END as activity_bucket
    FROM extensions.all_extensions
)
SELECT 
    activity_bucket,
    COUNT(*) as extension_count,
    COUNT(*) FILTER (WHERE extension_type = 'core') as core_count,
    COUNT(*) FILTER (WHERE extension_type = 'community') as community_count,
    AVG(stars) as avg_stars
FROM activity_buckets
GROUP BY activity_bucket
ORDER BY 
    CASE activity_bucket
        WHEN 'Today' THEN 1
        WHEN '≤ 7 days' THEN 2
        WHEN '8-30 days' THEN 3
        WHEN '31-90 days' THEN 4
        ELSE 5
    END;

-- 7. Find Extensions Similar to a Specific One (e.g., spatial extensions)
SELECT 
    name,
    extension_type,
    stars,
    description,
    repository_url
FROM extensions.all_extensions
WHERE LOWER(description) LIKE '%spatial%' 
   OR LOWER(description) LIKE '%geo%'
   OR LOWER(name) LIKE '%spatial%'
   OR LOWER(name) LIKE '%geo%'
ORDER BY stars DESC;

-- 8. Identify Potential Duplicates or Similar Extensions
WITH extension_keywords AS (
    SELECT 
        name,
        extension_type,
        stars,
        description,
        CASE 
            WHEN LOWER(description) LIKE '%http%' OR LOWER(name) LIKE '%http%' THEN 'HTTP/Web'
            WHEN LOWER(description) LIKE '%spatial%' OR LOWER(description) LIKE '%geo%' THEN 'Geospatial'
            WHEN LOWER(description) LIKE '%ml%' OR LOWER(description) LIKE '%machine learn%' THEN 'Machine Learning'
            WHEN LOWER(description) LIKE '%cloud%' OR LOWER(description) LIKE '%aws%' OR LOWER(description) LIKE '%azure%' THEN 'Cloud'
            WHEN LOWER(description) LIKE '%database%' OR LOWER(description) LIKE '%sql%' THEN 'Database'
            WHEN LOWER(description) LIKE '%file%' OR LOWER(description) LIKE '%format%' THEN 'File Format'
            ELSE 'Other'
        END as category
    FROM extensions.all_extensions
)
SELECT 
    category,
    COUNT(*) as extension_count,
    STRING_AGG(name ORDER BY stars DESC) as extensions
FROM extension_keywords
WHERE category != 'Other'
GROUP BY category
ORDER BY extension_count DESC;

-- 9. Extensions That Need Attention (stale but popular)
SELECT 
    name,
    extension_type,
    stars,
    last_activity,
    description,
    repository_url
FROM extensions.all_extensions
WHERE stars > 20  -- Popular
  AND (
    last_activity LIKE '%month%' 
    OR last_activity LIKE '%year%'
    OR (last_activity LIKE '%day%' AND last_activity::INT > 90)
  )
ORDER BY stars DESC;

-- 10. Extension Ecosystem Growth Analysis (requires historical data)
-- This would work once you have time-series data
/*
WITH monthly_stats AS (
    SELECT 
        DATE_TRUNC('month', analysis_date) as month,
        COUNT(*) as total_extensions,
        COUNT(*) FILTER (WHERE extension_type = 'community') as community_extensions
    FROM historical_extensions_data 
    GROUP BY DATE_TRUNC('month', analysis_date)
)
SELECT 
    month,
    total_extensions,
    community_extensions,
    total_extensions - LAG(total_extensions) OVER (ORDER BY month) as monthly_growth
FROM monthly_stats
ORDER BY month;
*/