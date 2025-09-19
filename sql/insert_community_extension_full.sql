-- Insert community extension with full repository information
INSERT INTO community_extensions_history 
(name, repository, status, last_push_date, last_push_days, stars, forks, 
 language, description, improved_description, homepage, license, topics, archived, 
 created_at, updated_at, featured, github_url, community_repo_url, install_url, 
 duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);