# DuckDB Community Extensions Deprecation Analysis Summary

**Analysis Date:** 2025-09-27  
**Total Extensions Analyzed:** 83  
**Analysis Tool:** `scripts/detect_deprecated_extensions.py`

## High-Confidence Deprecated Extensions (Score ≥ 8.0)

### 1. `nanoarrow` (Score: 10.0) ⚠️ **CRITICAL**
- **Repository:** [paleolimbot/duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow)
- **Evidence:** README explicitly states it serves "a similar purpose as the now-deprecated [Arrow DuckDB core extension]"
- **Recommendation:** **Mark as deprecated immediately**
- **Action Required:** Update configuration to set `deprecated: true`

### 2. `pivot_table` (Score: 8.0)
- **Repository:** [Alex-Monahan/pivot_table](https://github.com/Alex-Monahan/pivot_table)
- **Evidence:** Multiple example-only indicators
- **Last Activity:** 2024-09-22
- **Action Required:** Manual verification recommended before marking deprecated

### 3. `tarfs` (Score: 8.0)
- **Repository:** [Maxxen/duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs)
- **Evidence:** Multiple example-only indicators
- **Last Activity:** 2024-08-26
- **Action Required:** Manual verification recommended before marking deprecated

## Extensions Requiring Manual Review (Score: 5.0-7.0)

These 17 extensions show concerning patterns and should be manually reviewed:

- `hostfs`, `netquack`, `quackformers`, `splink_udfs` (Score: 7.0 each)
- `duckpgq`, `markdown`, `ofquack`, `ulid`, `yaml` (Score: 6.0 each)  
- `bigquery`, `chaos`, `h3`, `parser_tools`, `psql`, `snowflake`, `vortex`, `zipfs` (Score: 5.0 each)

**Common Issues:**
- Extensions marked as "experimental" or "work in progress"
- Template extensions that may not be production-ready
- Extensions with primarily example-focused documentation

## Technical Issues Found

### Repository URL Truncation
Several repository URLs are being truncated in the community extensions metadata, causing 404 errors:
- `query-farm/airpor` (should be `airport`)
- `query-farm/evalexpr_rha` (should be `evalexpr_rhai`)
- Multiple similar truncations

### HTTP 301 Redirects
Several `quackscience` repositories return 301 redirects, suggesting they may have been moved or reorganised.

## Recommended Actions

### Immediate (High Priority)
1. **Mark `nanoarrow` as deprecated** - Clear evidence of replacement
2. **Investigate URL truncation issue** - Fix metadata parsing in community-extensions repo
3. **Manual review of HTTP 301 redirects** - Update URLs or mark as deprecated

### Medium Priority
1. **Manual verification** of `pivot_table` and `tarfs` extensions
2. **Review experimental/WIP extensions** - Determine production readiness
3. **Template extensions audit** - Some may be meant for development only

### Process Improvements
1. **Regular deprecation scanning** - Run this analysis quarterly
2. **Automated metadata validation** - Catch truncation issues early
3. **Extension lifecycle documentation** - Clear guidelines for marking extensions deprecated

## Caching Performance

The analysis now includes intelligent caching:
- **Cache Directory:** `.cache/deprecation_detector/`
- **TTL:** 7 days (configurable)
- **Performance:** Second run completed in ~12 seconds vs initial ~90 seconds
- **API Efficiency:** Dramatically reduced GitHub API calls

## Usage

```bash
# Run with caching enabled (recommended)
GITHUB_TOKEN=$(gh auth token) uv run scripts/detect_deprecated_extensions.py \
  --cache-dir .cache/deprecation_detector \
  --format markdown \
  --output reports/deprecated_analysis.md

# Quick JSON analysis
GITHUB_TOKEN=$(gh auth token) uv run scripts/detect_deprecated_extensions.py \
  --format json | jq '.[] | select(.deprecation_score >= 8)'
```

---

**Next Steps:** Use this analysis to update the extensions configuration and improve the community extensions maintenance process.