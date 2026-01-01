# DuckDB Extensions Analysis - Simplified justfile

# Show available commands
default:
    @just --list

# === SETUP ===

# Install dependencies
install:
    uv sync

# Set up GitHub authentication
setup-auth:
    @echo "Setting up GitHub authentication..."
    @gh auth token > .env.tmp
    @echo "GITHUB_TOKEN=$(cat .env.tmp)" > .env
    @rm .env.tmp
    @echo "✅ GitHub token saved to .env"

# === ANALYSIS ===

# Analyze extensions (core | community | all)
analyze mode="all":
    uv run scripts/cli.py analyze {{mode}}

# Analyze with fresh data (bypass cache)
fresh mode="all":
    uv run scripts/cli.py analyze {{mode}} --cache-hours 0

# === REPORTING ===

# Generate markdown report
report:
    uv run scripts/cli.py report generate

# Generate report with GitHub issues (slower)
report-issues:
    uv run scripts/cli.py report generate --with-issues

# Generate all formats (markdown, CSV, Excel)
report-all:
    uv run scripts/cli.py report generate --format markdown --format csv --format excel

# Generate all formats with GitHub issues
report-all-issues:
    uv run scripts/cli.py report generate --format markdown --format csv --format excel --with-issues

# Generate HTML site from latest report
site:
    uv run scripts/build_report_site.py

# === DATABASE ===

# Save analysis to database
database:
    uv run scripts/cli.py database save

# Query database with analytics
query:
    uv run scripts/query_database.py

# === CACHE ===

# Show cache info
cache-info:
    uv run scripts/cli.py cache info

# Clear cache
cache-clear:
    uv run scripts/cli.py cache clear

# Stash current cache (save it with timestamp)
cache-stash:
    #!/usr/bin/env bash
    if [ -d ".cache" ]; then
        timestamp=$(date +"%Y%m%d_%H%M%S")
        cache_backup=".cache_stash_${timestamp}"
        echo "📦 Stashing current cache to: ${cache_backup}"
        cp -r .cache "${cache_backup}"
        echo "✅ Cache stashed successfully"
        echo "📊 Stashed cache info:"
        du -sh "${cache_backup}" 2>/dev/null || echo "Could not determine size"
    else
        echo "⚠️  No cache directory found to stash"
    fi

# List all stashed caches
cache-list-stashes:
    #!/usr/bin/env bash
    echo "📦 Available cache stashes:"
    if ls -d .cache_stash_* 2>/dev/null; then
        echo ""
        echo "Size breakdown:"
        du -sh .cache_stash_* 2>/dev/null | sort -k2
    else
        echo "No cache stashes found"
    fi

# Restore cache from most recent stash
cache-restore:
    #!/usr/bin/env bash
    latest_stash=$(ls -d .cache_stash_* 2>/dev/null | sort | tail -1)
    if [ -n "$latest_stash" ]; then
        echo "🔄 Restoring cache from: $latest_stash"
        if [ -d ".cache" ]; then
            echo "⚠️  Current cache exists, creating backup first..."
            timestamp=$(date +"%Y%m%d_%H%M%S")
            mv .cache ".cache_backup_${timestamp}"
        fi
        cp -r "$latest_stash" .cache
        echo "✅ Cache restored successfully"
        echo "📊 Restored cache info:"
        du -sh .cache 2>/dev/null || echo "Could not determine size"
    else
        echo "❌ No cache stashes found to restore"
    fi

# Restore cache from specific stash
cache-restore-from stash_name:
    #!/usr/bin/env bash
    stash_path=".cache_stash_{{stash_name}}"
    if [ -d "$stash_path" ]; then
        echo "🔄 Restoring cache from: $stash_path"
        if [ -d ".cache" ]; then
            echo "⚠️  Current cache exists, creating backup first..."
            timestamp=$(date +"%Y%m%d_%H%M%S")
            mv .cache ".cache_backup_${timestamp}"
        fi
        cp -r "$stash_path" .cache
        echo "✅ Cache restored successfully"
    else
        echo "❌ Stash not found: $stash_path"
        echo "Available stashes:"
        just cache-list-stashes
    fi

# Clean up old cache stashes (keep only the 5 most recent)
cache-cleanup-stashes:
    #!/usr/bin/env bash
    echo "🧹 Cleaning up old cache stashes (keeping 5 most recent)..."
    stashes=($(ls -d .cache_stash_* 2>/dev/null | sort))
    total_stashes=${#stashes[@]}
    if [ $total_stashes -gt 5 ]; then
        keep_count=5
        remove_count=$((total_stashes - keep_count))
        echo "Found $total_stashes stashes, removing $remove_count oldest ones"
        for ((i=0; i<remove_count; i++)); do
            echo "Removing: ${stashes[i]}"
            rm -rf "${stashes[i]}"
        done
        echo "✅ Cleanup complete"
    else
        echo "Only $total_stashes stashes found, no cleanup needed"
    fi

# === UTILITIES ===

# Validate release history table against GitHub releases
validate-releases:
    uv run scripts/validate_release_history.py

# Detect deprecated extensions by analyzing repositories
deprecation:
    #!/usr/bin/env bash
    echo "🔍 Analyzing extension repositories for deprecation indicators..."
    echo "This may take a few minutes as we scan all community extensions..."
    timestamp=$(date +"%Y%m%d_%H%M%S")
    output_file="reports/deprecation_analysis_${timestamp}.md"
    
    # Try to get GitHub token from various sources
    if [ -z "$GITHUB_TOKEN" ]; then
        if command -v gh >/dev/null 2>&1; then
            echo "📝 Getting GitHub token from gh CLI..."
            export GITHUB_TOKEN=$(gh auth token 2>/dev/null)
        elif [ -f ".env" ]; then
            echo "📝 Loading GitHub token from .env file..."
            source .env
        fi
    fi
    
    if [ -z "$GITHUB_TOKEN" ]; then
        echo "⚠️  No GitHub token found. Analysis will proceed with rate limits."
        echo "   Run 'gh auth login' or set GITHUB_TOKEN environment variable for better API limits."
    else
        echo "✅ Using GitHub token for enhanced API limits"
    fi
    
    uv run scripts/detect_deprecated_extensions.py --format markdown --output "$output_file"
    echo "📄 Report saved to: $output_file"
    echo "🎯 Review the report to identify extensions that should be marked as deprecated in conf/extensions_metadata.toml"

# Detect deprecated extensions and output to console
deprecation-quick:
    #!/usr/bin/env bash
    echo "🔍 Quick deprecation analysis (output to console)..."
    
    # Try to get GitHub token from gh CLI
    if [ -z "$GITHUB_TOKEN" ] && command -v gh >/dev/null 2>&1; then
        export GITHUB_TOKEN=$(gh auth token 2>/dev/null)
    fi
    
    if [ -n "$GITHUB_TOKEN" ]; then
        echo "✅ Using GitHub token for enhanced API limits"
    else
        echo "⚠️  No GitHub token found - proceeding with rate limits"
        echo "   Run 'gh auth login' for better API limits"
    fi
    
    uv run scripts/detect_deprecated_extensions.py --format markdown

# Detect deprecated extensions in JSON format for processing
deprecation-json:
    #!/usr/bin/env bash
    timestamp=$(date +"%Y%m%d_%H%M%S")
    output_file="reports/deprecation_analysis_${timestamp}.json"
    
    # Try to get GitHub token from gh CLI
    if [ -z "$GITHUB_TOKEN" ] && command -v gh >/dev/null 2>&1; then
        export GITHUB_TOKEN=$(gh auth token 2>/dev/null)
    fi
    
    uv run scripts/detect_deprecated_extensions.py --format json --output "$output_file"
    echo "📄 JSON report saved to: $output_file"

# Detect deprecated extensions in CSV format for spreadsheet analysis
deprecation-csv:
    #!/usr/bin/env bash
    timestamp=$(date +"%Y%m%d_%H%M%S")
    output_file="reports/deprecation_analysis_${timestamp}.csv"
    
    # Try to get GitHub token from gh CLI
    if [ -z "$GITHUB_TOKEN" ] && command -v gh >/dev/null 2>&1; then
        export GITHUB_TOKEN=$(gh auth token 2>/dev/null)
    fi
    
    uv run scripts/detect_deprecated_extensions.py --format csv --output "$output_file"
    echo "📄 CSV report saved to: $output_file"

# Format and lint code
check:
    uv run ruff format scripts/ conf/ src/
    uv run ruff check scripts/ conf/ src/

# Check GitHub token status and API rate limits
check-token:
    uv run scripts/check_github_token.py

# Check for GitHub secondary rate limit penalties
check-penalty:
    uv run scripts/check_rate_limit_penalty.py

# Show project status
status:
    @echo "📊 DuckDB Extensions Analysis"
    @echo "Version:" $(uv run scripts/cli.py --version | tail -1)
    @echo "Cache:" $(uv run scripts/cli.py --cache-info | grep "Cache size" || echo "No cache info")
    @echo "Database:" $(if [ -f data/extensions.duckdb ]; then echo "✅ Present"; else echo "❌ Missing"; fi)

# === WORKFLOWS ===

# Complete analysis and reporting (cached)
workflow:
    just analyze all
    just report-all
    just database
    @echo "✅ Workflow complete"

# Complete analysis and reporting (fresh data)
workflow-fresh:
    just fresh all
    just report-all
    just database
    @echo "✅ Fresh workflow complete"

# Complete analysis and reporting with GitHub issues
workflow-issues:
    just analyze all
    just report-all-issues
    just database
    @echo "✅ Issues workflow complete"

# Complete workflow including HTML site generation
workflow-site:
    just analyze all
    just report-all
    just site
    just database
    @echo "✅ Site workflow complete"
