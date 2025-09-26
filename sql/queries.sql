-- Common queries for DuckDB Extensions Analysis

-- Query: Analysis runs history
-- Shows the history of analysis runs with metadata
SELECT 
    run_timestamp, 
    duckdb_version,
    script_version,
    total_core_extensions,
    total_community_extensions,
    featured_extensions_count,
    notes
FROM analysis_runs 
ORDER BY run_timestamp DESC;

-- Query: Featured community extensions
-- Shows currently featured extensions ordered by popularity
SELECT name, stars, last_push_days, description
FROM community_extensions 
WHERE featured = true
ORDER BY stars DESC NULLS LAST, last_push_days ASC;

-- Query: Extensions with improved descriptions
-- Shows extensions where we enhanced the description
SELECT name, description, improved_description
FROM community_extensions 
WHERE improved_description IS NOT NULL 
AND (description IS NULL OR description = '' OR description = 'No description')
ORDER BY name;

-- Query: Extension activity summary
-- Categorises extensions by activity level
SELECT 
    CASE 
        WHEN last_push_days <= 7 THEN 'Very Active (≤ 7d)'
        WHEN last_push_days <= 30 THEN 'Active (≤ 30d)'
        WHEN last_push_days <= 90 THEN 'Moderate (≤ 90d)'
        WHEN last_push_days <= 365 THEN 'Low (≤ 1y)'
        ELSE 'Inactive (>1y)'
    END AS activity_level,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percentage
FROM community_extensions 
WHERE last_push_days IS NOT NULL
GROUP BY activity_level
ORDER BY MIN(last_push_days);

-- Query: DuckDB version correlation (requires historical data)
-- Shows extension counts per DuckDB version
SELECT 
    duckdb_version,
    COUNT(DISTINCT name) as total_extensions,
    SUM(CASE WHEN featured THEN 1 ELSE 0 END) as featured_count,
    MIN(analysis_date) as first_analysis,
    MAX(analysis_date) as last_analysis
FROM community_extensions_history
GROUP BY duckdb_version
ORDER BY first_analysis DESC;

-- Query: Most popular extensions
-- Top extensions by GitHub stars
SELECT name, repository, stars, last_push_days, description
FROM community_extensions
WHERE stars > 0
ORDER BY stars DESC, last_push_days ASC
LIMIT 20;

-- Query: Recently active extensions
-- Extensions with recent activity
SELECT name, repository, last_push_days, stars 
FROM community_extensions 
WHERE last_push_days < 30 AND stars > 10
ORDER BY stars DESC;

-- Query: Potentially abandoned extensions
-- Extensions that haven't been updated in a long time
SELECT name, repository, last_push_days 
FROM community_extensions 
WHERE last_push_days > 365
ORDER BY last_push_days DESC;

-- Query: Extensions by programming language
-- Count of extensions by primary language
SELECT 
    COALESCE(language, 'Unknown') as language,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percentage
FROM community_extensions
GROUP BY language
ORDER BY count DESC;

-- Query: Extension ecosystem health metrics
-- Overall health statistics
SELECT 
    COUNT(*) as total_extensions,
    COUNT(CASE WHEN featured THEN 1 END) as featured_extensions,
    COUNT(CASE WHEN stars > 100 THEN 1 END) as popular_extensions,
    COUNT(CASE WHEN last_push_days <= 30 THEN 1 END) as recently_active,
    COUNT(CASE WHEN last_push_days > 365 THEN 1 END) as potentially_abandoned,
    AVG(stars) as avg_stars,
    AVG(last_push_days) as avg_days_since_update
FROM community_extensions
WHERE repository IS NOT NULL;