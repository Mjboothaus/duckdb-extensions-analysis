# Extension Status Determination: Assumptions and Logic

## Executive Summary

The DuckDB Extensions Analysis tool provides automated extension classification **with final status determinations requiring manual human review**. The tool generates recommendations and flags potential issues, but definitive extension statuses are stored in configuration files after human verification.

### Key Points

- **Manual Review Required**: All final extension status classifications are stored in `conf/extensions_metadata.toml` after human review of automated analysis results. The tool provides recommendations, but humans make the final determinations.

- **Core extensions** (24) are classified as Ongoing, Platform Limited, or Legacy based on availability testing and platform compatibility checks.

- **Community extensions** (80+) are classified into seven categories (Active, Legacy, Review Required, Deprecated, Under Development, Template, Unknown) based on a decision tree considering:
  - **Explicit manual configurations** (highest priority - stored in config)
  - Automated deprecation detection with keyword scoring
  - Repository activity and maintenance patterns
  - Official status in DuckDB community listings
  - Compatibility test results when enabled

- **Documentation sources** come from multiple locations including DuckDB docs, GitHub repositories, the community-extensions repo, and individual extension repos, with URL patterns assumed for discovery.

- **URL validation** checks both HTTP accessibility and content relevance, detecting broken, valid, or potentially mismatched documentation links.

- **Deprecation detection** uses a keyword-based scoring system analyzing README files, with context extraction to distinguish true deprecation signals from false positives.

- **Version compatibility** is assessed through optional installation testing against current and previous DuckDB releases.

### Configuration-Driven Status Override

The configuration file (`conf/extensions_metadata.toml`) contains explicit human-reviewed classifications:
- `[community_extensions.deprecated]` - Extensions confirmed as deprecated
- `[community_extensions.review_required]` - Extensions flagged for manual verification
- `[community_extensions.templates]` - Template/example extensions not for production

### Key Challenges

- GitHub API rate limits can restrict complete analysis
- Repository structure variations require fallback strategies
- Documentation structure changes may need manual updates
- **Automated classifications may have false positives/negatives requiring human review**

This document details these processes and assumptions to provide transparency into how extension statuses are determined.

---

This document comprehensively describes all assumptions, data sources, and logic used by the DuckDB Extensions Analysis tool to determine the status and classification of DuckDB extensions.

## Table of Contents

- [Executive Summary](#executive-summary)
- [Core Extensions](#core-extensions)
- [Community Extensions](#community-extensions)
- [Documentation Sources](#documentation-sources)
- [Status Classification Logic](#status-classification-logic)
- [URL Discovery and Validation](#url-discovery-and-validation)
- [GitHub API Integration](#github-api-integration)
- [Deprecation Detection](#deprecation-detection)
- [Version Compatibility](#version-compatibility)
- [Known Limitations](#known-limitations)

## Core Extensions

### Data Sources

Core extensions are analyzed using multiple data sources:

1. **DuckDB Official Documentation**
   - Primary source: `https://duckdb.org/docs/stable/core_extensions/overview.html`
   - Extension-specific docs: `https://duckdb.org/docs/stable/core_extensions/{extension_name}.html`
   - Special cases for non-standard paths (see URL Discovery section)

2. **DuckDB GitHub Repository**
   - Main repo: `https://github.com/duckdb/duckdb`
   - Extension source paths vary by extension (see Repository Structure section)
   - Commit history for last update tracking

3. **Extension Metadata Configuration**
   - File: `conf/extensions_metadata.toml`
   - Contains manual overrides and special configurations

### Repository Structure Assumptions

The tool assumes core extensions reside in different paths within the DuckDB repository:

```
duckdb/duckdb/
├── extension/
│   ├── autocomplete/     # Most core extensions here
│   ├── jemalloc/
│   ├── json/
│   └── ...
├── third_party/
│   ├── parquet/          # Some extensions in third_party
│   └── ...
└── tools/
    └── shell/            # Shell-related extensions
```

**Path Mapping Logic** (from `src/analyzers/core_analyzer.py`):
- Primary search: `extension/{name}`
- Fallback paths: `third_party/{name}`, `tools/{name}`, `src/{name}`
- Special cases defined in `EXTENSION_REPO_PATHS` dictionary

### Status Classification for Core Extensions

Core extensions use a simplified status system:

- **🟢 Ongoing**: Active, maintained core extension
- **⚠️ Platform Limited**: Available but with platform restrictions
- **🔄 Legacy**: Compatible with previous DuckDB versions only

**Classification Logic**:
1. All core extensions default to "Ongoing" status
2. Platform availability is checked via HTTP HEAD requests to download URLs
3. Extensions with platform-specific issues may be flagged as "Platform Limited"

## Community Extensions

### Primary Data Sources

1. **DuckDB Community Extensions Repository**
   - Main listing: `https://github.com/duckdb/community-extensions`
   - Directory structure: `extensions/{extension_name}/`
   - Metadata file: `extensions/{extension_name}/description.yml`

2. **Individual Extension Repositories**
   - Retrieved from `description.yml` or inferred from extension name
   - README files analyzed for deprecation indicators
   - GitHub API for stars, last activity, contributors

3. **DuckDB Official Website**
   - Community extensions page: `https://community-extensions.duckdb.org/`
   - Used to identify "official" community extensions

### Repository Structure Assumptions

Community extensions follow this expected structure:

```
duckdb/community-extensions/
└── extensions/
    └── {extension_name}/
        ├── description.yml      # Required metadata file
        ├── README.md           # Optional documentation
        └── ...                 # Extension-specific files
```

**description.yml Format Assumptions**:
```yaml
extension:
  name: "extension_name"
  description: "Brief description"
  version: "1.0.0"
  language: "C++"
  build: "cmake"
  license: "MIT"
  maintainers:
    - github: "username"
  repo:
    github: "owner/repository"
    ref: "main"
  docs:
    hello_world: "SELECT hello('world');"
```

### Status Classification for Community Extensions

Community extensions use a more complex status system based on multiple factors:

#### Status Categories

- **✅ Active**: Actively maintained, compatible with current DuckDB
- **🔄 Legacy**: Compatible only with previous DuckDB versions
- **⚠️ Review Required**: Flagged for manual review due to various indicators
- **❌ Deprecated**: Explicitly marked as deprecated
- **🚧 Under Development**: Work in progress, experimental
- **📝 Template**: Template or example extension
- **❓ Unknown**: Status cannot be determined

#### Classification Logic Flow

```python
def determine_status(extension_info):
    # 1. Check explicit deprecation
    if extension_info.is_explicitly_deprecated():
        return "Deprecated"
    
    # 2. Check if it's a template
    if extension_info.is_template():
        return "Template"
    
    # 3. Check deprecation score from README analysis
    if extension_info.deprecation_score >= 8:
        return "Deprecated"
    elif extension_info.deprecation_score >= 5:
        return "Review Required"
    
    # 4. Check official status
    if extension_info.is_official:
        # Official extensions are more likely to be active
        if extension_info.last_activity_days <= 365:
            return "Active"
        else:
            return "Legacy"
    
    # 5. Check activity and maintenance
    if extension_info.last_activity_days <= 90:
        return "Active"
    elif extension_info.last_activity_days <= 365:
        return "Legacy"
    else:
        return "Review Required"
```

**Factors Considered**:

1. **Explicit Configuration** (highest priority)
   - Extensions listed in `conf/extensions_metadata.toml` under `deprecated`, `review_required`, or `templates`

2. **Deprecation Detection Score** (see Deprecation Detection section)
   - Score ≥ 8: Automatically marked as "Deprecated"
   - Score 5-7: Marked as "Review Required"

3. **Official Status**
   - Extensions listed on `https://community-extensions.duckdb.org/` are considered official
   - Official extensions get preference in status determination

4. **Repository Activity**
   - Last push within 90 days: Likely "Active"
   - Last push 90-365 days: Likely "Legacy"
   - Last push > 365 days: "Review Required" unless other factors apply

5. **Template Detection**
   - Extension name contains "template", "example", or "demo"
   - Repository description indicates it's a template

## Documentation Sources

### URL Discovery Hierarchy

The tool discovers documentation URLs using a hierarchical approach:

#### For Core Extensions

1. **Standard Pattern**: `https://duckdb.org/docs/stable/core_extensions/{name}.html`
2. **Special Cases** (hardcoded in `report_generator.py`):
   ```python
   SPECIAL_CORE_EXTENSION_URLS = {
       'json': 'https://duckdb.org/docs/stable/data/json/overview.html',
       'parquet': 'https://duckdb.org/docs/stable/data/parquet/overview.html',
       'csv': 'https://duckdb.org/docs/stable/data/csv/overview.html'
   }
   ```
3. **Dynamic Discovery**: Scraping the overview page for actual links
4. **Fallback**: Repository URL if documentation not found

#### For Community Extensions

1. **From description.yml**: Custom documentation URL if specified
2. **Standard Pattern**: `https://community-extensions.duckdb.org/extensions/{name}.html`
3. **Repository README**: Repository URL as fallback

### URL Validation Process

All discovered URLs undergo validation:

1. **HTTP Status Check**: HEAD request to verify URL accessibility
2. **Content Validation** (for documentation URLs): GET request to verify the extension name appears in the page content
3. **Classification**:
   - `ok`: URL accessible and content matches
   - `broken_url`: HTTP error (404, 403, etc.)
   - `likely_wrong`: URL accessible but content doesn't match extension name

## GitHub API Integration

### Rate Limiting Assumptions

- **Authenticated requests**: 5000 requests/hour with GitHub token
- **Unauthenticated requests**: 60 requests/hour
- **Retry logic**: Exponential backoff for rate limit errors (403, 429)

### Data Retrieved

For each repository:
- **Basic info**: Stars, forks, language, description
- **Activity**: Last push date, commit count
- **Contributors**: Contributor count and details
- **Releases**: Latest release information

### API Endpoint Assumptions

```python
GITHUB_API_ENDPOINTS = {
    "repo_info": "/repos/{owner}/{repo}",
    "contributors": "/repos/{owner}/{repo}/contributors",
    "releases": "/repos/{owner}/{repo}/releases/latest",
    "commits": "/repos/{owner}/{repo}/commits",
    "contents": "/repos/{owner}/{repo}/contents/{path}"
}
```

## Deprecation Detection

### Keyword-Based Detection

The tool scans README files for deprecation indicators:

```python
DEPRECATION_KEYWORDS = [
    r"\bdeprecated\b",
    r"\bsupersed(ed|es|ing)?\b",
    r"\barchived\b",
    r"\bnot maintained\b",
    r"\bno longer supported\b",
    r"\buse alternative\b",
    r"\bmoved to\b",
    r"\breplaced by\b"
]
```

### Scoring System

Each keyword match contributes to a deprecation score:
- High confidence keywords (e.g., "deprecated"): +3 points
- Medium confidence keywords (e.g., "not maintained"): +2 points
- Low confidence keywords (e.g., "archived"): +1 point

**Interpretation**:
- Score ≥ 8: High confidence deprecated
- Score 5-7: Requires manual review
- Score < 5: Likely active

### Context Analysis

The tool extracts context around deprecation keywords:
- ±5 lines around the matched keyword
- Helps distinguish between actual deprecation and false positives

## Version Compatibility

### DuckDB Version Detection

The tool automatically detects current and previous DuckDB versions:

1. **GitHub Releases API**: `https://api.github.com/repos/duckdb/duckdb/releases`
2. **Version parsing**: Semantic versioning (major.minor.patch)
3. **Stability filter**: Only stable releases (excludes pre-release, beta)

### Compatibility Testing (Optional)

When enabled with `--with-compatibility-testing`:

1. **Installation Testing**: Attempts to install extension in temporary DuckDB instance
2. **Loading Test**: Verifies extension can be loaded
3. **Functional Test**: Runs basic SQL queries if defined
4. **Version Matrix**: Tests against current and previous major versions

### Compatibility Status Classification

- **Compatible**: Successfully installs and loads
- **Installation Failed**: Cannot install (network, build errors)
- **Loading Failed**: Installs but fails to load
- **Version Incompatible**: Works with previous but not current version
- **Platform Incompatible**: Platform-specific installation issues

## Known Limitations

### Data Source Dependencies

1. **DuckDB Documentation Structure**: 
   - Assumes consistent URL patterns
   - Manual updates needed when documentation structure changes

2. **GitHub API Rate Limits**: 
   - Analysis may be incomplete during rate limiting
   - Cached data may become stale

3. **Community Extensions Repository**: 
   - Assumes `description.yml` format consistency
   - New extensions may not be immediately detected

### Classification Edge Cases

1. **False Positives**: 
   - Active extensions may be marked as deprecated due to keyword matches in historical context
   - Template detection may misclassify educational extensions

2. **False Negatives**: 
   - Deprecated extensions without explicit indicators may appear active
   - Subtle deprecation mentions may be missed

3. **Temporal Issues**: 
   - Extension status may change between analysis runs
   - Cached data may not reflect recent changes

### Platform-Specific Limitations

1. **Installation Testing**: 
   - Currently limited to the analysis platform (typically Linux/macOS)
   - Windows compatibility not thoroughly tested

2. **Extension Availability**: 
   - Platform-specific extensions may show inconsistent status
   - Binary availability varies by platform and DuckDB version

## Maintenance and Updates

### Regular Maintenance Required

1. **URL Pattern Updates**: When DuckDB changes documentation structure
2. **Keyword Updates**: As deprecation language evolves
3. **Metadata Updates**: Manual review and updates of `extensions_metadata.toml`
4. **Template Updates**: Report templates may need updates for new extension types

### Monitoring Recommendations

1. **URL Validation Reports**: Regular review of broken or likely-wrong URLs
2. **Deprecation Score Review**: Manual verification of high-scoring extensions
3. **GitHub API Usage**: Monitor rate limit usage and authentication status
4. **Cache Freshness**: Regular cache clearing for accurate analysis

---

*Last updated: 2025-09-30*
*Tool version: 0.1.3*