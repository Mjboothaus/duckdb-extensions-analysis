-- Create installation test results table
CREATE TABLE IF NOT EXISTS installation_test_history (
    id INTEGER PRIMARY KEY DEFAULT nextval('installation_test_seq'),
    extension_name VARCHAR NOT NULL,
    platform VARCHAR NOT NULL,
    success BOOLEAN NOT NULL,
    installation_time_seconds DOUBLE,
    load_time_seconds DOUBLE,
    error_message TEXT,
    error_type VARCHAR, -- 'download', 'install', 'load', 'execute', 'environment', 'timeout', 'special_case'
    duckdb_version VARCHAR NOT NULL,
    test_timestamp TIMESTAMP NOT NULL,
    file_size_bytes BIGINT,
    extension_path VARCHAR,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(extension_name, platform, duckdb_version, test_timestamp)
);