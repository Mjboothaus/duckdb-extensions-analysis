# 🚀 DuckDB Extensions Analysis - Quickstart Guide

Monitor DuckDB's extension ecosystem with automated analysis and reporting.

## ⚡ Quick Setup

```bash
# Clone and setup
git clone <repository-url>
cd duckdb-extensions-analysis
just install

# Optional: Setup GitHub authentication for better rate limits
just setup-auth
```

## 🔄 Essential Commands

```bash
# Complete workflow (recommended)
just workflow                    # Analyze → Report → Database

# Individual steps
just report-all                 # Generate MD, CSV, Excel reports
just report-all-issues          # Include GitHub issues analysis
just analyze all                # Run analysis only

# Fresh data (bypasses cache)
just workflow-fresh             # Complete analysis with latest data
```

## 📋 Output Files

- **`reports/latest.md`** - Human-readable analysis report
- **`reports/*.csv`** - Data for analysis tools  
- **`reports/*.xlsx`** - Multi-sheet Excel reports
- **`data/extensions.duckdb`** - Queryable database

## 📊 What's Analyzed

- **107 Total Extensions** (24 core + 83 community)
- Extension status, GitHub activity, installation health
- **264 GitHub issues** tracked across extension repositories
- **URL Validation** - All repository and documentation URLs checked automatically

## 📊 Understanding Reports

**Core Extensions (24)** - Built into DuckDB, updated with releases
**Community Extensions (83)** - Third-party, independent development
**GitHub Issues** - Installation problems, platform issues, health indicators
**URL Validation** - Broken links show as ~~strikethrough~~ with **NOT FOUND** message

## 🔧 Advanced Features

```bash
# Cache management (speeds up repeated runs)
just cache-stash              # Save current cache
just cache-restore            # Restore saved cache

# Specific analysis
just analyze core             # Core extensions only
just analyze community        # Community extensions only
just query                    # Database analytics
```

## 🤖 Automation

For daily monitoring, see GitHub Actions setup in the main README.

## 📊 Sample Output

```
ANALYSIS SUMMARY: DuckDB v1.4.0 | Core: 24 | Community: 83 | Total: 107
Core Extensions: 24 (100% active)
Community Extensions: 83 (76 active, 5 discontinued, 2 issues)
GitHub Issues: 264 issues tracked across extension repositories
```

Ready to monitor the DuckDB extension ecosystem! 🚀
