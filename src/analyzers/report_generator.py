"""
Report Generator for DuckDB Extensions Analysis.

Handles generation of reports in multiple formats (Markdown, CSV, Excel).
"""

from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import pandas as pd
from loguru import logger

from .base import BaseReportGenerator, AnalysisResult, ExtensionInfo


class ReportGenerator(BaseReportGenerator):
    """Unified report generator for multiple formats."""
    
    def __init__(self, config):
        super().__init__(config)
        self.reports_dir = config.reports_dir
        self.templates_dir = Path(config.project_root) / "templates"
        self.config = config
        self._core_extension_urls_cache = None
    
    def _load_template(self, template_name: str) -> str:
        """Load template content from file."""
        template_file = self.templates_dir / template_name
        if not template_file.exists():
            logger.warning(f"Template file not found: {template_file}")
            return ""
        
        with open(template_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    
    def _discover_core_extension_urls(self) -> Dict[str, str]:
        """Discover URLs for core extensions from DuckDB documentation."""
        if self._core_extension_urls_cache is not None:
            return self._core_extension_urls_cache
        
        logger.info("Discovering core extension URLs from DuckDB documentation")
        
        extension_urls = {}
        
        try:
            import requests
            from bs4 import BeautifulSoup
            import diskcache as dc
            from datetime import timedelta
            import hashlib
            
            # Set up caching
            cache = dc.Cache(str(self.config.cache_dir))
            cache_key = "core_extension_urls"
            
            # Check cache first (cache for 24 hours)
            cached_data = cache.get(cache_key)
            if cached_data:
                cached_time, urls = cached_data
                if datetime.now() - cached_time < timedelta(hours=24):
                    logger.debug("Using cached core extension URLs")
                    self._core_extension_urls_cache = urls
                    return urls
            
            # Fetch the core extensions overview page
            overview_url = "https://duckdb.org/docs/stable/core_extensions/overview.html"
            response = requests.get(overview_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for links to individual extension pages
            # Pattern 1: Links in tables
            for table in soup.find_all('table'):
                for row in table.find_all('tr'):
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 2:
                        # First cell might contain extension name and link
                        first_cell = cells[0]
                        link = first_cell.find('a', href=True)
                        if link:
                            href = link['href']
                            extension_name = link.get_text(strip=True).lower()
                            if href.startswith('/docs/stable/core_extensions/'):
                                full_url = f"https://duckdb.org{href}"
                                extension_urls[extension_name] = full_url
                            elif href.startswith('https://duckdb.org/docs/stable/core_extensions/'):
                                extension_urls[extension_name] = href
            
            # Pattern 2: Look for any links to core_extensions in the page
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/docs/stable/core_extensions/' in href and href.endswith('.html'):
                    # Extract extension name from URL
                    extension_name = href.split('/')[-1].replace('.html', '')
                    if extension_name not in ['overview', 'index']:
                        if href.startswith('/'):
                            full_url = f"https://duckdb.org{href}"
                        else:
                            full_url = href
                        extension_urls[extension_name.lower()] = full_url
            
            # Also check the main extensions page for additional links
            try:
                main_extensions_url = "https://duckdb.org/docs/stable/extensions/overview.html"
                response2 = requests.get(main_extensions_url, timeout=10)
                response2.raise_for_status()
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                
                for link in soup2.find_all('a', href=True):
                    href = link['href']
                    if '/docs/stable/core_extensions/' in href and href.endswith('.html'):
                        extension_name = href.split('/')[-1].replace('.html', '')
                        if extension_name not in ['overview', 'index']:
                            if href.startswith('/'):
                                full_url = f"https://duckdb.org{href}"
                            else:
                                full_url = href
                            extension_urls[extension_name.lower()] = full_url
            except Exception as e:
                logger.debug(f"Could not fetch main extensions page: {e}")
            
            # Cache the results
            cache.set(cache_key, (datetime.now(), extension_urls))
            
            logger.info(f"Discovered {len(extension_urls)} core extension URLs")
            logger.debug(f"Extension URLs: {list(extension_urls.keys())}")
            
        except Exception as e:
            logger.warning(f"Failed to discover core extension URLs: {e}")
            # Fallback to basic pattern-based URLs for known extensions
            common_extensions = [
                "autocomplete", "avro", "aws", "azure", "delta", "ducklake", "encodings", 
                "excel", "fts", "httpfs", "iceberg", "icu", "inet", "jemalloc", "json", 
                "mysql", "parquet", "postgres", "spatial", "sqlite", "tpcds", "tpch", "ui", "vss"
            ]
            for ext_name in common_extensions:
                extension_urls[ext_name] = f"https://duckdb.org/docs/stable/core_extensions/{ext_name}.html"
        
        self._core_extension_urls_cache = extension_urls
        return extension_urls
    
    def _format_days_ago(self, date_str: Optional[str], fallback_days: int) -> str:
        """Format a date string into 'X days ago' format."""
        if not date_str:
            return f"{fallback_days} days ago"
        
        try:
            from dateutil import parser
            commit_date = parser.parse(date_str)
            days_ago = (datetime.now(commit_date.tzinfo) - commit_date).days
            return f"{days_ago} days ago"
        except Exception as e:
            logger.debug(f"Could not parse date {date_str}: {e}")
            return f"{fallback_days} days ago"
    
    async def generate(self, analysis_result: AnalysisResult, format_type: str = "markdown") -> str:
        """Generate a report in the specified format."""
        if format_type.lower() == "markdown":
            return await self.generate_markdown(analysis_result)
        elif format_type.lower() == "csv":
            return await self.generate_csv(analysis_result)
        elif format_type.lower() == "excel":
            return await self.generate_excel(analysis_result)
        else:
            raise ValueError(f"Unsupported report format: {format_type}")
    
    async def generate_markdown(self, analysis_result: AnalysisResult) -> str:
        """Generate comprehensive markdown report."""
        logger.info("Generating markdown report")
        
        timestamp = analysis_result.analysis_timestamp
        duckdb_version = analysis_result.duckdb_version
        duckdb_release_date = analysis_result.duckdb_release_date
        
        # Calculate days since DuckDB release
        duckdb_lag_days = (timestamp.replace(tzinfo=None) - duckdb_release_date.replace(tzinfo=None)).days if duckdb_release_date else 0
        
        # Report header with template content
        header_template = self._load_template("report_header.md")
        report = [
            "# DuckDB Extensions Status Report",
            "",
            f"Generated on: **{timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}**",
            "",
        ]
        
        if header_template:
            report.extend([header_template, ""])
        
        # Core extensions section
        report.extend([
            "## Core Extensions\n",
            f"DuckDB core extensions from version **{duckdb_version}** (released {duckdb_lag_days} days ago).\n",
            "| Extension | Development Stage | Status | Last Updated |",
            "|-----------|-------------------|--------|--------------|",
        ])
        
        # Discover core extension URLs
        extension_urls = self._discover_core_extension_urls()
        
        for ext in analysis_result.core_extensions:
            stage = ext.stage or "Stable"
            status = "✅ Ongoing"
            
            # Use actual commit date if available, otherwise fallback to DuckDB release
            if ext.metadata and ext.metadata.get("last_commit_date"):
                last_updated = self._format_days_ago(ext.metadata["last_commit_date"], duckdb_lag_days)
            else:
                last_updated = f"{duckdb_lag_days} days ago (in {duckdb_version})"
            
            # Create extension name with URL if available
            extension_name = ext.name
            extension_url = extension_urls.get(ext.name.lower())
            if extension_url:
                extension_name = f"[{ext.name}]({extension_url})"
            
            report.append(f"| **{extension_name}** | {stage} | {status} | {last_updated} |")
        
        report.extend([
            f"\n**Total Core Extensions**: {len(analysis_result.core_extensions)}\n",
            "",
        ])
        
        # Community extensions section
        report.extend([
            "## Community Extensions\n",
            "| Extension | Repository | Status | Last Push | Stars | Language | Description |",
            "|-----------|------------|--------|-----------|-------|----------|-------------|",
        ])
        
        for ext in analysis_result.community_extensions:
            status = ext.metadata.get("status", "❌ Error") if ext.metadata else "❌ Error"
            repo_link = f"[{ext.repository}](https://github.com/{ext.repository})" if ext.repository else "N/A"
            last_push = f"{ext.days_ago} days ago" if ext.days_ago is not None else "Unknown"
            stars = str(ext.stars) if ext.stars is not None else "N/A"
            
            # Get language and description from metadata
            language = "N/A"
            description = ext.description or "No description"
            
            if ext.metadata and ext.metadata.get("repo_info"):
                repo_info = ext.metadata["repo_info"]
                language = repo_info.get("language", "N/A") or "N/A"
            
            # Truncate description
            if len(description) > 50:
                description = description[:50] + "..."
            
            # Escape pipe characters in description
            description = description.replace("|", "\\|")
            
            report.append(f"| **{ext.name}** | {repo_link} | {status} | {last_push} | {stars} | {language} | {description} |")
        
        # Community extensions summary
        active = sum(1 for ext in analysis_result.community_extensions 
                    if ext.metadata and ext.metadata.get("status") == "✅ Ongoing")
        discontinued = sum(1 for ext in analysis_result.community_extensions 
                          if ext.metadata and ext.metadata.get("status") == "🔴 Discontinued")
        errors = sum(1 for ext in analysis_result.community_extensions 
                    if ext.metadata and "❌" in ext.metadata.get("status", ""))
        total = len(analysis_result.community_extensions)
        
        report.extend([
            "\n### Community Extensions Summary",
            f"- **Total Extensions**: {total}",
            f"- **Active Extensions**: {active} ({active / total * 100:.1f}%)" if total > 0 else f"- **Active Extensions**: 0 (0%)",
            f"- **Discontinued Extensions**: {discontinued} ({discontinued / total * 100:.1f}%)" if total > 0 else f"- **Discontinued Extensions**: 0 (0%)",
            f"- **Extensions with Issues**: {errors} ({errors / total * 100:.1f}%)" if total > 0 else f"- **Extensions with Issues**: 0 (0%)",
            "",
        ])
        
        # Add methodology section from template
        methodology_template = self._load_template("report_methodology.md")
        if methodology_template:
            report.extend(["", methodology_template])
        
        return "\n".join(report)
    
    async def generate_csv(self, analysis_result: AnalysisResult) -> str:
        """Generate CSV report data and return the filename."""
        logger.info("Generating CSV report")
        
        rows = []
        
        # Add core extensions
        for ext in analysis_result.core_extensions:
            rows.append({
                "Extension": ext.name,
                "Type": "Core",
                "Repository": ext.repository or "duckdb/duckdb",
                "Status": "✅ Ongoing",
                "Development Stage": ext.stage or "Stable",
                "Last Push Days": (analysis_result.analysis_timestamp.replace(tzinfo=None) - analysis_result.duckdb_release_date.replace(tzinfo=None)).days if analysis_result.duckdb_release_date else 0,
                "Stars": "N/A",
                "Language": "C++",
                "Description": "Core DuckDB extension",
                "Featured": False,
            })
        
        # Add community extensions
        for ext in analysis_result.community_extensions:
            repo_info = ext.metadata.get("repo_info") if ext.metadata else {}
            
            rows.append({
                "Extension": ext.name,
                "Type": "Community",
                "Repository": ext.repository or "N/A",
                "Status": ext.metadata.get("status", "❌ Error") if ext.metadata else "❌ Error",
                "Development Stage": "N/A",
                "Last Push Days": ext.days_ago,
                "Stars": ext.stars or 0,
                "Language": repo_info.get("language", "N/A") if repo_info else "N/A",
                "Description": ext.description or "No description",
                "Featured": ext.featured,
            })
        
        # Create DataFrame and save to CSV
        df = pd.DataFrame(rows)
        timestamp = analysis_result.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        csv_filename = f"duckdb_extensions_report_{timestamp}.csv"
        csv_path = self.reports_dir / csv_filename
        
        self.config.ensure_directories()
        df.to_csv(csv_path, index=False)
        
        logger.info(f"CSV report saved: {csv_path}")
        return str(csv_path)
    
    async def generate_excel(self, analysis_result: AnalysisResult) -> str:
        """Generate Excel report data and return the filename."""
        logger.info("Generating Excel report")
        
        # Use the same data as CSV
        rows = []
        
        # Add core extensions
        for ext in analysis_result.core_extensions:
            rows.append({
                "Extension": ext.name,
                "Type": "Core",
                "Repository": ext.repository or "duckdb/duckdb",
                "Status": "✅ Ongoing",
                "Development Stage": ext.stage or "Stable",
                "Last Push Days": (analysis_result.analysis_timestamp.replace(tzinfo=None) - analysis_result.duckdb_release_date.replace(tzinfo=None)).days if analysis_result.duckdb_release_date else 0,
                "Stars": "N/A",
                "Language": "C++",
                "Description": "Core DuckDB extension",
                "Featured": False,
            })
        
        # Add community extensions
        for ext in analysis_result.community_extensions:
            repo_info = ext.metadata.get("repo_info") if ext.metadata else {}
            
            rows.append({
                "Extension": ext.name,
                "Type": "Community",
                "Repository": ext.repository or "N/A",
                "Status": ext.metadata.get("status", "❌ Error") if ext.metadata else "❌ Error",
                "Development Stage": "N/A",
                "Last Push Days": ext.days_ago,
                "Stars": ext.stars or 0,
                "Language": repo_info.get("language", "N/A") if repo_info else "N/A",
                "Description": ext.description or "No description",
                "Featured": ext.featured,
            })
        
        # Create DataFrame and save to Excel
        df = pd.DataFrame(rows)
        timestamp = analysis_result.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        excel_filename = f"duckdb_extensions_report_{timestamp}.xlsx"
        excel_path = self.reports_dir / excel_filename
        
        self.config.ensure_directories()
        df.to_excel(excel_path, index=False, engine='openpyxl')
        
        logger.info(f"Excel report saved: {excel_path}")
        return str(excel_path)
    
    def save_report(self, content: str, filename: str) -> str:
        """Save the report content to a file."""
        self.config.ensure_directories()
        
        file_path = self.reports_dir / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Also save as latest.md for markdown reports
        if filename.endswith('.md'):
            latest_path = self.reports_dir / "latest.md"
            with open(latest_path, "w", encoding="utf-8") as f:
                f.write(content)
        
        logger.info(f"Report saved: {file_path}")
        return str(file_path)