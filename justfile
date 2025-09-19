# Cross-platform justfile for DuckDB Extensions Analysis
# Works on macOS, Windows, and Linux

# Default recipe - show available commands
default:
    @just --list

# Install dependencies using uv
install:
    uv sync

# Run the community extensions analysis
community:
    uv run python scripts/analyze_extensions.py community

# Run the core extensions analysis
core:
    uv run python scripts/analyze_extensions.py core

# Run the full extensions analysis (core + community)
full:
    uv run python scripts/analyze_extensions.py full

# Run both analyses sequentially
all: community core

# Generate comprehensive markdown report
report:
    uv run python scripts/analyze_extensions.py report

# Generate CSV report
report-csv:
    uv run python scripts/analyze_extensions.py report --csv

# Generate Excel report
report-excel:
    uv run python scripts/analyze_extensions.py report --excel

# Generate all report formats
report-all:
    uv run python scripts/analyze_extensions.py report --csv --excel

# Save analysis to DuckDB database
database:
    uv run python scripts/analyze_extensions.py database

# Save analysis to database without cache
database-fresh:
    uv run python scripts/analyze_extensions.py database --no-cache

# Query the extensions database with example queries
query-db:
    uv run python scripts/query_database.py

# Back-fill database with simulated historical data
backfill-db:
    uv run python scripts/query_database.py backfill

# Clear cache and run fresh analysis
fresh:
    uv run python scripts/analyze_extensions.py full --clear-cache

# Run analysis without using cache (bypass cache)
no-cache:
    uv run python scripts/analyze_extensions.py full --no-cache

# Show cache information
cache-info:
    uv run python scripts/analyze_extensions.py report --cache-info

# Format code using ruff
format:
    uv run ruff format scripts/

# Lint code using ruff
lint:
    uv run ruff check scripts/

# Check code formatting and linting
check: format lint

# Clean up Python cache files and virtual environment
clean:
    @echo "Cleaning up Python cache files..."
    @{{ if os() == "windows" { "powershell -Command \"Get-ChildItem -Path . -Recurse -Name '__pycache__' | Remove-Item -Recurse -Force\"" } else { "find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true" } }}
    @{{ if os() == "windows" { "powershell -Command \"Get-ChildItem -Path . -Recurse -Name '*.pyc' | Remove-Item -Force\"" } else { "find . -name '*.pyc' -delete 2>/dev/null || true" } }}
    @echo "Removing virtual environment..."
    @{{ if os() == "windows" { "if exist .venv rmdir /s /q .venv" } else { "rm -rf .venv" } }}

# Update dependencies
update:
    uv lock --upgrade

# Show project status
status:
    @echo "Project: DuckDB Extensions Analysis"
    @echo "Python version:"
    @uv run python --version
    @echo ""
    @echo "Dependencies:"
    @uv tree

# Run development setup (install deps + check code)
dev-setup: install check

# === WORKFLOW RECIPES ===

# Complete workflow: database + all reports
workflow-complete: database report-all
    @echo "✅ Complete workflow finished: database saved and all reports generated"

# Fresh complete workflow (no cache): database + all reports  
workflow-fresh: database-fresh report-all
    @echo "✅ Fresh complete workflow finished: database saved and all reports generated with fresh data"

# Analysis workflow: core + community analysis, then database save
workflow-analysis: core community database
    @echo "✅ Analysis workflow finished: core + community analysis completed and saved to database"

# Reporting workflow: generate all report formats
workflow-reports: report-all
    @echo "✅ Reporting workflow finished: all report formats generated"

# Development workflow: setup + fresh analysis + reports
workflow-dev: dev-setup workflow-fresh
    @echo "✅ Development workflow finished: setup complete, fresh analysis and reports generated"

# Quick workflow: cached analysis + markdown report
workflow-quick: full report
    @echo "✅ Quick workflow finished: full analysis and markdown report generated"

# Data export workflow: database + CSV + Excel
workflow-export: database report-csv report-excel
    @echo "✅ Data export workflow finished: database and spreadsheet formats generated"

# === END WORKFLOWS ===

# Show help for common commands
help:
    @echo "DuckDB Extensions Analysis - Common Commands:"
    @echo ""
    @echo "  just install       - Install dependencies"
    @echo "  just community     - Run community extensions analysis"
    @echo "  just core          - Run core extensions analysis"
    @echo "  just full          - Run full extensions analysis (core + community)"
    @echo "  just all           - Run both analyses sequentially"
    @echo "  just report        - Generate comprehensive markdown report"
    @echo "  just fresh         - Clear cache and run fresh full analysis"
    @echo "  just database      - Save analysis to DuckDB database"
    @echo "  just query-db      - Query database with example analytics"
    @echo "  just backfill-db   - Add simulated historical data"
    @echo "  just cache-info    - Show cache statistics"
    @echo "  just check         - Format and lint code"
    @echo "  just clean         - Clean cache files and venv"
    @echo "  just status        - Show project status"
    @echo "  just dev-setup     - Setup for development"
    @echo ""
    @echo "Workflow Commands:"
    @echo "  just workflow-complete  - Complete workflow (database + all reports)"
    @echo "  just workflow-fresh     - Fresh complete workflow (no cache)"
    @echo "  just workflow-analysis  - Analysis workflow (core + community + database)"
    @echo "  just workflow-reports   - Generate all report formats"
    @echo "  just workflow-dev       - Development workflow (setup + fresh analysis)"
    @echo "  just workflow-quick     - Quick workflow (cached analysis + report)"
    @echo "  just workflow-export    - Data export workflow (database + spreadsheets)"
