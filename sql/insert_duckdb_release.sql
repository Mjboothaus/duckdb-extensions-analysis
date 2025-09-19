-- Insert DuckDB release information (ignore if exists)
INSERT OR IGNORE INTO duckdb_releases 
(version, published_date, days_since_release, analysis_date)
VALUES (?, ?, ?, ?);
