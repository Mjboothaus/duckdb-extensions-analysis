-- Create extension availability history table
CREATE TABLE IF NOT EXISTS extension_availability_history (
    id INTEGER PRIMARY KEY DEFAULT nextval('ext_availability_hist_seq'),
    extension_name VARCHAR NOT NULL,
    extension_type VARCHAR NOT NULL, -- 'core' or 'community'
    platform VARCHAR NOT NULL, -- 'linux_amd64', 'osx_amd64', 'osx_arm64', 'windows_amd64'
    duckdb_version VARCHAR NOT NULL,
    is_available BOOLEAN NOT NULL,
    availability_date TIMESTAMP, -- When extension became available (first successful check)
    check_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    http_status_code INTEGER, -- HTTP response code for availability check
    file_size_bytes BIGINT, -- Size of extension file if available
    error_message TEXT, -- Error details if not available
    days_since_release INTEGER, -- Days since DuckDB release when checked
    UNIQUE(extension_name, platform, duckdb_version, check_timestamp)
);