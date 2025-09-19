-- Create GitHub issues history table for tracking extension-related issues
CREATE TABLE IF NOT EXISTS github_issues_history (
    id INTEGER PRIMARY KEY DEFAULT nextval('github_issues_seq'),
    issue_number INTEGER NOT NULL,
    title VARCHAR NOT NULL,
    body TEXT,
    state VARCHAR NOT NULL, -- 'open' or 'closed'
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    closed_at TIMESTAMP,
    labels VARCHAR[], -- Array of issue labels
    extension_names VARCHAR[], -- Extensions mentioned in this issue
    platforms VARCHAR[], -- Platforms mentioned in this issue
    issue_type VARCHAR NOT NULL, -- 'installation', 'availability', 'platform', 'build', 'other'
    severity VARCHAR NOT NULL, -- 'high', 'medium', 'low'
    html_url VARCHAR NOT NULL,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(issue_number, analysis_date)
);

-- Create extension-issue mapping table for easier querying
CREATE TABLE IF NOT EXISTS extension_issues_mapping (
    id INTEGER PRIMARY KEY DEFAULT nextval('ext_issues_mapping_seq'),
    extension_name VARCHAR NOT NULL,
    extension_type VARCHAR NOT NULL, -- 'core' or 'community'
    issue_number INTEGER NOT NULL,
    relevance_score DOUBLE DEFAULT 1.0, -- How relevant this issue is to the extension (0-1)
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(extension_name, issue_number, analysis_date)
);