# DuckDB Extensions Analysis

Automated monitoring of DuckDB's extension ecosystem, tracking core and community extensions with daily reports.

## Latest Analysis

**Last Updated:** 2025-09-27 00:20:01 UTC

[![Daily Report](https://img.shields.io/badge/Daily%20Report-Active-green)](./reports/latest.md)
[![Extensions Tracked](https://img.shields.io/badge/Extensions%20Tracked-107-blue)](./reports/latest.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2025-09-27%2000:20:01%20UTC-lightgrey)](./reports/latest.md)

### Quick Summary

## Summary

| **Metric** | **Count** |
|------------|-----------|
| **Core Extensions** | 24 |
| **Community Extensions** | 83 |
| **Featured Extensions** | 42 |
| **Total Extensions** | 107 |
| **Recently Active** (≤ 30 days) | 59 |
| **Very Active** (≤ 7 days) | 49 |


---
## Core Extensions


## Reports

- **[Latest Analysis Report](./reports/latest.md)** - Complete markdown analysis
- **[CSV Data](./reports/)** - Machine-readable data for further analysis  
- **[Excel Reports](./reports/)** - Business-friendly spreadsheet format

## Quick Start

See [QUICKSTART.md](./QUICKSTART.md) for setup and usage instructions.

## Repository Structure

```
├── scripts/           # Analysis and reporting tools
├── reports/           # Generated reports (latest.md is the main report)
├── _site/             # Generated HTML site
├── blog/              # Blog posts and documentation
├── docs/              # Project documentation
├── deprecated/        # Deprecated code (kept for reference)
├── data/              # Generated databases
├── sql/               # Database schema and queries
└── conf/              # Configuration files
```

## Documentation

- **Setup & Usage**: [QUICKSTART.md](./QUICKSTART.md)
- **Contributing**: [CONTRIBUTING.md](./CONTRIBUTING.md) 
- **Data Sources**: [docs/project/duck_sources.md](./docs/project/duck_sources.md)
- **GitHub Actions**: [docs/project/GITHUB_ACTION.md](./docs/project/GITHUB_ACTION.md)
- **Release Notes**: [RELEASE_NOTES.md](./RELEASE_NOTES.md)

## Blog Posts

- **Live Blog Posts** (symbolic links to published posts):
  - [Post 1: Navigating Extension Updates](./blog/post1_navigating_extension_updates_LIVE.md)
  - [Post 2: Ecosystem Analysis Tool](./blog/post2_ecosystem_analysis_tool_LIVE.md)

## Automation

This repository automatically runs daily analysis at 6 AM UTC via GitHub Actions.
The reports track extension status, GitHub activity, and installation health across the DuckDB ecosystem.

---
*Generated automatically by [GitHub Actions](.github/workflows/daily-extensions-report.yml)*
