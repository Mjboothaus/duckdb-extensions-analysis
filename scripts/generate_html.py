#!/usr/bin/env python3

import markdown
import re
from pathlib import Path
from datetime import datetime

def main():
    # Read the markdown file
    with open('reports/latest.md', 'r') as f:
        md_content = f.read()
    
    # Extract report timestamp from markdown content
    report_timestamp = 'Loading...'
    timestamp_match = re.search(r'\*\*Report Generated:\*\* ([\d-]+ [\d:]+ UTC)', md_content)
    if timestamp_match:
        report_timestamp = timestamp_match.group(1)
    else:
        # Fallback to current time if not found in report
        report_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

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
    <!-- DataTables CSS -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.7/css/dataTables.bootstrap5.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #24292f;
            max-width: 1400px;
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
        <p><strong>Last Updated:</strong> <code id="utc-time">{report_timestamp}</code></p>
        <p><strong>Your Local Time:</strong> <code id="local-time">Loading...</code></p>
        <p><a href="#summary">Jump to Summary</a> | <a href="#core-extensions">Core Extensions</a> | <a href="#community-extensions">Community Extensions</a></p>
    </div>
    {html_content}
    <hr style="margin-top: 3rem;">
    <footer style="text-align: center; color: #6b7280; font-size: 0.875rem;">
        <p><em>Generated automatically by <a href="https://github.com/Mjboothaus/duckdb-extensions-analysis/actions">GitHub Actions</a></em></p>
        <p><a href="https://github.com/Mjboothaus/duckdb-extensions-analysis">📊 View Source & Data</a></p>
    </footer>
    
    <!-- DataTables JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.7/js/dataTables.bootstrap5.min.js"></script>
    
    <script>
    $(document).ready(function() {{
        // Display user's local time based on the report's UTC timestamp
        function updateLocalTime() {
            // Extract UTC time from the report
            const utcTimeText = $('#utc-time').text();
            const utcMatch = utcTimeText.match(/(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC/);
            
            if (utcMatch) {
                // Parse the UTC time from the report
                const utcTimeString = utcMatch[1];
                const utcDate = new Date(utcTimeString + ' UTC');
                
                // Convert to local time
                const localTimeString = utcDate.toLocaleString('en-AU', {
                    year: 'numeric',
                    month: '2-digit', 
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit',
                    timeZoneName: 'short'
                });
                $('#local-time').text(localTimeString);
            } else {
                // Fallback to current time if parsing fails
                const now = new Date();
                const localTimeString = now.toLocaleString('en-AU', {
                    year: 'numeric',
                    month: '2-digit', 
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit',
                    timeZoneName: 'short'
                });
                $('#local-time').text(localTimeString + ' (current)');
            }
        }
        
        // Update local time once (it's static based on report time)
        updateLocalTime();
        
        // Make tables interactive with appropriate configurations
        $('table').addClass('table table-striped table-hover');
        
        // Configure static tables (Summary, Historical Releases) differently
        $('table').each(function() {{
            const $table = $(this);
            const isStaticTable = $table.closest('h2, h3').prev().text().includes('Summary') || 
                                 $table.closest('h2, h3').prev().text().includes('Historical Releases');
            
            if (isStaticTable) {{
                // Static tables: no pagination, no length menu, but keep search for Historical
                const isHistorical = $table.closest('h2, h3').prev().text().includes('Historical');
                $table.DataTable({{
                    "paging": false,
                    "lengthChange": false,
                    "info": false,
                    "searching": isHistorical,
                    "order": [],
                    "responsive": true,
                    "dom": isHistorical ? 'ft' : 't'
                }});
            }} else {{
                // Interactive tables: full functionality
                $table.DataTable({{
                    "pageLength": 25,
                    "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
                    "order": [],
                    "columnDefs": [
                        {{ "orderable": true, "targets": "_all" }}
                    ],
                    "responsive": true,
                    "dom": '<"top"lf>rt<"bottom"ip><"clear">'
                }});
            }}
        }});
        
        // Add timezone info tooltip after tables are initialized
        setTimeout(function() {{
            $('#local-time').attr('title', 'Shows the report generation time converted to your local timezone');
        }}, 100);
    }});
    </script>
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