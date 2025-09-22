# DuckDB Extensions Analysis

A comprehensive Python tool for analysing the status and maintenance activity of DuckDB extensions, with **historical tracking**, **featured extension detection**, and **multiple export formats**.

## Overview

This project provides in-depth analysis of the DuckDB extension ecosystem:

- **Core Extensions**: Built-in extensions that are part of the main DuckDB release (24 extensions)
- **Community Extensions**: Third-party extensions maintained by the community (80+ extensions)
- **Featured Extensions**: Automatically detected featured extensions from DuckDB documentation 
- **Historical Tracking**: Complete versioned history with DuckDB version correlation

The analysis tracks repository activity, maintenance status, popularity metrics, and identifies potentially discontinued extensions with full historical context.

## Features

### 🔍 **Analysis Capabilities**
- **Comprehensive Coverage**: Examines 24 core + 80+ community extensions
- **Featured Extension Detection**: Automatically identifies ~27 featured extensions from DuckDB docs
- **Enhanced Descriptions**: Generates improved descriptions for extensions with missing/poor descriptions
- **Repository Metrics**: Stars, forks, activity levels, languages, topics, and trends
- **Status Tracking**: Identifies ongoing vs discontinued vs archived extensions

### 📊 **Historical Tracking**
- **Version Correlation**: Links extension data to specific DuckDB versions
- **True Versioning**: Preserves complete historical snapshots (no data overwriting)
- **Analysis Session Tracking**: Records script version, counts, timestamps, and metadata
- **Trend Analysis**: Track extension ecosystem growth over time

### 📈 **Multiple Output Formats**  
- **Markdown Reports**: Comprehensive reports with timestamps
- **CSV Export**: Data analysis-friendly format
- **Excel Reports**: Multi-sheet workbooks with core/community/summary sheets
- **DuckDB Database**: Full historical data with SQL query capabilities

### ⚡ **Performance & Reliability**
- **Async Processing**: Efficient API calls using modern async/await patterns
- **Intelligent Caching**: Configurable caching with TTL and cache bypass options
- **Retry Logic**: Robust error handling with exponential backoff
- **Rate Limit Handling**: Automatic GitHub API rate limit management

## Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for dependency management
- [just](https://github.com/casey/just) for task running (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd duckdb-extensions-analysis
   ```

2. Install dependencies:
   ```bash
   just install
   # or alternatively: uv sync
   ```

3. (Optional) Set up GitHub authentication for higher rate limits:
   ```bash
   # If you have gh CLI installed:
   export GITHUB_TOKEN=$(gh auth token)
   
   # Or set your GitHub token manually:
   export GITHUB_TOKEN=your_github_token_here
   ```

### Usage

#### Using just (recommended)

**Basic Analysis:**
```bash
# Run community extensions analysis only
just analyze community

# Run core extensions analysis only  
just analyze core

# Run full analysis (core + community) - default mode
just analyze all
```

**Reports & Data Export:**
```bash
# Generate comprehensive markdown report
just report

# Generate reports with specific formats
just report-all                    # All formats (markdown, CSV, Excel)
just report --no-issues            # Skip GitHub issues for faster generation

# Quick report generation (fastest - skips GitHub issues)
just report-quick

# Save analysis to DuckDB database
just database

# Save fresh analysis to database (bypass cache)
just database-fresh
```

**Historical Data & Analysis:**
```bash
# Query database with example analytics
just query-db

# Add simulated historical data for demonstration
just backfill-db
```

**Standard Workflows:**
```bash
# Complete workflow: fresh analysis + all reports + database
just workflow-complete

# Quick workflow: cached analysis + markdown report
just workflow-quick

# Fastest workflow: quick report without GitHub issues (fastest)
just workflow-fastest
```

**Utility Commands:**
```bash
# Cache management
just cache-info   # Show cache information
just fresh        # Clear cache and run fresh analysis
just no-cache     # Run analysis bypassing cache

# Development
just check        # Format and lint code
just status       # Show project status
just help         # Show all available commands
```

#### Direct CLI usage

**Analysis Commands:**
```bash
# Basic analysis modes
uv run python scripts/cli.py analyze community
uv run python scripts/cli.py analyze core  
uv run python scripts/cli.py analyze all

# With fresh data (bypass cache)
uv run python scripts/cli.py analyze all --cache-hours 0
uv run python scripts/cli.py analyze all --with-issues  # Enable GitHub issues (slower, may hit rate limits)
```

**Report Generation:**
```bash
# Generate markdown report (default)
uv run python scripts/cli.py report generate

# Generate multiple formats
uv run python scripts/cli.py report generate --format markdown --format csv --format excel
uv run python scripts/cli.py report generate --with-issues  # Enable GitHub issues (slower, may hit rate limits)

# Quick report (fastest - skips GitHub issues)
uv run python scripts/cli.py quick
```

**Database Operations:**
```bash
# Save to database
uv run python scripts/cli.py database save

# Database querying
uv run python scripts/query_database.py
```

**Cache Management:**
```bash
# Show cache information
uv run python scripts/cli.py cache info

# Clear cache
uv run python scripts/cli.py cache clear

# Show version and help
uv run python scripts/cli.py --version
uv run python scripts/cli.py --help
```

**Command Aliases:**
```bash
# Commands support partial matching
uv run python scripts/cli.py ana community      # Same as 'analyze community'
uv run python scripts/cli.py rep generate       # Same as 'report generate'
uv run python scripts/cli.py dat save           # Same as 'database save'
```

## Scripts

### `analyze_extensions.py`

The main unified script supporting multiple analysis modes:

- **community**: Analyses community extensions only
- **core**: Analyses core extensions only  
- **full**: Comprehensive analysis of both core and community extensions
- **report**: Generates detailed reports in markdown, CSV, and/or Excel formats
- **database**: Saves complete analysis results to DuckDB database with historical tracking

The analysis process includes:
- **Dynamic DuckDB version detection** from GitHub releases API
- **Featured extension detection** from official DuckDB documentation
- **Enhanced metadata generation** for extensions with missing descriptions
- **Repository activity analysis** including stars, forks, last push dates, languages
- **Historical data preservation** with DuckDB version correlation
- **Intelligent caching** with configurable TTL and bypass options

### `query_database.py`

Database analysis and querying script:

- **Historical trend analysis** across DuckDB versions
- **Extension popularity tracking** and growth patterns
- **Activity level categorisation** and statistics
- **Featured extension performance** analysis
- **Simulated historical back-filling** for demonstration purposes

Example queries include extension growth trends, most active extensions by version, and ecosystem health metrics.

## Output Formats

The tool generates multiple output formats for different use cases:

### 📝 **Console Logging**
Structured, real-time logging with analysis progress:
```
2025-09-19 11:14:58 | INFO | Found 80 community extensions
2025-09-19 11:14:58 | INFO | Found 27 featured extensions  
2025-09-19 11:14:58 | INFO | gsheets (Repo: evidence-dev/duckdb_gsheets): Ongoing | Last push: 9 days ago
2025-09-19 11:14:58 | INFO | Successfully saved 24 core extensions and 80 community extensions to database
```

### 📊 **Markdown Reports**
Comprehensive reports with extension tables, summaries, and methodology:
- `reports/latest.md` - Always current report (version controlled)
- `reports/duckdb_extensions_report_YYYYMMDD_HHMMSS.md` - Timestamped versions (archived locally)

#### 🗂️ **Report Management & Archiving**

To keep the repository clean while preserving development history:

- ✅ **Version Controlled**: Only `reports/latest.md` is committed to git
- 📦 **Local Archive**: Interim reports are automatically moved to `reports/archive/`
- ❌ **Never Committed**: All timestamped reports and archives are git-ignored
- 🔄 **Auto-Archive**: New reports are automatically excluded from git tracking

**Archive Features:**
- **Local Storage**: Historical reports remain accessible on your machine
- **Development History**: Track evolution of report content and formats
- **Clean Repository**: No interim reports clutter the repository
- **Cleanup Tools**: Optional archive cleanup commands for disk space management

See `reports/archive/README.md` for detailed archive documentation.

### 📈 **CSV & Excel Export** 
Data analysis friendly formats:
- **CSV**: Single flat file for easy analysis
- **Excel**: Multi-sheet workbooks with Core Extensions, Community Extensions, and Summary sheets

### 🗄️ **DuckDB Database**
Complete historical tracking with queryable SQL database:
```sql
-- Extension growth over DuckDB versions
SELECT duckdb_version, COUNT(*) as extensions, SUM(featured::int) as featured
FROM community_extensions_history GROUP BY duckdb_version;

-- Most active extensions
SELECT name, stars, last_push_days FROM community_extensions 
WHERE last_push_days <= 7 ORDER BY stars DESC;
```

### 🔍 **Interactive Database Analysis**
Built-in analytics via `just query-db`:
- Analysis runs history with DuckDB version correlation
- Featured extensions ranking by popularity
- Extension activity trends and statistics  
- Historical version comparisons

## Historical Tracking & Analysis

The project includes **comprehensive historical tracking** capabilities that preserve the complete evolution of the DuckDB extensions ecosystem.

### Key Historical Features

#### 🔄 **Version Correlation**
- Every extension record includes the **DuckDB version** active at analysis time
- Enables correlation between extension ecosystem growth and DuckDB releases
- Tracks how extensions evolve with platform updates

#### 📊 **True Historical Versioning** 
- Uses `INSERT` instead of `INSERT OR REPLACE` to preserve all historical data
- Each analysis run creates new records rather than overwriting existing ones
- Complete audit trail of extension ecosystem evolution

#### 🎯 **Enhanced Extension Metadata**
- **Featured Flag**: Automatically detects ~27 featured extensions from DuckDB docs
- **Improved Descriptions**: Generates descriptions for extensions with missing/poor descriptions
- **Extension URLs**: Direct links to community repo, GitHub repo, installation docs
- **Repository Metrics**: Stars, forks, activity levels, languages, topics

### Database Schema

The enhanced schema includes:
- `core_extensions_history` - Historical snapshots of core extensions
- `community_extensions_history` - Historical snapshots of community extensions
- `analysis_runs` - Metadata about each analysis session
- `duckdb_releases` - DuckDB version information
- Views for current data access (`core_extensions`, `community_extensions`)

### Historical Analysis Examples

```bash
# View historical trends and analysis
just query-db

# Add simulated historical data for demonstration
just backfill-db
```

Sample queries available in the interactive analysis:
- Extension growth over DuckDB versions
- Most active extensions by time period
- Featured extension performance trends
- Extension activity level distributions

**Learn more**: See [Historical Tracking Documentation](docs/historical_tracking.md) for complete details.

---

## Appendices

### Appendix A: Configuration

Configuration is now managed through TOML files for transparency and ease of modification:

#### Configuration Files
- **`conf/config.toml`**: Main application configuration
- **`pyproject.toml`**: Project metadata and version (linked to config)
- **`conf/config.py`**: Python configuration loader

#### Key Configuration Sections
- **GitHub API**: Endpoints, repositories, headers
- **Database**: Schema options (simple vs historical)
- **Caching**: TTL settings for performance
- **Analysis**: URLs and fallback data
- **HTTP**: Timeout and retry settings

#### GitHub Authentication
Set the `GITHUB_TOKEN` environment variable for higher rate limits:
- **Without token**: 60 requests/hour
- **With token**: 5000 requests/hour (recommended)

### Appendix B: Database Schema

The tool supports two schema modes via `conf/config.toml`:

#### Historical Schema (enable_history = true)
- **`core_extensions_history`**: Versioned core extension data
- **`community_extensions_history`**: Versioned community extension data
- **`analysis_runs`**: Analysis session metadata
- **`duckdb_releases`**: DuckDB version information
- **Views**: `core_extensions`, `community_extensions` (current data)

#### Simplified Schema (enable_history = false)
- **`core_extensions`**: Current core extension data
- **`community_extensions`**: Current community extension data
- **`analysis_runs`**: Basic run tracking
- **`duckdb_releases`**: Version information

### Appendix C: SQL Queries

Common analysis queries are stored in `sql/queries.sql`:

```sql
-- Find recently active extensions
SELECT name, repository, last_push_days, stars 
FROM community_extensions 
WHERE last_push_days < 30 AND stars > 10
ORDER BY stars DESC;

-- Extension activity summary
SELECT 
    CASE 
        WHEN last_push_days <= 7 THEN 'Very Active (≤7d)'
        WHEN last_push_days <= 30 THEN 'Active (≤30d)'
        ELSE 'Low Activity'
    END AS activity_level,
    COUNT(*) as count
FROM community_extensions 
GROUP BY activity_level;
```

### Appendix D: Development

#### Code Quality Tools
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checking (future)
- **uv**: Fast dependency management

#### Project Structure
```
duckdb-extensions-analysis/
├── conf/                       # Configuration files
│   ├── config.toml            # Main configuration
│   └── config.py              # Configuration loader
├── sql/                       # SQL files
│   ├── create_schema.sql      # Database schema
│   ├── create_schema_simple.sql # Simplified schema
│   ├── queries.sql            # Common queries
│   └── insert_data.sql        # Data insertion SQL
├── scripts/                   # Python scripts
│   ├── analyze_extensions.py  # Main analysis script
│   └── query_database.py      # Database querying
├── reports/                   # Generated reports
├── data/                      # Database files (git-ignored)
├── justfile                   # Simplified task runner
├── pyproject.toml            # Project metadata
└── README.md                 # This documentation
```

#### Development Commands
```bash
# Install dependencies
just install

# Format and lint code  
just check

# Show project status
just status

# Clean cache and build files
just clean
```

### Appendix E: Performance & Insights

#### Performance Characteristics
- **First run**: ~60-90 seconds (GitHub API calls)
- **Cached runs**: <2 seconds (99% improvement)
- **Cache hit rate**: >95% for repeated analysis

#### Extension Categories Discovered
1. **Core Extensions (24)**: Built into DuckDB
2. **Featured Community (~15)**: Highlighted on DuckDB website  
3. **All Community (80+)**: Complete repository

#### Activity Patterns
- **Very Active**: Daily/weekly commits
- **Stable**: Monthly commits, stable functionality
- **Legacy**: 100+ days since last commit
- **Languages**: Primarily C++, with Python, Rust, JavaScript

### Appendix F: Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and ensure code quality: `just check`
4. Commit with a descriptive message: `git commit -m "feat: add new analysis feature"`
5. Push to your branch: `git push origin feature/your-feature`  
6. Create a Pull Request

### Appendix G: Licence & Acknowledgements

This project is licensed under the MIT Licence.

**Acknowledgements:**
- [DuckDB](https://duckdb.org) for the excellent database engine
- The DuckDB community for maintaining extensions
- All contributors to this analysis tool
