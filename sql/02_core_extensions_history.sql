-- Create core extensions history table
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
    platform_availability JSON, -- Platform availability info
    earliest_availability_date TIMESTAMP, -- Earliest availability across platforms
    available_platforms VARCHAR[], -- List of available platforms
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
