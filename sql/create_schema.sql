-- DuckDB Extensions Analysis Database Schema
-- Creates tables for storing core and community extension data

-- Create sequences for auto-incrementing IDs (used if enable_history is true)
CREATE SEQUENCE IF NOT EXISTS core_ext_hist_seq;
CREATE SEQUENCE IF NOT EXISTS community_ext_hist_seq;
CREATE SEQUENCE IF NOT EXISTS analysis_runs_seq;

-- Core extensions history table (supports historical tracking)
CREATE TABLE IF NOT EXISTS core_extensions_history (
    id INTEGER PRIMARY KEY DEFAULT nextval('core_ext_hist_seq'),
    name VARCHAR NOT NULL,
    development_stage VARCHAR,
    status VARCHAR,
    last_updated_date TIMESTAMP,
    last_commit_date TIMESTAMP,
    last_commit_sha VARCHAR,
    last_commit_message VARCHAR,
    repository VARCHAR,
    duckdb_version VARCHAR,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Community extensions history table (supports historical tracking)
CREATE TABLE IF NOT EXISTS community_extensions_history (
    id INTEGER PRIMARY KEY DEFAULT nextval('community_ext_hist_seq'),
    name VARCHAR NOT NULL,
    repository VARCHAR,
    status VARCHAR,
    last_push_date TIMESTAMP,
    last_push_days INTEGER,
    stars INTEGER,
    forks INTEGER,
    language VARCHAR,
    description TEXT,
    improved_description TEXT,
    homepage VARCHAR,
    license VARCHAR,
    topics VARCHAR[],
    archived BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    featured BOOLEAN DEFAULT FALSE,
    github_url VARCHAR,
    community_repo_url VARCHAR,
    install_url VARCHAR,
    duckdb_version VARCHAR,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Current views for latest data (for backwards compatibility)
CREATE OR REPLACE VIEW core_extensions AS
SELECT DISTINCT ON (name) *
FROM core_extensions_history
ORDER BY name, analysis_date DESC;

CREATE OR REPLACE VIEW community_extensions AS
SELECT DISTINCT ON (name) *
FROM community_extensions_history
ORDER BY name, analysis_date DESC;

-- DuckDB releases table
CREATE TABLE IF NOT EXISTS duckdb_releases (
    version VARCHAR PRIMARY KEY,
    published_date TIMESTAMP,
    days_since_release INTEGER,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analysis runs table to track each analysis session
CREATE TABLE IF NOT EXISTS analysis_runs (
    id INTEGER PRIMARY KEY DEFAULT nextval('analysis_runs_seq'),
    run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duckdb_version VARCHAR,
    script_version VARCHAR,
    total_core_extensions INTEGER,
    total_community_extensions INTEGER,
    featured_extensions_count INTEGER,
    notes TEXT
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_core_ext_hist_name_date ON core_extensions_history(name, analysis_date);
CREATE INDEX IF NOT EXISTS idx_community_ext_hist_name_date ON community_extensions_history(name, analysis_date);
CREATE INDEX IF NOT EXISTS idx_core_ext_hist_duckdb_version ON core_extensions_history(duckdb_version);
CREATE INDEX IF NOT EXISTS idx_community_ext_hist_duckdb_version ON community_extensions_history(duckdb_version);