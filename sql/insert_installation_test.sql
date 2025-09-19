INSERT INTO installation_test_history (
    id,
    extension_name,
    platform,
    success,
    installation_time_seconds,
    load_time_seconds,
    error_message,
    error_type,
    duckdb_version,
    test_timestamp
) VALUES (
    nextval('installation_test_seq'),
    $1, $2, $3, $4, $5, $6, $7, $8, $9
);
