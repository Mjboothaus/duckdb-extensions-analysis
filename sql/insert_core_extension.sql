-- Insert core extension into history table
INSERT INTO core_extensions_history 
(name, development_stage, status, last_updated_date, last_commit_date, 
 last_commit_sha, last_commit_message, repository, duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);