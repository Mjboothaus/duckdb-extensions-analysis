-- Insert community extension with errors or no repository info
INSERT INTO community_extensions_history 
(name, repository, status, description, improved_description, featured,
 community_repo_url, install_url, duckdb_version, analysis_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);