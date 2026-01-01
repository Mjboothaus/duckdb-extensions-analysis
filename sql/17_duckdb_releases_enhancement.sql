-- Enhance duckdb_releases table with additional metadata from CSV
-- Add new columns if they don't exist (using IF NOT EXISTS)

-- Add lts column
ALTER TABLE duckdb_releases ADD COLUMN IF NOT EXISTS lts BOOLEAN DEFAULT FALSE;

-- Add codename column
ALTER TABLE duckdb_releases ADD COLUMN IF NOT EXISTS codename VARCHAR;

-- Add duck_species column
ALTER TABLE duckdb_releases ADD COLUMN IF NOT EXISTS duck_species VARCHAR;

-- Add duck_wikipage column
ALTER TABLE duckdb_releases ADD COLUMN IF NOT EXISTS duck_wikipage VARCHAR;

-- Add blog_post column
ALTER TABLE duckdb_releases ADD COLUMN IF NOT EXISTS blog_post VARCHAR;

-- Add end_of_life column
ALTER TABLE duckdb_releases ADD COLUMN IF NOT EXISTS end_of_life DATE;
