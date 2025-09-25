# Cross-platform justfile for DuckDB Extensions Analysis
# Simplified version with core commands only

# Default recipe - show available commands
default:
    @just --list

# === SETUP & INSTALLATION ===

# Install dependencies using uv
install:
    uv sync

# Update dependencies
update:
    uv lock --upgrade

# Set up GitHub token from gh CLI
setup-token:
    @echo "Setting up GitHub token from gh CLI..."
    @gh auth token > .env.tmp
    @echo "GITHUB_TOKEN=$(cat .env.tmp)" > .env
    @rm .env.tmp
    @echo "✅ GitHub token saved to .env file"

# === ANALYSIS COMMANDS ===

# Run analysis (options: core, community, all)
analyze mode="all" *flags="":
    uv run scripts/cli.py analyze {{mode}} {{flags}}

# Run analysis with fresh data (no cache)
analyze-fresh mode="all":
    uv run scripts/cli.py analyze {{mode}} --cache-hours 0

# === REPORTING COMMANDS ===

# Generate markdown report (add --with-issues to include GitHub issues analysis)
report *flags="":
    uv run scripts/cli.py report generate {{flags}}

# Generate all report formats
report-all:
    uv run scripts/cli.py report generate --format markdown --format csv --format excel

# Generate all report formats with fresh data (no cache)
report-all-fresh:
    uv run scripts/cli.py report generate --format markdown --format csv --format excel --cache-hours 0

# Quick report (same as default behavior now)
report-quick:
    uv run scripts/cli.py quick

# === DATABASE COMMANDS ===

# Save analysis to DuckDB database
database *flags="":
    uv run scripts/cli.py database save {{flags}}

# Query the extensions database
query:
    uv run scripts/query_database.py

# Back-fill database with historical data (demo)
backfill:
    uv run scripts/query_database.py backfill

# === CACHE MANAGEMENT ===

# Show cache information
cache-info:
    uv run scripts/cli.py cache info

# Clear cache
cache-clear:
    uv run scripts/cli.py cache clear

# === DEVELOPMENT COMMANDS ===

# Format and lint code
check:
    uv run ruff format scripts/ conf/
    uv run ruff check scripts/ conf/

# Clean up cache and build files
clean:
    @echo "Cleaning up cache and build files..."
    @{{ if os() == "windows" { "powershell -Command \"Get-ChildItem -Path . -Recurse -Name '__pycache__' | Remove-Item -Recurse -Force\"" } else { "find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true" } }}
    @{{ if os() == "windows" { "powershell -Command \"Get-ChildItem -Path . -Recurse -Name '*.pyc' | Remove-Item -Force\"" } else { "find . -name '*.pyc' -delete 2>/dev/null || true" } }}
    @{{ if os() == "windows" { "if exist .venv rmdir /s /q .venv" } else { "rm -rf .venv" } }}

# Show project status
status:
    @echo "Project: DuckDB Extensions Analysis"
    @uv run --version
    @echo ""
    @uv tree --depth 1

# === COMMON WORKFLOWS ===

# Complete workflow: fresh analysis + all reports + database
workflow-complete:
    just analyze-fresh all
    just report-all
    just database
    @echo "✅ Complete workflow finished"

# Quick workflow: cached analysis + markdown report  
workflow-quick:
    just analyze all
    just report
    @echo "✅ Quick workflow finished"

# Fastest workflow: default report (no GitHub issues)
workflow-fastest:
    just report-quick
    @echo "✅ Fastest workflow finished"
