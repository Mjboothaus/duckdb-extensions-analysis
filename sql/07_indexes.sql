-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_core_ext_hist_name_date ON core_extensions_history(name, analysis_date);
CREATE INDEX IF NOT EXISTS idx_community_ext_hist_name_date ON community_extensions_history(name, analysis_date);
CREATE INDEX IF NOT EXISTS idx_core_ext_hist_duckdb_version ON core_extensions_history(duckdb_version);
CREATE INDEX IF NOT EXISTS idx_community_ext_hist_duckdb_version ON community_extensions_history(duckdb_version);