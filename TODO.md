# TODO List

## Completed ✅

### Phase 1: Foundation
- ✅ Created DuckDB release manager
- ✅ Added trend database tables and views
- ✅ Enabled historical tracking in config
- ✅ Created WARP.md documentation
- ✅ Created IMPLEMENTATION_PLAN.md

### Phase 2: Trend Integration  
- ✅ Trend calculation in DatabaseManager
- ✅ Trend query functions + SQL files
- ✅ Historical backfill from git (103 records)
- ✅ Trend data in reports
- ✅ GitHub API rate limiting with aiolimiter

### Phase 3: Report Enhancements
- ✅ Collapsible sections by activity level
- ✅ Enhanced summary with trend highlights
- ✅ Blog post statistics tool

## Next Steps 🔄

### Immediate (Pre-Push)
- [ ] Manual inspection of merged reports
- [ ] Run full workflow: `just workflow`
- [ ] Verify reports look correct
- [ ] Check blog_stats.py output
- [ ] Test HTML site generation: `just site`

### Blog Post
- [ ] Draft blog post about ecosystem growth
- [ ] Include tool improvements summary
- [ ] Highlight key statistics (104→162 extensions, 55.8% growth)
- [ ] Add visualizations/screenshots if desired

### Future Enhancements (Phase 4 - Optional)

#### Code Cleanup
- [ ] Extract URL discovery to separate module
- [ ] Consolidate SQL files where possible
- [ ] Add more comprehensive tests
- [ ] Document trend query API

#### Advanced Features
- [ ] Interactive HTML dashboard with Chart.js
- [ ] Extension language detection improvements
- [ ] Deprecation warnings in reports
- [ ] Correlation with DuckDB releases

#### Maintenance
- [ ] Monitor GitHub Actions for failures
- [ ] Review rate limiting effectiveness
- [ ] Backfill extension_metrics_daily for better trend granularity

## Commands Reference

```bash
# Generate reports
just workflow              # Full analysis + reports + database
just workflow-fresh        # Bypass cache
just report-all           # Just regenerate reports

# Check trends
uv run scripts/query_database.py    # Interactive trend queries
uv run scripts/blog_stats.py        # Blog post statistics

# HTML site
just site                  # Generate HTML from latest report

# Database
just database             # Save current analysis to DB
just query                # Interactive DB queries

# Historical backfill
uv run scripts/backfill_trends_from_git.py
```

## Notes

- Don't push to main until manual verification complete
- Daily GitHub Actions runs at 06:00 UTC
- Current data: 162 extensions (25 core + 137 community)
- Historical tracking: 2025-09-18 to 2025-12-31 (105 days)
