# 🦆 Duck Sources: Where the Data Comes From

This document explains the data sources and collection methodology used by the DuckDB Extensions Analysis tool.

## 📊 Core Extensions Data Sources

### Primary Documentation
- **Extensions Overview**: [DuckDB Extensions](https://duckdb.org/docs/stable/extensions/overview.html)
- **Core Extensions**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Extension Versioning**: [Extension Versioning](https://duckdb.org/docs/stable/extensions/versioning_of_extensions.html)

### Repository Information
- **Main Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- **External Repositories**: Individual repositories for extensions like `duckdb/duckdb-avro`, `duckdb/duckdb-aws`, etc.
- **GitHub API**: Used to fetch commit histories, activity dates, and repository metadata

### Extension Metadata Collection
- **Discovery Method**: HTML parsing of DuckDB documentation pages
- **URL Patterns**: 
  - Standard: `/docs/stable/core_extensions/{extension_name}.html`
  - Overview: `/docs/stable/core_extensions/{extension_name}/overview.html`
  - Special cases: Some extensions like `json` and `parquet` are under `/docs/stable/data/`
- **Activity Data**: Last commit dates from GitHub API for each extension's source code

## 🌐 Community Extensions Data Sources

### Registry and Discovery
- **Primary Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Extensions Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured Page**: [Community Extensions](https://community-extensions.duckdb.org/)
- **Metadata Files**: `description.yml` files in each extension directory

### Repository Analysis
- **Individual Repositories**: GitHub repositories linked in the community extensions registry
- **GitHub API Endpoints**:
  - Repository information: `GET /repos/{owner}/{repo}`
  - Commit history: `GET /repos/{owner}/{repo}/commits`
  - Repository metadata: stars, language, topics, archive status
- **Activity Metrics**: Last push dates, commit frequency, repository status

### Featured Extensions Detection
- **Automatic Discovery**: Parsing of the community extensions website
- **Fallback List**: Hardcoded list of popular extensions in case automatic detection fails
- **Featured Criteria**: Extensions prominently displayed on the official community page

## 🔍 Data Collection Process

### 1. DuckDB Release Information
```
Source: GitHub Releases API
Endpoint: https://api.github.com/repos/duckdb/duckdb/releases/latest
Data: Version number, release date, release notes
```

### 2. Core Extensions Discovery
```
Process:
1. Parse https://duckdb.org/docs/stable/core_extensions/overview.html
2. Extract extension names and documentation links
3. Query GitHub API for each extension's activity
4. Determine repository location (main repo vs external)
5. Generate appropriate repository and documentation URLs
```

### 3. Community Extensions Analysis
```
Process:
1. Fetch extensions list from community-extensions repository
2. For each extension:
   a. Read description.yml metadata
   b. Extract GitHub repository information
   c. Query GitHub API for repository status and activity
   d. Calculate activity metrics and status
3. Sort by activity and categorize by status
```

### 4. URL Validation
```
Process:
1. Collect all repository and documentation URLs
2. Perform HTTP HEAD requests to validate accessibility
3. Mark broken links with 404 errors
4. Cache validation results (24-hour TTL)
```

## ⚡ Performance and Caching

### Caching Strategy
- **Web Content**: 24 hours (documentation pages, featured extensions)
- **GitHub API**: 1 hour (repository info, commits)
- **URL Validation**: 24 hours (link health checks)
- **Analysis Results**: Generated fresh for each report

### Rate Limiting
- **GitHub API**: Respects rate limits with exponential backoff
- **HTTP Requests**: Concurrent requests with timeout controls
- **Retry Logic**: Automatic retries for transient failures

## 🛠️ Configuration and Overrides

### Extension Metadata Configuration
File: `conf/extensions_metadata.toml`
- Repository overrides for extensions with non-standard locations
- Special URL patterns for documentation
- External repository mappings

### Manual Corrections
- Core extensions pointing to main DuckDB repo: `autocomplete`, `icu`, `jemalloc`, `json`, `parquet`, `tpcds`, `tpch`, `ducklake`
- External repositories: `avro`, `aws`, `azure`, `delta`, `spatial`, etc.
- Special documentation URLs for `json` and `parquet` (under `/data/` instead of `/core_extensions/`)

## 📈 Data Quality Notes

### Reliability Factors
- **Documentation Structure**: May change over time, requiring updates to parsing logic
- **GitHub API Availability**: Subject to rate limits and service availability
- **Community Repository Updates**: Extension metadata quality varies
- **URL Stability**: Documentation URLs may change with DuckDB releases

### Known Limitations
- Some extensions may have multiple repositories or documentation locations
- Repository activity dates may not reflect actual extension development activity
- Community extension descriptions depend on maintainer-provided metadata
- Network connectivity affects data collection reliability

## 🔄 Update Frequency

### Automated Updates
- **GitHub Action**: Can be configured to run daily reports
- **Cache Invalidation**: Automatic refresh based on TTL settings
- **Real-time Data**: Fresh analysis for each report generation

### Manual Updates
- Configuration files can be updated to handle new extensions or URL changes
- Extension metadata can be manually corrected for special cases
- Repository overrides can be added for non-standard extension layouts

---

This comprehensive data collection approach ensures accurate, up-to-date information about the DuckDB extensions ecosystem while maintaining performance through intelligent caching and respecting API rate limits.