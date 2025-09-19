-- Create views for extension availability analysis

-- View for current extension availability across all platforms
CREATE OR REPLACE VIEW current_extension_availability AS
SELECT DISTINCT ON (extension_name, platform, duckdb_version)
    extension_name,
    extension_type,
    platform,
    duckdb_version,
    is_available,
    availability_date,
    check_timestamp,
    http_status_code,
    file_size_bytes,
    error_message,
    days_since_release
FROM extension_availability_history
ORDER BY extension_name, platform, duckdb_version, check_timestamp DESC;

-- View for extension availability lag analysis
CREATE OR REPLACE VIEW extension_availability_lag AS
SELECT 
    h.extension_name,
    h.extension_type,
    h.duckdb_version,
    r.published_date as release_date,
    h.platform,
    h.availability_date,
    EXTRACT(DAY FROM (h.availability_date - r.published_date)) as lag_days,
    h.is_available
FROM extension_availability_history h
LEFT JOIN duckdb_releases r ON h.duckdb_version = r.version
WHERE h.availability_date IS NOT NULL
ORDER BY h.extension_name, h.duckdb_version, h.platform;

-- View for platform availability summary by extension and version
CREATE OR REPLACE VIEW extension_platform_summary AS
SELECT 
    extension_name,
    extension_type,
    duckdb_version,
    COUNT(CASE WHEN is_available THEN 1 END) as available_platforms_count,
    COUNT(*) as total_platforms_checked,
    ROUND(
        100.0 * COUNT(CASE WHEN is_available THEN 1 END) / COUNT(*), 
        2
    ) as availability_percentage,
    STRING_AGG(CASE WHEN is_available THEN platform END, ', ') as available_platforms,
    STRING_AGG(CASE WHEN NOT is_available THEN platform END, ', ') as unavailable_platforms,
    MIN(CASE WHEN is_available THEN availability_date END) as earliest_availability,
    MAX(CASE WHEN is_available THEN availability_date END) as latest_availability
FROM current_extension_availability
GROUP BY extension_name, extension_type, duckdb_version
ORDER BY extension_name, duckdb_version;

-- View for problematic extensions (those with platform-specific issues)
CREATE OR REPLACE VIEW problematic_extensions AS
SELECT 
    s.extension_name,
    s.extension_type,
    s.duckdb_version,
    s.availability_percentage,
    s.unavailable_platforms,
    STRING_AGG(DISTINCT c.error_message, ';') as error_summary
FROM extension_platform_summary s
LEFT JOIN current_extension_availability c ON (
    s.extension_name = c.extension_name AND 
    s.duckdb_version = c.duckdb_version AND
    NOT c.is_available
)
WHERE s.availability_percentage < 100
GROUP BY s.extension_name, s.extension_type, s.duckdb_version, s.availability_percentage, s.unavailable_platforms
ORDER BY s.availability_percentage ASC, s.extension_name;
