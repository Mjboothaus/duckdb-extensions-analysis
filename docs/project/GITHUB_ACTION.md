# 🤖 GitHub Action Automated Monitoring

Set up automated daily monitoring of DuckDB extensions with GitHub Actions and optional GitHub Pages deployment.

## 🚀 Quick Setup

### 1. Enable GitHub Actions
The workflow is already configured in `.github/workflows/daily-extensions-report.yml`

### 2. Enable GitHub Pages (Optional)
For public dashboard at `https://yourusername.github.io/duckdb-extensions-analysis`:

1. Go to **Settings** → **Pages**
2. Set **Source** to "GitHub Actions"
3. The workflow will automatically deploy to Pages

### 3. Configure Repository Settings
- **Actions**: Enable Actions in repository settings
- **Permissions**: Workflow has required permissions configured
- **Secrets**: Uses `GITHUB_TOKEN` (automatically available)

## 📅 Workflow Schedule

- **Daily**: Runs at 6 AM UTC (2 AM EDT, 11 PM PDT)
- **Manual**: Trigger via "Run workflow" button in Actions tab
- **On Push**: Can be configured to run on specific branches

## 📊 What Gets Generated

### Repository Updates
- Updates `README.md` with latest status and badges
- Generates new report files in `reports/` directory
- Commits changes with automated messages

### GitHub Pages Site (Optional)
- Clean HTML version of the latest report
- Direct download links for CSV/Excel files
- Automatic styling for better readability

## 🔧 Customization Options

### Change Schedule
Edit `.github/workflows/daily-extensions-report.yml`:
```yaml
on:
  schedule:
    - cron: '0 18 * * *'  # Change to 6 PM UTC
```

### Include/Exclude GitHub Issues
```bash
# With GitHub issues (current default)
--with-issues

# Without GitHub issues (faster)
# Remove --with-issues flag
```

### Report Formats
```bash
# Current: All formats
--format markdown --format csv --format excel

# Markdown only
--format markdown

# CSV only for automation
--format csv
```

## 🛡️ Rate Limiting

The workflow uses:
- `GITHUB_TOKEN` for API access (higher rate limits)
- Efficient direct repository API calls (not search API)  
- Built-in caching to reduce API usage

## 📋 Monitoring the Workflow

### Check Status
- **Actions Tab**: View workflow runs and logs
- **README Badges**: Quick status indicators
- **Commit History**: See automated commits

### Troubleshooting
- View workflow logs in Actions tab
- Check for rate limiting messages
- Verify Pages deployment status

## 🎯 Use Cases

### Daily Dashboard
- Track extension ecosystem health
- Monitor new extensions or issues
- Historical tracking via commit history

### API Integration  
- CSV/Excel files available for download
- Direct links to structured data
- Webhook triggers on repository updates

### Notifications
Add to workflow for alerts:
```yaml
- name: Notify on issues
  if: contains(steps.*.outputs.*, 'CRITICAL')
  uses: actions/github-script@v6
  # ... notification logic
```

## 🔍 Example Output

The workflow generates:
1. **README.md** with status badges and quick summary
2. **reports/latest.md** with full analysis
3. **CSV/Excel** files for data analysis
4. **GitHub Pages** site (if enabled)

Ready for automated DuckDB extension monitoring! 🚀