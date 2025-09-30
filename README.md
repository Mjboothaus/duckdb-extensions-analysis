# DuckDB Extensions Analysis

Automated monitoring of DuckDB's extension ecosystem, tracking core and community extensions with daily reports.

## Latest Analysis

**Last Updated:** 2025-10-08 01:17:00 UTC

[![Daily Report](https://img.shields.io/badge/Daily%20Report-Active-green)](./reports/latest.md)
[![Extensions Tracked](https://img.shields.io/badge/Extensions%20Tracked-112-blue)](./reports/latest.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2025-10-08%2001:17:00%20UTC-lightgrey)](./reports/latest.md)

### Quick Summary

## Summary

| **Metric** | **Count** |
|------------|-----------|
| **Core Extensions** | 24 |
| **Community Extensions** | 88 |
| **Featured Extensions** | 54 |
| **Total Extensions** | 112 |
| **Recently Active** (≤ 30 days) | 70 |
| **Very Active** (≤ 7 days) | 25 |


---
## Core Extensions


## Reports

- **[Latest Analysis Report](./reports/latest.md)** - Complete markdown analysis
- **[CSV Data](./reports/)** - Machine-readable data for further analysis  
- **[Excel Reports](./reports/)** - Business-friendly spreadsheet format

## Quick Start

See [QUICKSTART.md](./QUICKSTART.md) for setup and usage instructions.

## Documentation

### Key Documents

- **[Extension Status Assumptions](./docs/project/EXTENSION_STATUS_ASSUMPTIONS.md)** - Comprehensive guide to how extension statuses are determined, including the manual review process and configuration-driven overrides
- **[System Architecture](./docs/project/SYSTEM_ARCHITECTURE.md)** - Technical architecture and system design
- **[Data Sources](./docs/project/duck_sources.md)** - Detailed explanation of data collection methodology
- **[SQL Documentation](./docs/SQL_QUERIES.md)** - Database schema and sample queries

### Understanding Extension Classifications

⚠️ **Important**: Extension status determinations require **manual human review**. The tool provides automated analysis and recommendations, but final classifications are stored in [`conf/extensions_metadata.toml`](./conf/extensions_metadata.toml) after human verification.

See the [Extension Status Assumptions](./docs/project/EXTENSION_STATUS_ASSUMPTIONS.md) document for complete details on:
- How core and community extensions are classified
- Data sources and assumptions made by the tool
- The role of manual review in final status determinations
- Configuration-driven status overrides

## Automation

This repository automatically runs daily analysis at 6 AM UTC via GitHub Actions.
The reports track extension status, GitHub activity, and installation health across the DuckDB ecosystem.

---
*Generated automatically by [GitHub Actions](.github/workflows/daily-extensions-report.yml)*
