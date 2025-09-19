INSERT INTO github_issues_history (
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
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);