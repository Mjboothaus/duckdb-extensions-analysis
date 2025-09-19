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
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);