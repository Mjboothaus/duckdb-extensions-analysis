# DuckDB Extensions Analysis - Beta Release v0.1.0

**🦆 Comprehensive DuckDB Extension Ecosystem Monitoring (Beta)**

We're excited to announce the beta release of the DuckDB Extensions Analysis tool - an automated monitoring system that tracks and analyses the entire DuckDB extension ecosystem.

## What's New

- **📊 Daily Automated Reports**: Complete analysis of 107+ DuckDB extensions (24 core + 83 community)
- **🌐 Live GitHub Pages Dashboard**: Beautiful, responsive web interface at [mjboothaus.github.io/duckdb-extensions-analysis](https://mjboothaus.github.io/duckdb-extensions-analysis/)
- **📈 Multiple Output Formats**: Reports in Markdown, CSV, and Excel formats
- **🔍 GitHub Integration**: Tracks repository activity, issues, and development health
- **⚡ Performance Monitoring**: Extension installation validation and URL health checks

## Beta Notice

⚠️ **This is a beta release** - We're actively improving the tool and there may be occasional errors or inconsistencies in the data. Your feedback and contributions are welcome as we work toward a stable release.

## Key Features

- **Extension Discovery**: Automatically discovers and categorises core vs community extensions
- **Health Monitoring**: Validates installation URLs and tracks broken links
- **Activity Analysis**: Monitors GitHub activity, commit frequency, and issue status
- **Trend Tracking**: Historical data collection for ecosystem growth analysis
- **Multi-format Reporting**: Choose from web, CSV, or Excel outputs for different use cases

## Quick Start

```bash
git clone https://github.com/Mjboothaus/duckdb-extensions-analysis.git
cd duckdb-extensions-analysis
uv sync
uv run scripts/cli.py report generate
```

## Live Dashboard

Visit our automated dashboard for the latest ecosystem insights: **https://mjboothaus.github.io/duckdb-extensions-analysis/**

---

*Made with love and care at [DataBooth](https://www.databooth.com.au)*