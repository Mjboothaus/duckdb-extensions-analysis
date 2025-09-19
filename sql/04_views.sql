-- Create current views for latest data (for backwards compatibility)
CREATE OR REPLACE VIEW core_extensions AS
SELECT DISTINCT ON (name) *
FROM core_extensions_history
ORDER BY name, analysis_date DESC;

CREATE OR REPLACE VIEW community_extensions AS
SELECT DISTINCT ON (name) *
FROM community_extensions_history
ORDER BY name, analysis_date DESC;