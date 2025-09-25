## Data Sources & Methodology

This analysis is based on the following authoritative sources and their structural conventions:

### Core Extensions Data Sources
- **Primary**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Secondary**: [Extensions Overview](https://duckdb.org/docs/stable/extensions/overview.html)  
- **GitHub Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb) for commit history and development stages

**Important Notes on Documentation Structure Exceptions:**
- Some core extensions like `json` and `parquet` have documentation under `/docs/stable/data/` rather than `/docs/stable/core_extensions/`
- URL patterns vary: some use `/extension_name.html` while others use `/extension_name/overview.html`
- The documentation structure may evolve over time, requiring periodic updates to URL discovery logic

### Community Extensions Data Sources  
- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured Page**: [Community Extensions](https://community-extensions.duckdb.org/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

### Status Determination Methodology
- ✅ **Ongoing**: Repository is active and not archived
- 🔴 **Discontinued**: Repository is archived or marked as discontinued  
- ❌ **No Repo/Error**: Repository information unavailable or inaccessible

### Activity & Update Metrics
- **Core Extensions**: Based on last commit date to DuckDB repository for extension-specific code
- **Community Extensions**: Based on last push/commit date to individual extension repositories
- **Caching**: API responses are cached (24 hours for URLs, configurable for other data) to improve performance and reduce rate limiting

### Data Quality & Reliability Notes
- URL discovery relies on parsing HTML documentation pages, which may change structure
- GitHub API rate limits may occasionally affect data freshness
- Extension metadata quality varies between community extensions
- Some extensions may have multiple repositories or documentation locations

Report generated using the [duckdb-extensions-analysis](https://github.com/Mjboothaus/duckdb-extensions-analysis) tool.
