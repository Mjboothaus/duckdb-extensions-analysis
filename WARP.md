# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

**DuckDB Extensions Analysis** is a comprehensive automated monitoring tool for DuckDB's extension ecosystem. It tracks both core extensions (maintained by DuckDB team) and community extensions (third-party), generating daily reports in multiple formats (Markdown, CSV, Excel, HTML).

The tool analyzes 100+ extensions, tracking GitHub activity, installation health, repository status, and issues across the ecosystem with intelligent caching and historical tracking capabilities.

## Development Setup

```bash
# Install dependencies (uses uv for Python project management)
just install

# Optional: Setup GitHub authentication for higher API rate limits
just setup-auth
```

**Python version**: 3.13 (specified in `.python-version`)

**Note**: GitHub Actions workflows use Python 3.12 for better wheel compatibility.

## Essential Commands

### Primary Workflows
```bash
# Complete workflow: analyze → report → database (uses cache)
just workflow

# Fresh workflow: bypass cache and use latest data
just workflow-fresh

# Complete workflow with GitHub issues analysis (slower)
just workflow-issues

# Complete workflow including HTML site generation
just workflow-site
```

### Analysis Commands
```bash
# Analyze extensions
just analyze core                  # Core extensions only
just analyze community             # Community extensions only
just analyze all                   # All extensions (default)

# Fresh analysis (bypass cache)
just fresh all                     # or: just fresh core/community
```

### Report Generation
```bash
# Generate reports in various formats
just report                        # Markdown only
just report-all                    # MD + CSV + Excel
just report-issues                 # Markdown with GitHub issues
just report-all-issues             # All formats with issues

# Generate HTML site from latest report
just site
```

### Status Checks (Quick Freshness)
```bash
# Check if extensions are up-to-date
uv run scripts/cli.py status core
uv run scripts/cli.py status community h3 prql bigquery
uv run scripts/cli.py status all --as-of-date 2025-09-16 h3 prql
```

### Database Operations
```bash
# Save analysis to DuckDB database
just database

# Interactive database analytics
just query
```

### Cache Management
```bash
# Cache operations
just cache-info                    # Show cache statistics
just cache-clear                   # Clear all cache
just cache-stash                   # Save current cache with timestamp
just cache-list-stashes           # List saved caches
just cache-restore                # Restore most recent stash
just cache-restore-from 20250925  # Restore specific stash
just cache-cleanup-stashes        # Keep only 5 most recent stashes
```

### Code Quality
```bash
# Format and lint code (using ruff)
just check

# Run tests
uv run pytest
```

### Utilities
```bash
# Validate release history against GitHub releases
just validate-releases

# Detect deprecated extensions
just deprecation                   # Full report to file
just deprecation-quick            # Quick output to console
just deprecation-json             # JSON format for processing
just deprecation-csv              # CSV format for spreadsheet

# Show project status
just status
```

## Testing

The project uses **pytest** for testing. Test files are located in `tests/` directory.

```bash
# Run all tests
uv run pytest

# Run specific test
uv run pytest tests/test_installation_tester.py

# Run with verbose output
uv run pytest -v
```

**Test configuration**: `pytest.ini` specifies async testing mode and test discovery patterns.

## Architecture

### Project Structure
```
duckdb-extensions-analysis/
├── src/analyzers/          # Core analysis modules
│   ├── orchestrator.py       # Main coordinator for all analysis
│   ├── core_analyzer.py      # Core extensions analysis
│   ├── community_analyzer.py # Community extensions analysis
│   ├── github_api.py         # GitHub API client with caching
│   ├── github_issues_tracker.py  # Issues tracking
│   ├── report_generator.py   # Report generation (all formats)
│   ├── database_manager.py   # DuckDB database operations
│   ├── url_validator.py      # URL validation for extensions
│   └── installation_tester.py  # Extension installation tests
├── src/templates.py        # Jinja2 template engine
├── scripts/                # CLI and utility scripts
│   ├── cli.py               # Click-based CLI (main entry point)
│   ├── query_database.py    # Database analytics queries
│   ├── detect_deprecated_extensions.py  # Deprecation detector
│   └── build_report_site.py # HTML site generator
├── conf/                   # Configuration
│   ├── config.py            # Configuration loader
│   ├── config.toml          # Main settings
│   └── extensions_metadata.toml  # Extension metadata overrides
├── templates/              # Jinja2 templates
│   ├── config/              # TOML configs for templates
│   ├── components/          # Reusable template sections
│   ├── reports/             # Main report templates
│   └── formats/             # Format-specific templates
├── reports/                # Generated reports (output)
├── sql/                    # SQL queries for database analysis
└── .cache/                 # Intelligent caching (diskcache)
```

### Key Design Patterns

**Analysis Pipeline**:
1. **Discovery**: Extensions found from DuckDB docs + community registry
2. **Analysis**: Gather metadata via GitHub API (with caching)
3. **Processing**: Clean, enrich, standardize data
4. **Output**: Generate reports via Jinja2 templates + save to DuckDB
5. **Historical**: Version tracking for trend analysis (optional)

**Orchestrator Pattern**: `AnalysisOrchestrator` coordinates all analysis modules:
- Core and community analyzers
- GitHub API client with intelligent caching
- Report generation (Markdown, CSV, Excel)
- Database operations
- URL validation
- Issues tracking

**Template System**: Jinja2 + TOML configuration:
- Templates: `templates/reports/full_analysis.md.j2`
- Components: `templates/components/*.md.j2` (reusable sections)
- Configuration: `templates/config/*.toml` (layouts, formatting, URLs)
- Custom filters for dates, badges, numbers

**Caching Strategy**: `diskcache` with configurable TTL:
- Default: 1 hour (configurable via `--cache-hours`)
- Web content: 24 hours
- Cache directory: `.cache/`
- Stash system for saving/restoring cache states

### CLI Architecture

The CLI uses **Click** framework (`scripts/cli.py`) with command groups:
- `analyze`: Run extension analysis
- `report`: Generate reports
- `database`: Database operations
- `cache`: Cache management
- `status`: Quick freshness checks

**Entry point**: `uv run scripts/cli.py <command>`

All `just` commands are wrappers around the CLI for convenience.

## Configuration

Main configuration in `conf/config.toml`:
- **GitHub API**: Repository URLs, endpoints
- **Caching**: Duration settings for different content types
- **Analysis**: Core extensions URL, popular extensions fallback
- **Database**: Historical tracking settings
- **HTTP**: Timeout, retry settings
- **Logging**: Level and format

Extension metadata overrides in `conf/extensions_metadata.toml` (for deprecated extensions, custom descriptions, etc.).

## GitHub Actions

Daily automation at 6 AM UTC via `.github/workflows/daily-extensions-report.yml`:
1. Analyze all extensions (with GitHub issues)
2. Generate reports (MD, CSV, Excel)
3. Update README.md with latest status
4. Commit and push reports
5. Deploy HTML site to GitHub Pages

**Manual trigger**: Workflow can be triggered manually via GitHub UI.

## Data Outputs

Generated reports in `reports/`:
- `latest.md` - Human-readable Markdown report
- `*.csv` - Machine-readable data for analysis
- `*.xlsx` - Multi-sheet Excel reports
- `deprecation_analysis_*.md` - Deprecated extensions report

Database: `data/extensions.duckdb` - Queryable DuckDB database with analysis results.

HTML site: `_site/` - Static HTML site deployed to GitHub Pages.

## Important Notes

- **GitHub Token**: Optional but recommended to avoid rate limits. Set via `just setup-auth` or export `GITHUB_TOKEN` environment variable.
- **Cache Strategy**: Use caching for faster repeated runs. Use `just workflow-fresh` for latest data bypassing cache.
- **GitHub Issues**: Disabled by default (`enable_issues_analysis = false` in config) to avoid rate limits. Enable for comprehensive health monitoring.
- **Historical Tracking**: Disabled by default. Enable in config for versioned data with DuckDB release correlation.
- **Australian English**: Use for all documentation and comments (prefer US spelling for code identifiers).

## Troubleshooting

**Rate Limits**: If hitting GitHub API rate limits, ensure `GITHUB_TOKEN` is set via `just setup-auth` or manually export the token.

**Cache Issues**: Clear cache with `just cache-clear` or use fresh workflows `just workflow-fresh`.

**Stale Data**: Use `--cache-hours 0` or `just fresh` commands to bypass cache completely.

**Testing Changes**: Test individual components before running full workflow:
```bash
uv run scripts/cli.py analyze core --cache-hours 1
uv run scripts/cli.py report generate --format markdown
```
