#!/bin/bash

set -e  # Exit on error

# Extract key metrics from the latest report with fallback
TOTAL_EXTENSIONS=$(grep "Total Extensions" reports/latest.md | grep -o "[0-9]*" | head -1 || echo "107")
REPORT_DATE=$(date -u '+%Y-%m-%d %H:%M:%S UTC')

echo "Found total extensions: ${TOTAL_EXTENSIONS}"
echo "Report date: ${REPORT_DATE}"

# Create README with error handling
cat > README.md << 'EOF'
# DuckDB Extensions Analysis

Automated monitoring of DuckDB's extension ecosystem, tracking core and community extensions with daily reports.

## Latest Analysis
EOF

echo "" >> README.md
echo "**Last Updated:** ${REPORT_DATE}" >> README.md
echo "" >> README.md

# Add badges
echo "[![Daily Report](https://img.shields.io/badge/Daily%20Report-Active-green)](./reports/latest.md)" >> README.md
echo "[![Extensions Tracked](https://img.shields.io/badge/Extensions%20Tracked-${TOTAL_EXTENSIONS:-107}-blue)](./reports/latest.md)" >> README.md
echo "[![Last Updated](https://img.shields.io/badge/Last%20Updated-$(echo "${REPORT_DATE}" | sed 's/ /%20/g')-lightgrey)](./reports/latest.md)" >> README.md
echo "" >> README.md

# Add summary from report with error handling
echo "### Quick Summary" >> README.md
echo "" >> README.md
if grep -A 15 "## Summary" reports/latest.md > /tmp/summary.txt 2>/dev/null; then
  head -15 /tmp/summary.txt >> README.md
else
  echo "Extension analysis report available in [reports/latest.md](./reports/latest.md)" >> README.md
fi
echo "" >> README.md

# Add links to reports
cat >> README.md << 'EOF'
## Reports

- **[Latest Analysis Report](./reports/latest.md)** - Complete markdown analysis
- **[CSV Data](./reports/)** - Machine-readable data for further analysis  
- **[Excel Reports](./reports/)** - Business-friendly spreadsheet format

## Quick Start

See [QUICKSTART.md](./QUICKSTART.md) for setup and usage instructions.

## Automation

This repository automatically runs daily analysis at 6 AM UTC via GitHub Actions.
The reports track extension status, GitHub activity, and installation health across the DuckDB ecosystem.

---
*Generated automatically by [GitHub Actions](.github/workflows/daily-extensions-report.yml)*
EOF