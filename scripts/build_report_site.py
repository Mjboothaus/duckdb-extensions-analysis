#!/usr/bin/env python3

import markdown
import re
from pathlib import Path
from datetime import datetime

def main():
    # Read the markdown file
    with open('reports/latest.md', 'r') as f:
        md_content = f.read()
    
    # Extract report timestamp from markdown content or Git
    report_timestamp = 'Loading...'
    
    # Try to find the timestamp in the markdown first
    timestamp_patterns = [
        r'\*\*Report Generated:\*\* ([\d-]+ [\d:]+ UTC)',
        r'Report Generated: ([\d-]+ [\d:]+ UTC)',
        r'Last Updated: ([\d-]+ [\d:]+ UTC)'
    ]
    
    for pattern in timestamp_patterns:
        timestamp_match = re.search(pattern, md_content)
        if timestamp_match:
            report_timestamp = timestamp_match.group(1)
            break
    
    # If not found in markdown, try to get from git (latest commit time)
    if report_timestamp == 'Loading...':
        try:
            import subprocess
            git_timestamp = subprocess.check_output(
                ['git', 'log', '-1', '--format=%cd', '--date=format:%Y-%m-%d %H:%M:%S UTC', '--', 'reports/latest.md'],
                cwd=Path.cwd(),
                universal_newlines=True
            ).strip()
            if git_timestamp:
                report_timestamp = git_timestamp
        except Exception:
            pass
    
    # Final fallback to current time
    if report_timestamp == 'Loading...':
        report_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

    # Convert markdown to HTML with proper handling of HTML blocks
    # The 'md_in_html' extension allows markdown processing inside HTML tags
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'toc',
        'md_in_html'  # Critical: enables markdown parsing inside <details> and other HTML tags
    ])
    html_content = md.convert(md_content)

    # Read template files
    template_dir = Path('scripts/templates')
    
    # Read HTML template
    with open(template_dir / 'index.html', 'r') as f:
        html_template = f.read()
    
    # Read CSS template
    with open(template_dir / 'styles.css', 'r') as f:
        css_content = f.read()
    
    # Read JavaScript template
    with open(template_dir / 'main.js', 'r') as f:
        js_content = f.read()
    
    # Replace placeholders in the HTML template
    full_html = html_template.replace('{{STYLES}}', css_content)
    full_html = full_html.replace('{{CONTENT}}', html_content)
    full_html = full_html.replace('{{REPORT_TIMESTAMP}}', report_timestamp)
    full_html = full_html.replace('{{JAVASCRIPT}}', js_content)

    # Create _site directory
    Path('_site').mkdir(exist_ok=True)

    # Write the HTML file
    with open('_site/index.html', 'w') as f:
        f.write(full_html)
        
    print("✅ HTML site generated successfully")

if __name__ == "__main__":
    main()