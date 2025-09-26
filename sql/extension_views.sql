-- DuckDB Views for Extension Analysis
-- This file creates reusable views that match the reporting structure

-- Create the extensions database if it doesn't exist
CREATE SCHEMA IF NOT EXISTS extensions;

-- Core Extensions View
CREATE OR REPLACE VIEW extensions.core_extensions AS
SELECT 
    ROW_NUMBER() OVER (ORDER BY name) as extension_id,
    name,
    repository_name,
    repository_url,
    documentation_url,
    status,
    last_activity,
    stars,
    primary_language,
    description,
    'core' as extension_type
FROM read_json('data/core_extensions.json');

-- Community Extensions View (consolidated)
CREATE OR REPLACE VIEW extensions.community_extensions AS
SELECT 
    ROW_NUMBER() OVER (ORDER BY name) as extension_id,
    name,
    repository_name, 
    repository_url,
    documentation_url,
    status,
    last_activity,
    stars,
    primary_language,
    description,
    CASE 
        WHEN name IN (
            'airport', 'gsheets', 'prql', 'flock', 'quack', 'bigquery', 
            'cache_httpfs', 'psql', 'shellfs', 'lindel', 'open_prompt',
            'h3', 'duckpgq', 'scrooge', 'substrait', 'httpserver', 
            'geography', 'nanoarrow', 'nanodbc', 'pbix', 'rusty_quack',
            'chsql', 'cronjob', 'http_client', 'faiss', 'datasketches',
            'crypto', 'evalexpr_rhai', 'fuzzycomplete', 'hashfuncs',
            'marisa', 'netquack', 'parser_tools', 'pcap_reader', 
            'pyroscope', 'quickjs', 'radio', 'rapidfuzz', 'redis',
            'splink_udfs', 'tributary', 'tsid', 'vortex', 'webmacro',
            'wireduck'
        ) THEN true 
        ELSE false 
    END as is_featured,
    'community' as extension_type
FROM read_json('data/community_extensions.json');

-- All Extensions View (unified)
CREATE OR REPLACE VIEW extensions.all_extensions AS
SELECT 
    extension_id,
    name,
    repository_name,
    repository_url, 
    documentation_url,
    status,
    last_activity,
    stars,
    primary_language,
    description,
    extension_type,
    false as is_featured  -- Core extensions aren't "featured"
FROM extensions.core_extensions
UNION ALL
SELECT 
    extension_id + 100 as extension_id,  -- Offset to avoid ID conflicts
    name,
    repository_name,
    repository_url,
    documentation_url, 
    status,
    last_activity,
    stars,
    primary_language,
    description,
    extension_type,
    is_featured
FROM extensions.community_extensions;

-- Activity Analysis View
CREATE OR REPLACE VIEW extensions.activity_analysis AS
SELECT 
    extension_type,
    COUNT(*) as total_extensions,
    SUM(CASE WHEN last_activity <= '7 days' THEN 1 ELSE 0 END) as very_active_7d,
    SUM(CASE WHEN last_activity <= '30 days' THEN 1 ELSE 0 END) as active_30d,
    SUM(CASE WHEN stars > 50 THEN 1 ELSE 0 END) as popular_extensions,
    AVG(stars) as avg_stars
FROM extensions.all_extensions
GROUP BY extension_type;

-- Featured Extensions Summary  
CREATE OR REPLACE VIEW extensions.featured_extensions AS
SELECT 
    name,
    repository_url,
    stars,
    primary_language,
    description,
    last_activity
FROM extensions.all_extensions 
WHERE is_featured = true
ORDER BY stars DESC;

-- Language Analysis
CREATE OR REPLACE VIEW extensions.language_analysis AS
SELECT 
    primary_language,
    extension_type,
    COUNT(*) as extension_count,
    AVG(stars) as avg_stars,
    STRING_AGG(name, ', ' ORDER BY stars DESC LIMIT 5) as top_extensions
FROM extensions.all_extensions
GROUP BY primary_language, extension_type
ORDER BY extension_count DESC;

-- Popular Extensions (by stars)
CREATE OR REPLACE VIEW extensions.popular_extensions AS
SELECT 
    name,
    extension_type,
    stars,
    primary_language,
    description,
    repository_url,
    is_featured
FROM extensions.all_extensions
WHERE stars > 10  -- Arbitrary threshold for "popular"
ORDER BY stars DESC;

-- Maintenance Health View
CREATE OR REPLACE VIEW extensions.maintenance_health AS
SELECT 
    name,
    extension_type,
    last_activity,
    stars,
    CASE 
        WHEN last_activity <= '7 days' THEN '🟢 Very Active'
        WHEN last_activity <= '30 days' THEN '🟡 Active' 
        WHEN last_activity <= '90 days' THEN '🟠 Moderate'
        ELSE '🔴 Stale'
    END as health_status,
    repository_url
FROM extensions.all_extensions
ORDER BY 
    CASE 
        WHEN last_activity <= '7 days' THEN 1
        WHEN last_activity <= '30 days' THEN 2
        WHEN last_activity <= '90 days' THEN 3
        ELSE 4
    END,
    stars DESC;