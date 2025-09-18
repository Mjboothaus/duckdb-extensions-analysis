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

# Clear cache and run fresh analysis
fresh:
    uv run python scripts/analyze_extensions.py full --clear-cache

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
    @echo "  just cache-info    - Show cache statistics"
    @echo "  just check         - Format and lint code"
    @echo "  just clean         - Clean cache files and venv"
    @echo "  just status        - Show project status"
    @echo "  just dev-setup     - Setup for development"
