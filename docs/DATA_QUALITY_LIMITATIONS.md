# Data Quality & Limitations

## Understanding "NOT FOUND" Messages

When an extension shows "NOT FOUND" or "No Repo/Error", this typically means:
- **Core Extensions**: The extension's documentation URL doesn't follow the standard pattern, or the extension is embedded/integrated in ways that don't require a dedicated doc page
- **Community Extensions**: The repository link is unavailable, private, or the extension metadata is incomplete

**Examples of legitimate "NOT FOUND" cases:**
- **motherduck**: Closed-source commercial extension with vendor-specific access
- **vortex**: Proprietary extension with separate distribution model
- Built-in extensions deeply integrated into DuckDB core (e.g., CSV, JSON, Parquet)

## Metadata Caveats

### Documentation Structure Variations
DuckDB's documentation structure is not entirely uniform:
- Some core extensions (e.g., `json`, `parquet`) have documentation under `/docs/stable/data/` rather than `/docs/stable/core_extensions/`
- URL patterns vary: some use `/extension_name.html` while others use `/extension_name/overview.html`
- The structure may evolve over time, requiring periodic updates to URL discovery logic

### Community Extensions Variability
- Repository activity and metadata quality vary significantly across community extensions
- Some extensions may have multiple repositories or documentation locations
- Not all extensions follow the same GitHub repository structure conventions

## Best Practices for Using This Data

1. **Verification**: For critical decisions, cross-reference with official [DuckDB documentation](https://duckdb.org/docs/)
2. **Freshness**: Check the report generation timestamp and cache settings
3. **Rate Limits**: GitHub API rate limits may occasionally affect data freshness; GitHub token authentication is recommended for frequent analysis
4. **Installation Testing**: "NOT FOUND" doesn't necessarily mean the extension is broken—test installation with `INSTALL extension_name;` in DuckDB

## Data Sources

- **Core Extensions**: [DuckDB Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Community Extensions**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Release Information**: [DuckDB Release Calendar](https://duckdb.org/release_calendar.html)
- **API Data**: GitHub API (with caching to reduce rate limiting)

## Known Limitations

- **URL Discovery**: Relies on parsing HTML documentation pages, which may change structure
- **API Rate Limits**: GitHub API rate limits may affect data freshness (use GitHub token for higher limits)
- **Caching**: Default caching (24 hours for URLs, configurable for other data) means some data may be slightly stale
- **Closed-Source Extensions**: Cannot analyse proprietary extensions not in public repositories

## Reporting Issues

If you find incorrect data or missing extensions:
1. Check the [extensions metadata configuration](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/conf/extensions_metadata.toml)
2. Report issues at the [GitHub repository](https://github.com/Mjboothaus/duckdb-extensions-analysis/issues)
3. For DuckDB core extension issues, see [DuckDB's GitHub](https://github.com/duckdb/duckdb/issues)
