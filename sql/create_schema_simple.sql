-- DuckDB Extensions Analysis Database Schema - Simplified Version
-- Creates basic tables without historical tracking

-- Core extensions table
CREATE TABLE IF NOT EXISTS core_extensions (
    name VARCHAR PRIMARY KEY,
    development_stage VARCHAR,
    status VARCHAR DEFAULT '✅ Ongoing',
    last_updated_date TIMESTAMP,
    last_commit_date TIMESTAMP,
    last_commit_sha VARCHAR,
    last_commit_message VARCHAR,
    repository VARCHAR,
    duckdb_version VARCHAR,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Community extensions table
CREATE TABLE IF NOT EXISTS community_extensions (
    name VARCHAR PRIMARY KEY,
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
    archived BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    featured BOOLEAN DEFAULT FALSE,
    github_url VARCHAR,
    community_repo_url VARCHAR,
    install_url VARCHAR,
    duckdb_version VARCHAR,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DuckDB releases table
CREATE TABLE IF NOT EXISTS duckdb_releases (
    version VARCHAR PRIMARY KEY,
    published_date TIMESTAMP,
    days_since_release INTEGER,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analysis runs table (lightweight version)
CREATE TABLE IF NOT EXISTS analysis_runs (
    id INTEGER PRIMARY KEY,
    run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duckdb_version VARCHAR,
    script_version VARCHAR,
    total_core_extensions INTEGER,
    total_community_extensions INTEGER,
    featured_extensions_count INTEGER,
    notes TEXT
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_core_ext_name ON core_extensions(name);
CREATE INDEX IF NOT EXISTS idx_community_ext_name ON community_extensions(name);
CREATE INDEX IF NOT EXISTS idx_community_ext_featured ON community_extensions(featured);
CREATE INDEX IF NOT EXISTS idx_community_ext_stars ON community_extensions(stars);