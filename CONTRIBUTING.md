# Contributing to DuckDB Extensions Analysis

Thank you for your interest in contributing to the DuckDB Extensions Analysis tool! This guide provides everything you need to understand, use, and improve the project.

## 📖 **Project Overview**

This tool provides comprehensive analysis of the DuckDB extensions ecosystem, tracking both **core extensions** (built into DuckDB) and **community extensions** (third-party contributions). It generates detailed reports, maintains historical data, and offers quick status checks.

### **Key Capabilities**
- 🔍 **Extension Discovery**: Automatically finds and analyzes 24 core + 80+ community extensions
- 📊 **Multi-Format Reports**: Generates Markdown, CSV, Excel, and HTML reports
- 🕰️ **Historical Tracking**: Maintains versioned data with DuckDB release correlation
- ⚡ **Quick Status Checks**: Fast freshness checks with `--as-of-date` support
- 🎯 **Featured Detection**: Identifies prominent extensions from DuckDB documentation
- 🗄️ **Database Storage**: Stores analysis results in queryable DuckDB database

---

## 🚀 **Quick Start**

### **Prerequisites**
- **Python 3.13+** 
- **[uv](https://github.com/astral-sh/uv)** for dependency management
- **[just](https://github.com/casey/just)** for task automation (recommended)
- **GitHub Token** (optional but recommended for higher API limits)

### **Installation**
```bash
# Clone and setup
git clone <repository-url>
cd duckdb-extensions-analysis
just install  # or: uv sync

# Optional: Set GitHub token for higher rate limits
export GITHUB_TOKEN=$(gh auth token)  # if using gh CLI
# or: export GITHUB_TOKEN=your_token_here
```

### **Basic Usage**
```bash
# Quick report generation
just report                           # Generate markdown report
just report-all                       # All formats (MD, CSV, Excel)

# Extension analysis
just analyze core                     # Core extensions only
just analyze community                # Community extensions only  
just analyze all                      # Full analysis

# Status checks
uv run scripts/cli.py status core                    # Core freshness
uv run scripts/cli.py status community h3 prql      # Specific extensions
uv run scripts/cli.py status all --as-of-date 2025-09-16  # Historical check

# Database operations
just database                         # Save to database
just query-db                         # Interactive analysis
```

---

## 🏗️ **Architecture Overview**

### **Project Structure**
```
duckdb-extensions-analysis/
├── src/
│   ├── analyzers/           # Core analysis modules
│   │   ├── orchestrator.py      # Main coordination
│   │   ├── core_analyzer.py     # Core extensions analysis
│   │   ├── community_analyzer.py # Community extensions analysis
│   │   ├── github_api.py        # GitHub API client
│   │   ├── report_generator.py  # Report generation
│   │   └── database_manager.py  # Database operations
│   └── templates.py         # Jinja2 template engine
├── templates/               # Template system
│   ├── config/             # TOML configuration files
│   ├── components/         # Reusable template components
│   ├── reports/            # Main report templates
│   └── formats/            # Format-specific templates
├── conf/                   # Application configuration
├── scripts/                # CLI interface
└── reports/                # Generated reports
```

### **Key Components**

#### **1. Template System** 🎨
The tool uses **Jinja2 + TOML** for configurable, maintainable reports:

- **Templates**: `templates/reports/full_analysis.md.j2`
- **Components**: `templates/components/*.md.j2` (reusable sections)
- **Configuration**: `templates/config/*.toml` (layouts, formatting, URLs)
- **Custom Filters**: Date formatting, status badges, number formatting

#### **2. Analysis Pipeline** ⚙️
```
Data Sources → Analyzers → Template Engine → Reports + Database
```

- **Core Extensions**: Discovered from DuckDB documentation + GitHub commits
- **Community Extensions**: Fetched from community registry + individual repos
- **GitHub API**: Repository metadata, activity, stars, releases
- **Caching**: Intelligent caching with configurable TTL

#### **3. Data Flow** 📊
1. **Discovery**: Find extensions from authoritative sources
2. **Analysis**: Gather metadata, activity, and status information  
3. **Processing**: Clean, enrich, and standardize data
4. **Output**: Generate reports via templates + save to database
5. **Historical**: Maintain versioned records for trend analysis

---

## 🛠️ **Development Workflow**

### **Setting Up Development Environment**
```bash
# Development dependencies
just install
just check           # Format and lint code

# Run tests (when available)
just test            # pytest

# Development commands
just fresh           # Clear cache and run fresh analysis
just no-cache        # Run analysis bypassing cache
just status          # Show project status
```

### **Code Quality**
- **Formatter**: `ruff format`
- **Linter**: `ruff check`
- **Type Checking**: `mypy` (future)
- **Standards**: Follow existing patterns and PEP 8

### **Testing Changes**
```bash
# Test core functionality
uv run scripts/cli.py analyze core --cache-hours 1
uv run scripts/cli.py status core

# Test template changes
uv run scripts/cli.py report generate --format markdown

# Test with different date contexts
uv run scripts/cli.py status all --as-of-date 2025-09-16 h3 prql
```

---

## 🎯 **Contributing Areas**

### **🐛 Bug Fixes & Issues**
- Extension discovery accuracy
- GitHub API rate limit handling
- Template rendering edge cases
- Data quality improvements

### **✨ New Features**
- **Output Formats**: HTML reports, JSON exports, dashboards
- **Analysis Modes**: Performance metrics, dependency graphs, security scanning
- **Integrations**: CI/CD workflows, automated monitoring
- **Visualization**: Charts, graphs, trend analysis

### **🎨 Template Improvements**
The template system makes customization easy:

```bash
# Template files
templates/config/report_templates.toml    # Report structures
templates/config/table_configs.toml       # Table layouts
templates/components/                      # Reusable sections
```

**Common Template Tasks**:
- Add new report sections
- Customize table formatting
- Create new output formats
- Improve visual design

### **📊 Data Enhancement**
- Extension categorization and tagging
- Dependency tracking between extensions  
- Performance benchmarking data
- Security vulnerability scanning
- Extension usage analytics

### **⚙️ Configuration & Ops**
- Docker containerization
- GitHub Actions workflows  
- Monitoring and alerting
- Database optimization
- Caching strategies

---

## 📋 **Contribution Guidelines**

### **Before Contributing**
1. **Check existing issues** and discussions
2. **Open an issue** for major changes to discuss approach
3. **Fork the repository** and create a feature branch
4. **Follow existing code patterns** and architecture

### **Making Changes**
1. **Keep changes focused** - one feature/fix per PR
2. **Add tests** for new functionality (when test framework exists)
3. **Update documentation** if changing APIs or usage
4. **Follow commit message format**: `feat:`, `fix:`, `docs:`, etc.
5. **Test thoroughly** with different scenarios

### **Pull Request Process**
1. **Ensure CI passes** (linting, formatting, tests)
2. **Provide clear description** of changes and rationale
3. **Include examples** of new functionality
4. **Reference related issues** if applicable
5. **Respond to review feedback** promptly

### **Code Style**
- **Python**: PEP 8 compliant, formatted with `ruff`
- **Documentation**: Clear docstrings, type hints
- **Config**: TOML for configuration, YAML for CI
- **Templates**: Consistent Jinja2 patterns

---

## 🔧 **Extending the Tool**

### **Adding New Extensions**
Special extensions (like DuckLake) can be configured in:
```toml
# templates/config/special_extensions.toml
[extensions.my_extension]
name = "my_extension"
special_handling = true
repositories = [...]
releases = {...}
```

### **Creating New Report Types**
1. **Add template**: `templates/reports/my_report.md.j2`
2. **Configure**: Add to `templates/config/report_templates.toml`
3. **Update CLI**: Add command option in `scripts/cli.py`

### **Custom Analysis**
Extend analyzers in `src/analyzers/`:
```python
class MyAnalyzer(BaseAnalyzer):
    async def analyze(self) -> List[ExtensionInfo]:
        # Custom analysis logic
        pass
```

### **Database Queries**
Add custom analytics in `scripts/query_database.py` or create new analysis scripts.

---

## 🎯 **Current Priorities**

### **High Priority**
- [ ] Complete hardcoded URL migration to configuration
- [ ] HTML report generation
- [ ] Performance optimization for large datasets
- [ ] Comprehensive test suite

### **Medium Priority**  
- [ ] Extension dependency analysis
- [ ] Security vulnerability scanning
- [ ] Automated release workflows
- [ ] Extension categorization system

### **Future Ideas**
- [ ] Web dashboard interface
- [ ] Real-time monitoring
- [ ] Extension recommendation engine
- [ ] Community contribution metrics

---

## 📞 **Getting Help**

- **Documentation**: Check README.md for detailed usage
- **Issues**: Open GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Code**: Review existing code for patterns and best practices

## 📜 **License & Attribution**

This project welcomes contributions under the existing license terms. By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Happy Contributing!** 🦆✨

*The DuckDB Extensions Analysis tool is a community-driven project. Every contribution, no matter how small, helps make the DuckDB ecosystem more transparent and accessible to everyone.*