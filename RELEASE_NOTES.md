# DuckDB Extensions Analysis - Release Notes

## v0.2.0 - January 2026 Update

*Released: January 28, 2026*

### ✨ New Features

**🔢 GitHub Tags API Integration**
- Added GitHub Tags API as release source to catch newly released DuckDB versions immediately
- Fixes delay in detecting releases not yet in official CSV (e.g., v1.4.4)
- Priority: CSV (full metadata) → GitHub Tags (gap filling) → Release calendar (upcoming)

**📊 Consolidated Community Extensions Table**
- Replaced multiple activity-based tables with single sortable table
- Added Activity column with visual indicators (🔥 Very Active, ✅ Active, 🟡 Stable, 🟠 Stale)
- Numeric prefixes (1-4) for proper sorting by activity level
- Initial alphabetical sort for logical row numbering

**🌐 Interactive DataTables**
- Sortable, searchable, paginated tables in web interface
- Default 20 entries per page (10/20/50/100/All options)
- Smart column sorting for Status, Stars, Activity, and dates
- Responsive design for mobile and tablet

**📈 Analytics Integration**
- Added Umami Cloud for privacy-focused web analytics
- Cookieless tracking, GDPR/CCPA compliant
- Tracks page views, referrers, devices without personal data

**🔍 SEO & Discoverability**
- Added comprehensive keywords and topics to reports and README
- Improved search engine visibility for extension ecosystem queries

### 🐛 Fixes

**🔗 Repository Links**
- Fixed incorrect GitHub repo links (was pointing to duckdb/duckdb, now correct repo)
- Absolute URLs for documentation files (DATA_QUALITY_LIMITATIONS.md, HISTORICAL_PRE_1_0_RELEASES.md)

**📝 Report Formatting**
- Fixed bullet point formatting in data quality section
- Removed extra `---` separators for cleaner layout
- Improved markdown rendering consistency

**💾 Caching Improvements**
- Enabled GitHub Actions caching for `.cache` and DuckDB database
- Reduced workflow runtime by persisting analysis artifacts
- Cache restoration on subsequent runs for faster analysis

### 📚 Documentation

- Created `docs/DATA_QUALITY_LIMITATIONS.md` - comprehensive data quality notes
- Created `ANALYTICS.md` - analytics implementation documentation  
- Updated blog posts with current ecosystem statistics (177 extensions, growth from 107)
- Clarified trend tracking plans and historical data availability
- Simplified issue reporting instructions

### 📊 Ecosystem Growth

- **177 total extensions** (from 107 in Sept 2025)
- **27 core extensions** (from 24)
- **150 community extensions** (from 83)
- Nearly doubled in 4 months!

### 🛠️ Technical Improvements

- Optimised table rendering and column definitions
- Enhanced GitHub API error handling and rate limiting
- Improved release detection reliability
- Better handling of closed-source extensions (motherduck, vortex)

---

## v0.1.0 - Beta Release

*Released: September 2025*

## Overview

The DuckDB Extensions Analysis tool provides comprehensive monitoring and analysis of the DuckDB extension ecosystem. This beta release introduces automated daily reporting, web dashboard, and multi-format data exports to help developers, researchers, and users understand the growing DuckDB extension landscape.

## 🆕 What's New in Beta v0.1.0

### Core Features

**📊 Comprehensive Extension Analysis**
- Monitors 107+ DuckDB extensions (24 core, 83 community)
- Categorises extensions by type: core, community, and featured
- Tracks extension metadata, documentation, and installation status

**🌐 Live Web Dashboard**
- Beautiful, responsive GitHub Pages site
- Real-time ecosystem statistics and trends
- Professional HTML rendering with GitHub-like styling
- Mobile-optimised interface
- Available at: https://mjboothaus.github.io/duckdb-extensions-analysis/

**🤖 Automated Reporting Pipeline**
- Daily automated reports via GitHub Actions (6 AM UTC)
- Multiple output formats: Markdown, CSV, Excel
- Automatic repository updates and deployments
- Historical data preservation and archiving

**🔍 Extension Health Monitoring**
- URL validation for installation endpoints
- Documentation link verification
- GitHub repository activity tracking
- Issue and development health assessment

**📈 GitHub Integration**
- Repository statistics (stars, forks, activity)
- Commit frequency and recency analysis
- Issue tracking and resolution patterns
- Contributor activity monitoring

### Technical Implementation

**🛠️ Modern Python Stack**
- Built with Python 3.13+ and `uv` for fast dependency management
- DuckDB for data processing and analysis
- GitHub API integration for repository data
- Professional CLI interface with rich output formatting

**📋 Data Quality**
- Robust error handling and validation
- Progress tracking for long-running operations
- Comprehensive logging and debugging capabilities
- Fallback mechanisms for API failures

**🔧 Extensible Architecture**
- Modular design for easy feature additions
- Template-based report generation
- Configurable data sources and analysis parameters
- Clear separation of concerns for maintenance

## 🚧 Beta Limitations & Known Issues

This is a beta release with known limitations that we're actively addressing:

### Data Quality
- **URL Validation**: Some false positives/negatives in broken link detection
- **Extension Categorisation**: Manual curation still needed for some edge cases
- **Historical Data**: Limited baseline for trend analysis (building over time)

### Reporting
- **Community Extension Tables**: Currently split across multiple tables, consolidation planned
- **Sorting Functionality**: Tables not yet sortable in web interface
- **Mobile Experience**: Some table layouts could be improved for smaller screens

### Technical
- **Rate Limiting**: GitHub API rate limits may occasionally delay updates
- **Performance**: Large dataset processing could be optimised further
- **Error Recovery**: Some edge cases in data collection need refinement

## 🔮 Upcoming Features (Roadmap)

### Short Term (v0.2.0)
- **Interactive Tables**: Sortable columns and filtering in web interface
- **Unified Community Table**: Merge separate community extension tables
- **Database Views**: Implement DuckDB views for easier data querying
- **Enhanced Error Handling**: Better resilience to API failures

### Medium Term (v0.3.0)
- **Trend Analysis**: Historical comparison and growth metrics
- **Extension Search**: Search and filter functionality
- **Performance Metrics**: Installation success rates and timing
- **Export Improvements**: Additional format support (JSON, Parquet)

### Long Term (v1.0.0)
- **Real-time Updates**: More frequent refresh capabilities
- **Custom Dashboards**: User-configurable views and metrics
- **API Access**: RESTful API for programmatic access
- **Alerting System**: Notifications for extension changes

## 🛠️ Installation & Usage

### Quick Start
```bash
# Clone repository
git clone https://github.com/Mjboothaus/duckdb-extensions-analysis.git
cd duckdb-extensions-analysis

# Install dependencies
uv sync

# Generate reports
uv run scripts/cli.py report generate

# View reports
open reports/latest.md
```

### Advanced Usage
```bash
# Generate specific formats
uv run scripts/cli.py report generate --format markdown --format csv --format excel

# Include GitHub issues analysis
uv run scripts/cli.py report generate --with-issues

# Force refresh of cached data
uv run scripts/cli.py report generate --force-refresh
```

## 📊 Current Ecosystem Statistics

As of the beta release:
- **Total Extensions**: 107
- **Core Extensions**: 24 (built-in to DuckDB)
- **Community Extensions**: 83 (external repositories)
- **Featured Extensions**: 41 (highlighted by DuckDB team)
- **Recently Active**: 59 (activity within 30 days)
- **Very Active**: 50 (activity within 7 days)

## 🤝 Contributing

We welcome contributions! This beta release is our foundation for building a comprehensive DuckDB ecosystem analysis tool.

**How to Help:**
- Report bugs and inconsistencies in extension data
- Suggest improvements to categorisation and analysis
- Contribute code improvements and new features
- Share feedback on the web interface and usability

**Areas Needing Attention:**
- Extension metadata accuracy and completeness
- URL validation logic refinement
- Performance optimisation for large datasets
- User experience improvements

## 📞 Support & Feedback

- **Issues**: Report bugs via [GitHub Issues](https://github.com/Mjboothaus/duckdb-extensions-analysis/issues)
- **Discussions**: Feature requests and general discussion welcome
- **Email**: Contact via [DataBooth](https://www.databooth.com.au) for consulting needs

## 🙏 Acknowledgments

Special thanks to:
- The DuckDB team for building an amazing analytical database
- The DuckDB community for creating a rich extension ecosystem
- GitHub for providing excellent CI/CD and hosting infrastructure

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

*Made with love and care at [DataBooth](https://www.databooth.com.au)*

*This beta release represents our commitment to transparency and open-source contribution to the DuckDB community. We're excited to iterate and improve based on your feedback.*