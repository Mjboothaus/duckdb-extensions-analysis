"""
Report Generator for DuckDB Extensions Analysis.

Handles generation of reports in multiple formats (Markdown, CSV, Excel).
"""

from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

import pandas as pd
from loguru import logger

from .base import BaseReportGenerator, AnalysisResult, ExtensionInfo


class ReportGenerator(BaseReportGenerator):
    """Unified report generator for multiple formats."""
    
    def __init__(self, config):
        super().__init__(config)
        self.reports_dir = config.reports_dir
    
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
        
        # Report header
        report = [
            "# DuckDB Extensions Status Report",
            "",
            f"Generated on: **{timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}**",
            "",
            "This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.",
            "",
        ]
        
        # Core extensions section
        report.extend([
            "## Core Extensions\n",
            f"DuckDB core extensions from version **{duckdb_version}** (released {duckdb_lag_days} days ago).\n",
            "| Extension | Development Stage | Status | Last Updated |",
            "|-----------|-------------------|--------|--------------|",
        ])
        
        for ext in analysis_result.core_extensions:
            stage = ext.stage or "Stable"
            status = "✅ Ongoing"
            last_updated = f"{duckdb_lag_days} days ago (in {duckdb_version})"
            report.append(f"| **{ext.name}** | {stage} | {status} | {last_updated} |")
        
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
        
        # Add methodology section
        report.extend([
            "## Methodology",
            "",
            "- **Core Extensions**: Information gathered from the official DuckDB documentation",
            "- **Community Extensions**: Information gathered from the `duckdb/community-extensions` repository and individual extension repositories",
            "- **Status Determination**:",
            "  - ✅ **Ongoing**: Repository is active and not archived",
            "  - 🔴 **Discontinued**: Repository is archived or marked as discontinued",
            "  - ❌ **No Repo/Error**: Repository information unavailable or inaccessible",
            "- **Activity Metrics**: Based on the last push/commit date to the repository",
            "- **Caching**: API responses are cached to improve performance and reduce rate limiting",
            "",
            "Report generated using the [duckdb-extensions-analysis](https://github.com/Mjboothaus/duckdb-extensions-analysis) tool.",
        ])
        
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