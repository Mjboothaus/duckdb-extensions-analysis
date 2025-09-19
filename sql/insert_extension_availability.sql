INSERT INTO extension_availability_history (
    extension_name, 
    extension_type, 
    platform, 
    duckdb_version,
    is_available,
    availability_date,
    check_timestamp,
    http_status_code,
    file_size_bytes,
    error_message,
    days_since_release
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);