# Hardcoded URLs and Strings Audit

## Current State Summary

### ✅ **Already Configurable**
- Core extension URLs and patterns (via `extensions_metadata.toml`)
- Extension metadata handling (via TOML configuration)
- GitHub API endpoints (via main config)
- Report templates (now via Jinja2 templates)

### ❌ **Still Hardcoded - Needs Migration**

#### 1. **Community Analyzer URLs** (`src/analyzers/community_analyzer.py`)
```python
# Lines 101, 106-108, 112
"https://github.com/duckdb/community-extensions/tree/main/extensions/{ext_name}"
"https://github.com/{repo}"  
"https://github.com/{repo}/issues"
"https://github.com/{repo}/releases"
"https://duckdb.org/docs/extensions/community_extensions.html#{ext_name}"
```

#### 2. **Report Generator URLs** (`src/analyzers/report_generator.py`)
```python
# Multiple hardcoded documentation and GitHub URLs
# Lines 88, 107, 109, 126, 133, 151, 265, 276, 281, 392
Various duckdb.org and github.com URLs in templates and links
```

#### 3. **Core Analyzer** (`src/analyzers/core_analyzer.py`)
```python
# Line 81
"https://duckdb.org" (base URL construction)
```

#### 4. **Installation Tester** (`src/analyzers/installation_tester.py`) 
```python
# Line 136
"https://duckdb.org/docs/extensions/overview.html"
```

#### 5. **GitHub Issues Tracker** (`src/analyzers/github_issues_tracker.py`)
```python  
# Line 166
"https://github.com/duckdb/duckdb/issues"
```

### 🔧 **String Patterns and Messages**

#### Status Messages and Descriptions
- Extension status badges and emojis
- Error messages and logging strings
- Description generation patterns in `community_analyzer.py`

#### URL Construction Patterns  
- GitHub repository URL patterns
- DuckDB documentation URL patterns
- Extension installation URL patterns

## Recommended Migration Strategy

### Phase 1: URL Configuration ✅ **IMPLEMENTED**
- Created `templates/config/output_formats.toml` with URL patterns
- Created `templates/config/special_extensions.toml` for special cases
- Template system now uses configurable URLs

### Phase 2: Update Analyzers 🔄 **IN PROGRESS** 
- Modify community_analyzer.py to use URL patterns from config
- Update report_generator.py to use template system
- Move hardcoded URLs to configuration files

### Phase 3: Message Templates 📋 **PLANNED**
- Move status messages to configuration
- Create message templates for common strings
- Internationalization-ready structure

### Phase 4: Pattern Extraction 🎯 **PLANNED**
- Extract description generation patterns
- Configurable inference rules
- Plugin-based extension classification

## Config Files Created ✅

1. **`templates/config/report_templates.toml`** - Report structures and components
2. **`templates/config/table_configs.toml`** - Table layouts and formatting  
3. **`templates/config/output_formats.toml`** - Format-specific settings and URL patterns
4. **`templates/config/special_extensions.toml`** - Special handling for DuckLake etc.

## Template System Benefits ✅

- **No hardcoded report HTML/Markdown** - Everything is templated
- **Configurable URL patterns** - Easy to update domains or paths
- **Reusable components** - DRY principle for report sections
- **Multiple output formats** - Same data, different presentations  
- **Custom filters** - Standardized formatting logic

## Next Actions Required

1. **Update CommunityExtensionAnalyzer** to use URL patterns from config
2. **Migrate ReportGenerator** to use new template system
3. **Extract remaining hardcoded strings** to message templates
4. **Test configuration-driven system** end-to-end

## Migration Impact

### Positive
- ✅ Much more maintainable codebase
- ✅ Easy to adapt to DuckDB website/API changes
- ✅ Support for multiple environments (dev/prod URLs)
- ✅ Better separation of concerns

### Considerations  
- ⚠️ Need to ensure backward compatibility
- ⚠️ Config validation needed
- ⚠️ Documentation updates required