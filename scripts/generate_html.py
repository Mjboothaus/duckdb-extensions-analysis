#!/usr/bin/env python3

import markdown
import re
from pathlib import Path
from datetime import datetime

def main():
    # Read the markdown file
    with open('reports/latest.md', 'r') as f:
        md_content = f.read()

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    html_content = md.convert(md_content)

    # Create full HTML page
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DuckDB Extensions Analysis</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #24292f;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #1f2937;
            border-bottom: 1px solid #e1e5e9;
            padding-bottom: 0.5rem;
            margin-top: 2rem;
        }}
        h1 {{ font-size: 2rem; }}
        h2 {{ font-size: 1.5rem; }}
        h3 {{ font-size: 1.25rem; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1rem 0;
            background-color: #fff;
        }}
        th, td {{
            border: 1px solid #d1d5db;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f9fafb;
            font-weight: 600;
            color: #374151;
        }}
        tr:nth-child(even) {{
            background-color: #f9fafb;
        }}
        tr:hover {{
            background-color: #f3f4f6;
        }}
        code {{
            background-color: #f1f5f9;
            color: #1e293b;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'SFMono-Regular', 'Monaco', 'Inconsolata', 'Liberation Mono', 'Courier New', monospace;
        }}
        pre {{
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
        }}
        a {{
            color: #0969da;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .status-ongoing {{ color: #059669; }}
        .status-discontinued {{ color: #dc2626; }}
        .status-issues {{ color: #d97706; }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            background-color: #f1f5f9;
            border-radius: 4px;
            font-size: 0.875rem;
            margin-right: 8px;
        }}
        .toc {{
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 2rem;
        }}
        .header-info {{
            background-color: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 2rem;
        }}
    </style>
</head>
<body>
    <div class="header-info">
        <h2 style="margin-top: 0; border: none;">🦆 DuckDB Extensions Analysis</h2>
        <p>Automated monitoring and analysis of DuckDB's extension ecosystem.</p>
        <p><strong>Last Updated:</strong> <code>{datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</code></p>
        <p><a href="#summary">Jump to Summary</a> | <a href="#core-extensions">Core Extensions</a> | <a href="#community-extensions">Community Extensions</a></p>
    </div>
    {html_content}
    <hr style="margin-top: 3rem;">
    <footer style="text-align: center; color: #6b7280; font-size: 0.875rem;">
        <p><em>Generated automatically by <a href="https://github.com/Mjboothaus/duckdb-extensions-analysis/actions">GitHub Actions</a></em></p>
        <p><a href="https://github.com/Mjboothaus/duckdb-extensions-analysis">📊 View Source & Data</a></p>
    </footer>
</body>
</html>'''

    # Create _site directory
    Path('_site').mkdir(exist_ok=True)

    # Write the HTML file
    with open('_site/index.html', 'w') as f:
        f.write(full_html)
        
    print("✅ HTML site generated successfully")

if __name__ == "__main__":
    main()