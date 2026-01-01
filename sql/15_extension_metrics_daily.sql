-- Create extension metrics daily table for per-extension tracking
CREATE SEQUENCE IF NOT EXISTS extension_metrics_daily_seq START 1;

CREATE TABLE IF NOT EXISTS extension_metrics_daily (
    id INTEGER PRIMARY KEY DEFAULT nextval('extension_metrics_daily_seq'),
    extension_name VARCHAR NOT NULL,
    extension_type VARCHAR NOT NULL,  -- 'core' or 'community'
    analysis_date DATE NOT NULL,
    stars INTEGER,
    forks INTEGER,
    days_since_update INTEGER,
    status VARCHAR,
    is_active BOOLEAN,
    is_archived BOOLEAN DEFAULT FALSE,
    repository VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(extension_name, extension_type, analysis_date)
);
