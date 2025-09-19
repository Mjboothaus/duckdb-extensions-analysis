-- Create views for GitHub issues analysis

-- View for current GitHub issues (latest analysis only)
CREATE OR REPLACE VIEW current_github_issues AS
SELECT DISTINCT ON (issue_number)
    issue_number,
    title,
    body,
    state,
    created_at,
    updated_at,
    closed_at,
    labels,
    extension_names,
    platforms,
    issue_type,
    severity,
    html_url,
    analysis_date
FROM github_issues_history
ORDER BY issue_number, analysis_date DESC;

-- View combining extension issues with availability data
CREATE OR REPLACE VIEW extension_issues_with_availability AS
SELECT 
    e.extension_name,
    e.extension_type,
    e.duckdb_version,
    e.availability_percentage,
    e.unavailable_platforms,
    COUNT(CASE WHEN i.state = 'open' THEN 1 END) as open_issues_count,
    COUNT(CASE WHEN i.state = 'closed' THEN 1 END) as closed_issues_count,
    COUNT(CASE WHEN i.severity = 'high' THEN 1 END) as high_severity_issues,
    COUNT(CASE WHEN i.severity = 'medium' THEN 1 END) as medium_severity_issues,
    COUNT(CASE WHEN i.severity = 'low' THEN 1 END) as low_severity_issues,
    COUNT(CASE WHEN i.issue_type = 'availability' THEN 1 END) as availability_issues,
    COUNT(CASE WHEN i.issue_type = 'installation' THEN 1 END) as installation_issues,
    COUNT(CASE WHEN i.issue_type = 'platform' THEN 1 END) as platform_issues,
    STRING_AGG(DISTINCT i.html_url, ', ') as related_issue_urls
FROM extension_platform_summary e
LEFT JOIN extension_issues_mapping m ON e.extension_name = m.extension_name
LEFT JOIN current_github_issues i ON m.issue_number = i.issue_number
GROUP BY 
    e.extension_name, 
    e.extension_type, 
    e.duckdb_version, 
    e.availability_percentage, 
    e.unavailable_platforms
ORDER BY e.extension_name;

-- View for extensions with correlated issues and availability problems
CREATE OR REPLACE VIEW problematic_extensions_with_issues AS
SELECT 
    p.extension_name,
    p.extension_type,
    p.duckdb_version,
    p.availability_percentage,
    p.unavailable_platforms,
    p.error_summary,
    ei.open_issues_count,
    ei.high_severity_issues,
    ei.availability_issues,
    ei.installation_issues,
    ei.platform_issues,
    ei.related_issue_urls,
    -- Calculate correlation score between availability and issues
    CASE 
        WHEN p.availability_percentage < 50 AND ei.open_issues_count > 0 THEN 'HIGH'
        WHEN p.availability_percentage < 100 AND ei.availability_issues > 0 THEN 'HIGH'
        WHEN p.availability_percentage < 100 AND ei.installation_issues > 0 THEN 'MEDIUM'
        WHEN ei.open_issues_count > 2 THEN 'MEDIUM'
        ELSE 'LOW'
    END as correlation_level
FROM problematic_extensions p
LEFT JOIN extension_issues_with_availability ei ON p.extension_name = ei.extension_name
ORDER BY 
    CASE correlation_level 
        WHEN 'HIGH' THEN 1 
        WHEN 'MEDIUM' THEN 2 
        ELSE 3 
    END,
    p.availability_percentage ASC,
    ei.open_issues_count DESC;

-- View for recent extension issues (last 30 days)
CREATE OR REPLACE VIEW recent_extension_issues AS
SELECT 
    i.issue_number,
    i.title,
    i.state,
    i.created_at,
    i.updated_at,
    i.extension_names,
    i.platforms,
    i.issue_type,
    i.severity,
    i.html_url,
    -- Calculate days since creation
    EXTRACT(DAY FROM (CURRENT_TIMESTAMP - i.created_at)) as days_old
FROM current_github_issues i
WHERE i.created_at >= CURRENT_TIMESTAMP - INTERVAL '30 days'
ORDER BY i.created_at DESC;

-- View for issue trends over time
CREATE OR REPLACE VIEW extension_issues_trends AS
SELECT 
    DATE_TRUNC('week', created_at) as week_start,
    issue_type,
    severity,
    COUNT(*) as issue_count,
    COUNT(CASE WHEN state = 'open' THEN 1 END) as open_count,
    COUNT(CASE WHEN state = 'closed' THEN 1 END) as closed_count
FROM current_github_issues
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '90 days'
GROUP BY DATE_TRUNC('week', created_at), issue_type, severity
ORDER BY week_start DESC, issue_type, severity;