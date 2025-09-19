-- Data insertion SQL statements for DuckDB Extensions Analysis

-- Insert DuckDB release information
-- Parameters: version, published_date, days_since_release, analysis_date
INSERT OR REPLACE INTO duckdb_releases 
(version, published_date, days_since_release, analysis_date)
VALUES (?, ?, ?, ?);

-- Insert analysis run record
-- Parameters: run_timestamp, duckdb_version, script_version, total_core_extensions, 
--            total_community_extensions, featured_extensions_count, notes
INSERT INTO analysis_runs 
(run_timestamp, duckdb_version, script_version, total_core_extensions, 
 total_community_extensions, featured_extensions_count, notes)
VALUES (?, ?, ?, ?, ?, ?, ?);

-- Insert core extension (into history table for versioning)
-- Parameters: name, development_stage, status, last_updated_date, last_commit_date, 
--            last_commit_sha, last_commit_message, repository, duckdb_version, analysis_date
INSERT INTO core_extensions_history 
(name, development_stage, status, last_updated_date, last_commit_date, 
 last_commit_sha, last_commit_message, repository, duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- Insert community extension with full data (into history table for versioning)
-- Parameters: name, repository, status, last_push_date, last_push_days, stars, forks, 
--            language, description, improved_description, homepage, license, topics, archived, 
--            created_at, updated_at, featured, github_url, community_repo_url, install_url, 
--            duckdb_version, analysis_date
INSERT INTO community_extensions_history 
(name, repository, status, last_push_date, last_push_days, stars, forks, 
 language, description, improved_description, homepage, license, topics, archived, 
 created_at, updated_at, featured, github_url, community_repo_url, install_url, 
 duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- Insert community extension with error/minimal data
-- Parameters: name, repository, status, description, improved_description, featured,
--            community_repo_url, install_url, duckdb_version, analysis_date
INSERT INTO community_extensions_history 
(name, repository, status, description, improved_description, featured,
 community_repo_url, install_url, duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- For simplified schema (without history) - Insert/Update core extension
INSERT OR REPLACE INTO core_extensions 
(name, development_stage, status, last_updated_date, last_commit_date, 
 last_commit_sha, last_commit_message, repository, duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- For simplified schema (without history) - Insert/Update community extension
INSERT OR REPLACE INTO community_extensions 
(name, repository, status, last_push_date, last_push_days, stars, forks, 
 language, description, improved_description, homepage, license, topics, archived, 
 created_at, updated_at, featured, github_url, community_repo_url, install_url, 
 duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);