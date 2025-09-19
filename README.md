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
just community

# Run core extensions analysis only  
just core

# Run full analysis (core + community)
just full
```

**Reports & Data Export:**
```bash
# Generate comprehensive markdown report
just report

# Generate CSV report
just report-csv

# Generate Excel report
just report-excel

# Generate all report formats
just report-all

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
# Complete workflow: database + all reports
just workflow-complete

# Fresh complete workflow (no cache)
just workflow-fresh

# Quick workflow: cached analysis + markdown report
just workflow-quick

# Data export workflow: database + spreadsheets
just workflow-export

# Development workflow: setup + fresh analysis + reports
just workflow-dev
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

#### Direct execution

```bash
# Basic analysis modes
uv run python scripts/analyze_extensions.py community
uv run python scripts/analyze_extensions.py core
uv run python scripts/analyze_extensions.py full

# Report generation
uv run python scripts/analyze_extensions.py report
uv run python scripts/analyze_extensions.py report --csv
uv run python scripts/analyze_extensions.py report --excel
uv run python scripts/analyze_extensions.py report --csv --excel

# Database operations
uv run python scripts/analyze_extensions.py database
uv run python scripts/analyze_extensions.py database --no-cache

# Cache management
uv run python scripts/analyze_extensions.py report --cache-info
uv run python scripts/analyze_extensions.py full --clear-cache
uv run python scripts/analyze_extensions.py full --no-cache

# Database querying
uv run python scripts/query_database.py
uv run python scripts/query_database.py backfill
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
- `reports/latest.md` - Always current report
- `reports/duckdb_extensions_report_YYYYMMDD_HHMMSS.md` - Timestamped versions

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

## Configuration

The scripts use several configuration constants that can be modified:

- `GITHUB_API_BASE`: GitHub API endpoint
- `COMMUNITY_REPO`: Community extensions repository
- `DUCKDB_VERSION`: Current DuckDB version for core analysis
- `HEADERS`: HTTP headers for API requests

### GitHub Rate Limits

The GitHub API has rate limits (60 requests/hour for unauthenticated requests). For better performance and to avoid rate limiting:

1. **Recommended**: Use GitHub authentication by setting the `GITHUB_TOKEN` environment variable
2. The scripts will automatically detect and use the token for authenticated requests (5000 requests/hour)
3. If you hit rate limits, the scripts will show 403 errors but will continue processing

## Development

### Code Quality

The project uses modern Python tooling:

- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checking
- **uv**: Fast dependency resolution and environment management

Run quality checks:

```bash
just check
# or: just format && just lint
```

### Project Structure

```
├── scripts/
│   ├── analyze_extensions.py   # Main analysis script with historical tracking
│   └── query_database.py       # Database querying and analysis examples
├── reports/                    # Generated reports in multiple formats
│   ├── latest.md               # Always points to most recent markdown report
│   ├── duckdb_extensions_report_*.md   # Timestamped markdown reports
│   ├── duckdb_extensions_report_*.csv  # CSV exports
│   └── duckdb_extensions_report_*.xlsx # Excel workbooks
├── data/                       # Database and data files (git-ignored)
│   └── extensions.duckdb       # Historical tracking database
├── docs/                       # Project documentation
│   ├── project_summary.md      # Comprehensive project overview
│   └── historical_tracking.md  # Historical tracking documentation
├── .cache/                     # HTTP response cache (git-ignored)
├── justfile                    # Task runner with workflow recipes
├── pyproject.toml             # Project configuration and dependencies
├── uv.lock                    # Locked dependency versions
└── README.md                  # This documentation
```

## Dependencies

### Runtime
- **httpx**: Modern async HTTP client for API requests
- **requests**: HTTP library for web content fetching
- **beautifulsoup4**: HTML parsing for documentation scraping
- **loguru**: Structured logging with rich formatting
- **tenacity**: Retry logic with exponential backoff
- **pyyaml**: YAML file parsing for extension metadata
- **diskcache**: Intelligent caching with TTL support
- **pandas**: Data manipulation for CSV/Excel report generation
- **openpyxl**: Excel file writing capabilities
- **duckdb**: Embedded database for historical tracking

### Development
- **ruff**: Fast Python linting and formatting
- **mypy**: Static type checking

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests if applicable
4. Ensure code quality: `just check`
5. Commit with a descriptive message: `git commit -m "feat: add new analysis feature"`
6. Push to your branch: `git push origin feature/your-feature`
7. Create a Pull Request

## Licence

This project is licensed under the MIT Licence. See the LICENSE file for details.

## Acknowledgements

- [DuckDB](https://duckdb.org) for the excellent database engine
- The DuckDB community for maintaining extensions
- All contributors to this analysis tool