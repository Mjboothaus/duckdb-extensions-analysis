-- Create analysis runs table to track each analysis session
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