# Performance & GitHub API Notes

## Expected GitHub API Behaviour

### 403 Errors (Rate Limiting)

**Expected behaviour**: Some 403 errors are normal when analysing 162 extensions.

**Why it happens**:
- GitHub has **secondary rate limits** (abuse detection) beyond the documented 5000/hour limit
- Even with rate limiting at 5 req/sec, rapid sequential requests can trigger these limits
- The tool already implements:
  - AsyncLimiter (5 req/sec) to avoid secondary limits
  - Exponential backoff retry logic (5 attempts, 2-60s waits)
  - Caching with 1-hour default TTL

**What gets cached**:
- Repository metadata (stars, forks, last push, etc.)
- Commit history
- Community extensions list
- DuckDB releases

**How to minimise 403s**:
- ✅ Use `GITHUB_TOKEN` environment variable (set via `just setup-auth`)
- ✅ Use cached data: `just workflow` (default 12-hour cache)
- ❌ **NEVER use `--cache-hours 0`** - this bypasses cache and triggers abuse detection
- ⚠️ If you get 403s: wait 30-60 minutes for GitHub's penalty to expire
- 💡 For truly fresh data: delete cache and use default TTL: `just cache-clear && just workflow`

### 404 Errors (Repos Not Found)

**Expected behaviour**: Some repos genuinely don't exist anymore.

**Why it happens**:
- Repository **deleted or renamed** after being added to community-extensions
- Repository made **private** by owner
- Incorrect repo URL in extension metadata

**Where extension info comes from**:
1. **Primary source**: `duckdb/community-extensions/extensions/{name}/description.yml`
   - Contains: extension name, description, version, maintainer
   - **Always available** even if repo is missing
2. **Secondary source**: GitHub repository API
   - Contains: stars, forks, last push, language, topics
   - **May fail** with 404 if repo deleted/private

**How the tool handles missing repos**:
- Fetches extension list from community-extensions (never fails)
- Attempts GitHub API call for repo info (may fail)
- Falls back to `description.yml` metadata when repo unavailable
- Uses deprecation detector to identify truly deprecated extensions
- Reports basic info even without GitHub access

**Extensions with missing repos are still valid** - they may be deprecated or the maintainer moved the repo.

## Performance Optimisation Opportunities

### Current Performance Bottlenecks

Based on workflow timing analysis:

#### 1. Core Extensions Analysis (~slow)
**Why it's slow**:
- 25 extensions × multiple API calls each:
  - Repository info (1 call)
  - Commit history (1-2 calls, potentially with path filters)
  - External repo checks for some extensions
- Platform availability checks: 6 platforms × 25 extensions = **150 HTTP HEAD requests** to DuckDB extension servers
- Some sequential processing that could be parallelised

**Optimisation options**:
- ✅ Already cached: repo info, commits (1 hour TTL)
- 🔄 **Could cache**: platform availability checks (currently not cached)
- 🔄 **Could cache**: DuckDB docs HTML parsing (re-downloads every run)
- 🔄 **Could parallelise**: platform checks across extensions

#### 2. Community Extensions Analysis (~moderate)
**Why it's moderate**:
- 137 extensions × API calls:
  - Extension metadata (description.yml) - 137 calls
  - Repository info - 137 calls
  - Deprecation detection (README fetch) - 137 calls
- Already uses rate limiting (5 req/sec)

**Optimisation options**:
- ✅ Already cached: extension metadata, repo info (1 hour TTL)
- ✅ Already cached: deprecation detector data (1 hour TTL, now fixed)
- 🔄 **Could batch**: metadata fetches (fetch multiple at once)

#### 3. Database Operations (~fast)
- Already efficient: single connection, batch inserts
- Trend calculations are SQL-based (fast)

### Recommended Optimisations (Priority Order)

#### Priority 1: Cache Platform Availability Checks
**Impact**: High (150+ HTTP requests → 0 on cached runs)
**Complexity**: Low

Cache extension binary availability checks for longer (24 hours):
- Binary availability rarely changes within a day
- Would save ~10-15 seconds per run for core extensions

#### Priority 2: Cache DuckDB Docs HTML
**Impact**: Medium (1 HTTP request + HTML parsing → cached)
**Complexity**: Low

Cache the core extensions docs page HTML:
- Currently re-downloaded and parsed every run
- Changes rarely (only when core extensions added/updated)

#### Priority 3: Parallelise Platform Checks
**Impact**: Medium (reduce sequential wait time)
**Complexity**: Medium

Already uses `asyncio.gather()` for platform checks per extension, but could:
- Check multiple extensions' platforms concurrently
- Requires careful rate limiting to avoid overwhelming servers

#### Priority 4: Batch Community Extension Metadata
**Impact**: Low-Medium (reduce sequential API calls)
**Complexity**: Medium

GitHub API supports GraphQL for batching:
- Could fetch multiple extension metadata files in one request
- Requires implementing GraphQL queries

### Cache Management Best Practices

**For development** (frequent testing):
```bash
just workflow            # Use default 1-hour cache
just cache-info          # Check cache stats
```

**For production** (daily automation):
```bash
just workflow-fresh      # Always fetch latest data
```

**For manual inspection** (current situation):
```bash
just workflow            # Use cache to avoid rate limits
just cache-clear         # If you need truly fresh data
```

### Current Cache Configuration

**GitHub API cache** (`GitHubAPIClient`):
- Default TTL: 1 hour (configurable via `--cache-hours`)
- Location: `.cache/`
- Cached items: repo info, commits, releases, extensions list

**Deprecation detector cache** (`RepositoryCache`):
- Default TTL: 1 hour (now fixed from 24 days bug)
- Location: `.cache/deprecation_detector/`
- Cached items: README content, repo status

**Web content cache** (via config):
- TTL: 24 hours (for less frequently changing content)
- Used for: DuckDB docs, documentation pages

## Monitoring & Debugging

### Check cache effectiveness:
```bash
just cache-info
```

### View GitHub API rate limit status:
```bash
# In python:
import requests
headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
response = requests.get('https://api.github.com/rate_limit', headers=headers)
print(response.json())
```

### Analyse workflow timing:
Look for log lines showing time spent on each phase:
- "Analysis of core extensions" - should be ~20-40s cached, ~60-90s fresh
- "Analysis of community extensions" - should be ~30-60s cached, ~90-180s fresh  
- "Database operations" - should be ~5-10s

### Expected 403/429 rate limit indicators:
```
WARNING: Rate limit (403/429) detected, waiting 5s
WARNING: Retry attempt 2 for GitHub API after error: ...
```

## Summary

**Current state**:
- ✅ Rate limiting implemented (5 req/sec)
- ✅ Intelligent caching (1 hour default)
- ✅ Exponential backoff retries
- ✅ Graceful fallback for missing repos
- 🔧 Fixed: cache TTL bug (24 days → 1 hour)

**Expected behaviour**:
- Some 403 errors are **normal** (secondary rate limits)
- Some 404 errors are **expected** (deleted/private repos)
- Extensions work even without GitHub access (fallback to community-extensions metadata)

**Performance is acceptable for**:
- Daily automation (runs once per day with fresh data)
- Development with cache (fast repeated runs)

**Further optimisation needed if**:
- Running multiple times per hour (cache helps)
- Hitting consistent rate limits (increase `--cache-hours` or add `GITHUB_TOKEN`)
- Need faster core extensions analysis (implement platform availability caching)
