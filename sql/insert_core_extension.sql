-- Insert core extension into history table
INSERT INTO core_extensions_history 
(name, development_stage, status, last_updated_date, last_commit_date, 
 last_commit_sha, last_commit_message, repository, duckdb_version, 
 platform_availability, earliest_availability_date, available_platforms, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
