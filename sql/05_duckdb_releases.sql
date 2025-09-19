-- Create DuckDB releases table
CREATE TABLE IF NOT EXISTS duckdb_releases (
    version VARCHAR PRIMARY KEY,
    published_date TIMESTAMP,
    days_since_release INTEGER,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);