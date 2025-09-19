-- Insert or replace DuckDB release information
INSERT OR REPLACE INTO duckdb_releases 
(version, published_date, days_since_release, analysis_date)
VALUES (?, ?, ?, ?);