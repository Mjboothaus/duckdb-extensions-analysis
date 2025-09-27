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

# Format and lint code
check:
    uv run ruff format scripts/ conf/ src/
    uv run ruff check scripts/ conf/ src/

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
