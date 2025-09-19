-- Views for installation test analysis

-- View for current installation test results (latest tests only)
CREATE OR REPLACE VIEW current_installation_tests AS
SELECT DISTINCT ON (extension_name, platform, duckdb_version)
    extension_name,
    platform,
    success,
    installation_time_seconds,
    load_time_seconds,
    error_message,
    error_type,
    duckdb_version,
    test_timestamp,
    file_size_bytes,
    extension_path,
    analysis_date
FROM installation_test_history
ORDER BY extension_name, platform, duckdb_version, test_timestamp DESC;

-- View combining availability and installation test data
CREATE OR REPLACE VIEW extension_comprehensive_status AS
SELECT 
    a.extension_name,
    a.extension_type,
    a.platform,
    a.duckdb_version,
    a.is_available as file_available,
    a.availability_date,
    a.http_status_code,
    a.file_size_bytes as availability_file_size,
    i.success as installation_successful,
    i.installation_time_seconds,
    i.load_time_seconds,
    i.error_message as installation_error,
    i.error_type as installation_error_type,
    i.test_timestamp as last_test_time,
    i.file_size_bytes as actual_file_size,
    -- Calculate overall status
    CASE 
        WHEN a.is_available = false THEN 'UNAVAILABLE'
        WHEN a.is_available = true AND i.success = true THEN 'WORKING'
        WHEN a.is_available = true AND i.success = false THEN 'BROKEN'
        WHEN a.is_available = true AND i.success IS NULL THEN 'UNTESTED'
        ELSE 'UNKNOWN'
    END as overall_status
FROM current_extension_availability a
LEFT JOIN current_installation_tests i ON (
    a.extension_name = i.extension_name AND 
    a.platform = i.platform AND
    a.duckdb_version = i.duckdb_version
)
ORDER BY a.extension_name, a.platform;

-- View for extension reliability scores
CREATE OR REPLACE VIEW extension_reliability_scores AS
SELECT 
    extension_name,
    duckdb_version,
    COUNT(*) as total_platform_tests,
    COUNT(CASE WHEN overall_status = 'WORKING' THEN 1 END) as working_platforms,
    COUNT(CASE WHEN overall_status = 'BROKEN' THEN 1 END) as broken_platforms,
    COUNT(CASE WHEN overall_status = 'UNAVAILABLE' THEN 1 END) as unavailable_platforms,
    COUNT(CASE WHEN overall_status = 'UNTESTED' THEN 1 END) as untested_platforms,
    ROUND(
        100.0 * COUNT(CASE WHEN overall_status = 'WORKING' THEN 1 END) / COUNT(*), 
        2
    ) as reliability_percentage,
    AVG(CASE WHEN installation_successful THEN installation_time_seconds END) as avg_install_time,
    AVG(CASE WHEN installation_successful THEN load_time_seconds END) as avg_load_time,
    STRING_AGG(
        CASE WHEN overall_status = 'WORKING' THEN platform END, 
        ', ' 
    ) as working_platforms_list,
    STRING_AGG(
        CASE WHEN overall_status = 'BROKEN' THEN platform END, 
        ', ' 
    ) as broken_platforms_list
FROM extension_comprehensive_status
GROUP BY extension_name, duckdb_version
ORDER BY reliability_percentage DESC, extension_name;

-- View for installation performance benchmarks
CREATE OR REPLACE VIEW installation_performance_benchmarks AS
SELECT 
    extension_name,
    COUNT(CASE WHEN success THEN 1 END) as successful_installs,
    COUNT(*) as total_install_attempts,
    AVG(CASE WHEN success THEN installation_time_seconds END) as avg_install_time,
    MIN(CASE WHEN success THEN installation_time_seconds END) as fastest_install_time,
    MAX(CASE WHEN success THEN installation_time_seconds END) as slowest_install_time,
    AVG(CASE WHEN success THEN load_time_seconds END) as avg_load_time,
    AVG(CASE WHEN success THEN file_size_bytes END) / 1024.0 / 1024.0 as avg_size_mb,
    -- Performance category
    CASE 
        WHEN AVG(CASE WHEN success THEN installation_time_seconds END) < 5 THEN 'FAST'
        WHEN AVG(CASE WHEN success THEN installation_time_seconds END) < 15 THEN 'MODERATE'
        WHEN AVG(CASE WHEN success THEN installation_time_seconds END) < 30 THEN 'SLOW'
        ELSE 'VERY_SLOW'
    END as performance_category
FROM current_installation_tests
WHERE success = true
GROUP BY extension_name
HAVING COUNT(CASE WHEN success THEN 1 END) > 0
ORDER BY avg_install_time ASC;

-- View for problematic extensions with detailed diagnostics
CREATE OR REPLACE VIEW problematic_extensions_detailed AS
SELECT 
    r.extension_name,
    r.duckdb_version,
    r.reliability_percentage,
    r.broken_platforms,
    r.unavailable_platforms,
    -- Installation issues
    COUNT(CASE WHEN s.installation_error_type = 'download' THEN 1 END) as download_errors,
    COUNT(CASE WHEN s.installation_error_type = 'install' THEN 1 END) as install_errors,
    COUNT(CASE WHEN s.installation_error_type = 'load' THEN 1 END) as load_errors,
    COUNT(CASE WHEN s.installation_error_type = 'timeout' THEN 1 END) as timeout_errors,
    -- GitHub issues correlation (if available)
    COALESCE(ei.open_issues_count, 0) as related_open_issues,
    COALESCE(ei.availability_issues, 0) as github_availability_issues,
    COALESCE(ei.installation_issues, 0) as github_installation_issues,
    -- Performance issues
    AVG(CASE WHEN s.installation_successful THEN s.installation_time_seconds END) as avg_install_time,
    -- Overall problem severity
    CASE 
        WHEN r.reliability_percentage = 0 THEN 'CRITICAL'
        WHEN r.reliability_percentage < 50 THEN 'HIGH'
        WHEN r.reliability_percentage < 80 THEN 'MEDIUM'
        ELSE 'LOW'
    END as problem_severity
FROM extension_reliability_scores r
LEFT JOIN extension_comprehensive_status s ON (
    r.extension_name = s.extension_name AND 
    r.duckdb_version = s.duckdb_version
)
LEFT JOIN extension_issues_with_availability ei ON r.extension_name = ei.extension_name
WHERE r.reliability_percentage < 100  -- Only show extensions with issues
GROUP BY 
    r.extension_name, 
    r.duckdb_version, 
    r.reliability_percentage, 
    r.broken_platforms, 
    r.unavailable_platforms,
    ei.open_issues_count,
    ei.availability_issues,
    ei.installation_issues
ORDER BY 
    CASE problem_severity 
        WHEN 'CRITICAL' THEN 1 
        WHEN 'HIGH' THEN 2 
        WHEN 'MEDIUM' THEN 3 
        ELSE 4 
    END,
    r.reliability_percentage ASC;