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
from .extension_metadata import ExtensionMetadata
from ..templates import TemplateEngine


class ReportGenerator(BaseReportGenerator):
    """Unified report generator for multiple formats."""
    
    def __init__(self, config):
        super().__init__(config)
        self.reports_dir = config.reports_dir
        self.templates_dir = Path(config.project_root) / "templates"
        self.config = config
        self.metadata = ExtensionMetadata(config.config_dir)
        self.template_engine = TemplateEngine(config, self.templates_dir)
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
        """
        Discover URLs to the documentation for core extensions from DuckDB website.
        
        This function relies on several DuckDB documentation sources to find URLs:
        1. Primary source: Core extensions overview page at /docs/stable/core_extensions/overview.html
        2. Secondary source: Main extensions overview at /docs/stable/extensions/overview.html
        3. Special cases: Some extensions like 'json' and 'parquet' have documentation under 
           /docs/stable/data/ rather than /core_extensions/
        
        The function handles several URL patterns and exceptions:
        - Standard pattern: /docs/stable/core_extensions/extension_name.html
        - Overview pattern: /docs/stable/core_extensions/extension_name/overview.html
        - Data section pattern: /docs/stable/data/extension_name/overview.html
        
        Note that DuckDB's documentation structure has inconsistencies in URL patterns 
        and location of extension documentation, which requires special handling.
        
        Returns:
            Dict[str, str]: Mapping of extension names to their documentation URLs
        """
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
                    if href.endswith('/overview.html'):
                        # Handle httpfs/overview.html -> httpfs
                        extension_name = href.split('/')[-2]
                    else:
                        # Handle standard extension.html -> extension
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
                        # Extract extension name from URL
                        if href.endswith('/overview.html'):
                            # Handle httpfs/overview.html -> httpfs
                            extension_name = href.split('/')[-2]
                        else:
                            # Handle standard extension.html -> extension
                            extension_name = href.split('/')[-1].replace('.html', '')
                        
                        if extension_name not in ['overview', 'index']:
                            if href.startswith('/'):
                                full_url = f"https://duckdb.org{href}"
                            else:
                                full_url = href
                            extension_urls[extension_name.lower()] = full_url
            except Exception as e:
                logger.debug(f"Could not fetch main extensions page: {e}")
            
            # Add URLs from metadata system for extensions with special documentation patterns
            # This handles extensions that don't follow standard URL patterns and ensures
            # all known core extensions have valid URLs in the report.
            for ext_name in self.metadata.get_all_core_extensions():
                special_url = self.metadata.get_special_url(ext_name)
                if special_url:
                    extension_urls[ext_name] = special_url
                elif ext_name not in extension_urls:
                    # Generate URL using metadata patterns
                    generated_url = self.metadata.get_documentation_url(ext_name)
                    if generated_url:
                        extension_urls[ext_name] = generated_url
            
            # Cache the results (including special cases)
            cache.set(cache_key, (datetime.now(), extension_urls))
            
            logger.info(f"Discovered {len(extension_urls)} core extension URLs")
            logger.debug(f"Extension URLs: {list(extension_urls.keys())}")
            
        except Exception as e:
            logger.warning(f"Failed to discover core extension URLs: {e}")
            # Fallback to metadata-based URL generation for all known extensions
            for ext_name in self.metadata.get_all_core_extensions():
                # Use metadata to generate appropriate URL
                generated_url = self.metadata.get_documentation_url(ext_name)
                if generated_url:
                    extension_urls[ext_name] = generated_url
        
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
    
    def _get_days_from_date(self, date_str: Optional[str]) -> Optional[int]:
        """Extract the number of days ago from a date string."""
        if not date_str:
            return None
        
        try:
            from dateutil import parser
            commit_date = parser.parse(date_str)
            days_ago = (datetime.now(commit_date.tzinfo) - commit_date).days
            return days_ago
        except Exception as e:
            logger.debug(f"Could not parse date {date_str}: {e}")
            return None
    
    def _generate_core_extension_description(self, ext_name: str, stage: str) -> str:
        """Generate description for core extensions based on name and metadata."""
        descriptions = {
            'autocomplete': 'Auto-completion support for DuckDB CLI',
            'avro': 'Apache Avro format support for reading and writing',
            'aws': 'AWS S3 integration and cloud services support',
            'azure': 'Azure Blob Storage integration and cloud services',
            'delta': 'Delta Lake format support for ACID transactions',
            'ducklake': 'Delta Lake support via DuckLake implementation',
            'encodings': 'Character encoding support for text processing',
            'excel': 'Microsoft Excel file format support',
            'fts': 'Full-text search functionality and indexing',
            'httpfs': 'HTTP/S3 filesystem support for remote data',
            'iceberg': 'Apache Iceberg format support for data lakes',
            'icu': 'International Components for Unicode support',
            'inet': 'Internet address data types and functions',
            'jemalloc': 'Memory allocator for improved performance',
            'json': 'JSON data format support and functions',
            'mysql': 'MySQL database connectivity and integration',
            'parquet': 'Apache Parquet columnar format support',
            'postgres': 'PostgreSQL database connectivity and integration',
            'spatial': 'Geospatial data types and spatial functions',
            'sqlite': 'SQLite database connectivity and integration',
            'tpcds': 'TPC-DS benchmark data generation',
            'tpch': 'TPC-H benchmark data generation',
            'ui': 'Browser-based user interface for DuckDB',
            'vss': 'Vector similarity search capabilities'
        }
        
        return descriptions.get(ext_name.lower(), f"DuckDB core extension: {ext_name}")
    
    def _determine_core_extension_status(self, ext, duckdb_lag_days: int) -> str:
        """Determine status of core extension based on activity and metadata."""
        # For now, all core extensions are considered active
        # This could be enhanced later to detect deprecated extensions
        return "✅ Active"
    
    def _get_core_extension_repository_info(self, ext_name: str, ext_metadata: dict) -> tuple[str, str, str]:
        """Get repository link, stars, and language for core extension."""
        # Check if extension has external repository from metadata
        repo_path = ext_metadata.get("repository_path", "") if ext_metadata else ""
        
        # Check extension metadata for external repositories
        external_repos = self.metadata.metadata.get("core_extensions", {}).get("external_repositories", {})
        
        if ext_name.lower() in external_repos:
            # Extension has dedicated external repository
            repo_name = external_repos[ext_name.lower()]["repository"]
            repo_link = f"[{repo_name}](https://github.com/{repo_name})"
            
            # Try to get stars from the extension's repository info if available
            if ext_metadata and ext_metadata.get("repo_info"):
                stars = str(ext_metadata["repo_info"].get("stargazers_count", "—"))
            else:
                stars = "—"  # Stars not fetched yet
            language = "C++"  # Most DuckDB extensions are C++
        elif repo_path and repo_path.startswith("external:"):
            # Fallback: extract repo from external path
            repo_name = repo_path.replace("external:", "")
            repo_link = f"[{repo_name}](https://github.com/{repo_name})"
            stars = "—" 
            language = "C++"
        else:
            # Extension is in main DuckDB repository
            repo_link = "[duckdb/duckdb](https://github.com/duckdb/duckdb)"
            stars = "—"  # Don't show main repo stars as it's not meaningful
            language = "C++"
        
        return repo_link, stars, language
    
    
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
            "| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |",
            "|---|-----------|------------|--------|---------------|-------|----------|-------------|",
        ])
        
        # Discover core extension URLs
        extension_urls = self._discover_core_extension_urls()
        
        # Sort core extensions alphabetically
        sorted_core_extensions = sorted(analysis_result.core_extensions, key=lambda x: x.name.lower())
        
        for idx, ext in enumerate(sorted_core_extensions, 1):
            # Get extension details
            status = self._determine_core_extension_status(ext, duckdb_lag_days)
            description = self._generate_core_extension_description(ext.name, ext.stage or "Stable")
            repo_link, stars, language = self._get_core_extension_repository_info(ext.name, ext.metadata)
            
            # Calculate last activity
            if ext.metadata and ext.metadata.get("last_commit_date"):
                repo_path = ext.metadata.get("repository_path", "")
                if repo_path == "integrated_core":
                    last_activity = f"{duckdb_lag_days} days ago"
                elif repo_path.startswith("external:"):
                    last_activity = self._format_days_ago(ext.metadata["last_commit_date"], duckdb_lag_days)
                elif repo_path and repo_path != "not_found":
                    last_activity = self._format_days_ago(ext.metadata["last_commit_date"], duckdb_lag_days)
                else:
                    last_activity = f"~{duckdb_lag_days} days ago"
            else:
                last_activity = f"~{duckdb_lag_days} days ago"
            
            # Create extension name with URL if available
            extension_name = ext.name
            extension_url = extension_urls.get(ext.name.lower())
            if extension_url:
                extension_name = f"[{ext.name}]({extension_url})"
            
            report.append(f"| {idx} | **{extension_name}** | {repo_link} | {status} | {last_activity} | {stars} | {language} | {description} |")
        
        report.extend([
            f"\n**Total Core Extensions**: {len(analysis_result.core_extensions)}\n",
            "",
        ])
        
        # Community extensions section
        report.extend([
            "## Community Extensions\n",
            "| # | Extension | Repository | Status | Last Activity | Stars | Language | Description |",
            "|---|-----------|------------|--------|---------------|-------|----------|-------------|",
        ])
        
        # Sort community extensions alphabetically
        sorted_community_extensions = sorted(analysis_result.community_extensions, key=lambda x: x.name.lower())
        
        for idx, ext in enumerate(sorted_community_extensions, 1):
            # Determine status with enhanced logic
            if ext.metadata:
                raw_status = ext.metadata.get("status", "❌ Issues")
                if raw_status == "✅ Ongoing":
                    status = "✅ Active"
                elif raw_status == "🔴 Discontinued":
                    status = "🔴 Archived"
                else:
                    status = "❌ Issues"
            else:
                status = "❌ Issues"
            
            repo_link = f"[{ext.repository}](https://github.com/{ext.repository})" if ext.repository else "N/A"
            last_activity = f"{ext.days_ago} days ago" if ext.days_ago is not None else "Unknown"
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
            
            report.append(f"| {idx} | **{ext.name}** | {repo_link} | {status} | {last_activity} | {stars} | {language} | {description} |")
        
        # Community extensions summary
        active = sum(1 for ext in analysis_result.community_extensions 
                    if ext.metadata and ext.metadata.get("status") == "✅ Ongoing")
        archived = sum(1 for ext in analysis_result.community_extensions 
                          if ext.metadata and ext.metadata.get("status") == "🔴 Discontinued")
        issues = sum(1 for ext in analysis_result.community_extensions 
                    if ext.metadata and "❌" in ext.metadata.get("status", ""))
        total = len(analysis_result.community_extensions)
        
        report.extend([
            "\n### Community Extensions Summary",
            f"- **Total Extensions**: {total}",
            f"- **Active Extensions**: {active} ({active / total * 100:.1f}%)" if total > 0 else f"- **Active Extensions**: 0 (0%)",
            f"- **Archived Extensions**: {archived} ({archived / total * 100:.1f}%)" if total > 0 else f"- **Archived Extensions**: 0 (0%)",
            f"- **Extensions with Issues**: {issues} ({issues / total * 100:.1f}%)" if total > 0 else f"- **Extensions with Issues**: 0 (0%)",
            "",
        ])
        
        # Add DuckDB Release Information Appendix
        duckdb_appendix = self._load_template("duckdb_release_info.md")
        if duckdb_appendix:
            report.extend(["", duckdb_appendix])
        
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
    
    async def generate_url_validation_csv(self, analysis_result: AnalysisResult) -> str:
        """Generate CSV report of URL validation results for easy correction."""
        logger.info("Generating URL validation CSV report")
        
        validation_results = getattr(analysis_result, 'url_validation_results', {})
        if not validation_results:
            logger.warning("No URL validation results found")
            return None
        
        rows = []
        for url_key, result in validation_results.items():
            # Parse extension name and URL type from key
            if '_' in url_key:
                extension_name = url_key.rsplit('_', 1)[0]
                url_type = url_key.rsplit('_', 1)[1]
            else:
                extension_name = url_key
                url_type = 'unknown'
            
            rows.append({
                "Extension Name": extension_name,
                "URL Type": url_type,
                "Current URL": result.get('url', ''),
                "Status": result.get('status', 'UNKNOWN'),
                "HTTP Status Code": result.get('status_code', ''),
                "Error Message": result.get('error_message', ''),
                "Extension Name Found": result.get('extension_name_found', ''),
                "Content Validated": result.get('content_validation', ''),
                "Corrected URL": '',  # Empty column for user to fill in
                "Notes": ''  # Empty column for user notes
            })
        
        # Sort by status (broken/likely wrong first) then by extension name
        def sort_key(row):
            status_priority = {'BROKEN': 0, 'LIKELY_WRONG': 1, 'OK': 2}
            return (status_priority.get(row['Status'], 3), row['Extension Name'])
        
        rows.sort(key=sort_key)
        
        # Create DataFrame and save to CSV
        import pandas as pd
        df = pd.DataFrame(rows)
        timestamp = analysis_result.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        csv_filename = f"url_validation_results_{timestamp}.csv"
        csv_path = self.reports_dir / csv_filename
        
        self.config.ensure_directories()
        df.to_csv(csv_path, index=False)
        
        logger.info(f"URL validation CSV saved: {csv_path}")
        return str(csv_path)
    
    async def generate_markdown_template(self, analysis_result: AnalysisResult, template_name: str = 'full_analysis') -> str:
        """Generate markdown report using the new template system."""
        logger.info(f"Generating markdown report using template: {template_name}")
        
        try:
            # Convert AnalysisResult to dict format expected by template engine
            analysis_data = {
                'core_extensions': [],
                'community_extensions': [],
                'duckdb_version_info': {
                    'version': getattr(analysis_result, 'duckdb_version', None),
                    'release_date': getattr(analysis_result, 'duckdb_release_date', None)
                },
                'analysis_timestamp': analysis_result.analysis_timestamp,
                'url_validation_results': getattr(analysis_result, 'url_validation_results', {}),
                'stats': {}
            }
            
            # Convert core extensions
            extension_urls = self._discover_core_extension_urls()
            for ext in analysis_result.core_extensions:
                # Calculate actual days ago from metadata if available
                last_activity_days = 0  # Default for core extensions
                if ext.metadata and ext.metadata.get("last_commit_date"):
                    try:
                        from dateutil import parser
                        commit_date = parser.parse(ext.metadata["last_commit_date"])
                        last_activity_days = (datetime.now(commit_date.tzinfo) - commit_date).days
                    except Exception:
                        # If DuckDB release date is available, use that as reference
                        if analysis_result.duckdb_release_date:
                            last_activity_days = (analysis_result.analysis_timestamp.replace(tzinfo=None) - analysis_result.duckdb_release_date.replace(tzinfo=None)).days
                        else:
                            last_activity_days = 0
                elif analysis_result.duckdb_release_date:
                    # For core extensions without specific commit data, use DuckDB release age
                    last_activity_days = (analysis_result.analysis_timestamp.replace(tzinfo=None) - analysis_result.duckdb_release_date.replace(tzinfo=None)).days
                
                # Get meaningful description from metadata or use the extension's description
                description = ext.description
                if not description and ext.metadata:
                    # Try to get description from metadata
                    description = ext.metadata.get('description')
                
                # Use metadata system to get enhanced description if still not available
                if not description:
                    metadata_desc = self.metadata.get_extension_description(ext.name)
                    if metadata_desc:
                        description = metadata_desc
                    else:
                        description = f'Core DuckDB extension: {ext.name}'
                
                # For core extensions, use the main DuckDB repository unless it's an external extension
                repository_url = 'duckdb/duckdb'
                if ext.metadata and ext.metadata.get('repository_path', '').startswith('external:'):
                    repository_url = ext.metadata['repository_path'].replace('external:', '')
                elif ext.repository and ext.repository != 'integrated_core':
                    repository_url = ext.repository
                
                core_ext = {
                    'name': ext.name,
                    'repository': repository_url,
                    'docs_url': extension_urls.get(ext.name.lower()),
                    'status': 'ongoing',
                    'last_push_days': last_activity_days,
                    'stars': 0,  # Not applicable for core
                    'language': 'C++',
                    'description': description,
                    'featured': False,
                    'version': '',
                    'topics': []
                }
                analysis_data['core_extensions'].append(core_ext)
            
            # Convert community extensions
            for ext in analysis_result.community_extensions:
                repo_info = ext.metadata.get('repo_info', {}) if ext.metadata else {}
                
                community_ext = {
                    'name': ext.name,
                    'repository': ext.repository,
                    'docs_url': f"https://duckdb.org/community_extensions/extensions/{ext.name}.html",
                    'status': self._parse_status(ext.metadata.get('status', '❌ Error') if ext.metadata else '❌ Error'),
                    'last_push_days': ext.days_ago,
                    'stars': ext.stars or 0,
                    'language': repo_info.get('language', 'N/A'),
                    'description': ext.description or 'No description available',
                    'featured': getattr(ext, 'featured', False),
                    'version': '',
                    'topics': repo_info.get('topics', [])
                }
                analysis_data['community_extensions'].append(community_ext)
            
            # Generate report using template engine
            rendered_report = self.template_engine.render_report(template_name, analysis_data)
            return rendered_report
            
        except Exception as e:
            logger.error(f"Error generating template-based report: {e}")
            logger.info("Falling back to legacy report generation")
            return self.generate_markdown(analysis_result)
    
    def _parse_status(self, raw_status: str) -> str:
        """Parse status from raw format to standardized format."""
        if "✅" in raw_status or "Ongoing" in raw_status:
            return "ongoing"
        elif "🔴" in raw_status or "Discontinued" in raw_status or "Archived" in raw_status:
            return "archived" 
        else:
            return "unknown"
    
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
