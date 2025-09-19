-- Insert analysis run record
INSERT INTO analysis_runs 
(run_timestamp, duckdb_version, script_version, total_core_extensions, 
 total_community_extensions, featured_extensions_count, notes)
VALUES (?, ?, ?, ?, ?, ?, ?);