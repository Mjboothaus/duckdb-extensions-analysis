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

# Run analysis (options: core, community, full)
analyze mode="full" *flags="":
    uv run python scripts/analyze_extensions.py {{mode}} {{flags}}

# Run analysis with fresh data (no cache)
analyze-fresh mode="full":
    uv run python scripts/analyze_extensions.py {{mode}} --no-cache

# === REPORTING COMMANDS ===

# Generate reports (supports --csv --excel flags)
report *flags="":
    uv run python scripts/analyze_extensions.py report {{flags}}

# Generate all report formats
report-all:
    uv run python scripts/analyze_extensions.py report --csv --excel

# === DATABASE COMMANDS ===

# Save analysis to DuckDB database
database *flags="":
    uv run python scripts/analyze_extensions.py database {{flags}}

# Query the extensions database
query:
    uv run python scripts/query_database.py

# Back-fill database with historical data (demo)
backfill:
    uv run python scripts/query_database.py backfill

# === CACHE MANAGEMENT ===

# Show cache information
cache-info:
    uv run python scripts/analyze_extensions.py report --cache-info

# Clear cache
cache-clear:
    uv run python scripts/analyze_extensions.py full --clear-cache

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
    @uv run python --version
    @echo ""
    @uv tree --depth 1

# === COMMON WORKFLOWS ===

# Complete workflow: fresh analysis + all reports + database
workflow-complete:
    just analyze-fresh full
    just report-all
    just database
    @echo "✅ Complete workflow finished"

# Quick workflow: cached analysis + markdown report  
workflow-quick:
    just analyze full
    just report
    @echo "✅ Quick workflow finished"
