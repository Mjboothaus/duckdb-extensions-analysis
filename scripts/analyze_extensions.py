#!/usr/bin/env python3
"""
Unified DuckDB Extensions Analysis Tool

This script provides comprehensive analysis of DuckDB extensions including:
- Community extensions analysis
- Core extensions analysis  
- Full analysis combining both
- Markdown report generation

Features intelligent caching to speed up subsequent runs.
"""

import argparse
import asyncio
import base64
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import sys
import os

import httpx
import requests
from bs4 import BeautifulSoup
import diskcache as dc
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import yaml

# Configure logger
logger.remove()
logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

# Configuration constants
GITHUB_API_BASE = "https://api.github.com"
COMMUNITY_REPO = "duckdb/community-extensions"
DUCKDB_REPO = "duckdb/duckdb"
DUCKDB_VERSION = "v1.4.0"
DUCKDB_RELEASE_DATE = datetime(2024, 12, 19)  # Correct DuckDB v1.4.0 release date
CURRENT_DATE = datetime.now()

# Set up caching
CACHE_DIR = Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)
cache = dc.Cache(str(CACHE_DIR))

# GitHub headers with optional token
HEADERS = {"Accept": "application/vnd.github.v3+json"}
if github_token := os.getenv("GITHUB_TOKEN"):
    HEADERS["Authorization"] = f"token {github_token}"
    logger.info("Using GitHub authentication token")
else:
    logger.warning("No GitHub token found. Consider setting GITHUB_TOKEN environment variable for higher rate limits.")


def get_cache_key(url: str, headers: Dict[str, str]) -> str:
    """Generate a cache key for a request."""
    key_data = f"{url}_{str(sorted(headers.items()))}"
    return hashlib.md5(key_data.encode()).hexdigest()


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((httpx.RequestError,)),
    before=lambda _: logger.debug("Retrying request..."),
)
async def fetch_github_api_cached(client: httpx.AsyncClient, url: str, cache_hours: int = 1) -> dict:
    """Fetch from GitHub API with intelligent caching."""
    cache_key = get_cache_key(url, HEADERS)
    
    # Check cache first
    cached_data = cache.get(cache_key)
    if cached_data:
        cached_time, data = cached_data
        if datetime.now() - cached_time < timedelta(hours=cache_hours):
            logger.debug(f"Using cached data for {url}")
            return data
    
    # Fetch fresh data
    logger.debug(f"Fetching fresh data from {url}")
    response = await client.get(url, headers=HEADERS, timeout=10, follow_redirects=True)
    response.raise_for_status()
    data = response.json()
    
    # Cache the response
    cache.set(cache_key, (datetime.now(), data))
    return data


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((requests.RequestException,)),
    before=lambda _: logger.debug("Retrying request..."),
)
def fetch_web_content_cached(url: str, cache_hours: int = 24) -> str:
    """Fetch web content with caching."""
    cache_key = get_cache_key(url, {})
    
    # Check cache first
    cached_data = cache.get(f"web_{cache_key}")
    if cached_data:
        cached_time, content = cached_data
        if datetime.now() - cached_time < timedelta(hours=cache_hours):
            logger.debug(f"Using cached web content for {url}")
            return content
    
    # Fetch fresh content
    logger.debug(f"Fetching fresh web content from {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    content = response.text
    
    # Cache the response
    cache.set(f"web_{cache_key}", (datetime.now(), content))
    return content


class ExtensionAnalyzer:
    """Main class for analyzing DuckDB extensions."""
    
    def __init__(self):
        self.core_extensions: List[Dict] = []
        self.community_extensions: List[str] = []
        self.extension_data: List[Dict] = []
    
    def get_core_extensions(self) -> List[Dict]:
        """Fetch core extensions from DuckDB documentation."""
        if self.core_extensions:
            return self.core_extensions
            
        logger.info("Fetching core extensions from DuckDB documentation")
        url = "https://duckdb.org/docs/stable/core_extensions/overview.html"
        html = fetch_web_content_cached(url)
        soup = BeautifulSoup(html, "html.parser")

        # Parse the table for extensions and stages
        table = soup.find("table")
        if not table:
            logger.warning("Could not find core extensions table")
            return []

        rows = table.find_all("tr")[1:]  # Skip header
        extensions = []
        for row in rows:
            cols = row.find_all(["td", "th"])
            if len(cols) >= 2:
                name = cols[0].get_text(strip=True)
                stage = cols[1].get_text(strip=True)
                extensions.append({"name": name, "stage": stage})

        self.core_extensions = extensions
        logger.info(f"Found {len(extensions)} core extensions from DuckDB {DUCKDB_VERSION}")
        return extensions
    
    async def get_community_extensions(self, client: httpx.AsyncClient) -> List[str]:
        """Fetch community extensions list from GitHub."""
        if self.community_extensions:
            return self.community_extensions
            
        logger.info("Fetching community extensions list")
        contents_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions"
        contents = await fetch_github_api_cached(client, contents_url)
        extensions = [item["name"] for item in contents if item["type"] == "dir"]
        
        self.community_extensions = extensions
        logger.info(f"Found {len(extensions)} community extensions")
        return extensions
    
    async def get_extension_metadata(self, client: httpx.AsyncClient, ext_name: str) -> Optional[Dict]:
        """Get metadata for a community extension."""
        metadata_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions/{ext_name}/description.yml"
        try:
            metadata_raw = await fetch_github_api_cached(client, metadata_url)
            metadata_content = base64.b64decode(metadata_raw["content"]).decode("utf-8")
            metadata = yaml.safe_load(metadata_content)
            return metadata
        except httpx.HTTPStatusError as e:
            logger.warning(f"Description not found for {ext_name}: {e}")
            return None
    
    async def get_repository_info(self, client: httpx.AsyncClient, repo: str) -> Optional[Dict]:
        """Get detailed repository information from GitHub API."""
        repo_url = f"{GITHUB_API_BASE}/repos/{repo}"
        try:
            repo_data = await fetch_github_api_cached(client, repo_url, cache_hours=0.5)  # Shorter cache for repo info
            return {
                "archived": repo_data.get("archived", False),
                "last_push": repo_data.get("pushed_at"),
                "stars": repo_data.get("stargazers_count", 0),
                "forks": repo_data.get("forks_count", 0),
                "language": repo_data.get("language"),
                "description": repo_data.get("description"),
                "license": repo_data.get("license", {}).get("spdx_id") if repo_data.get("license") else None,
                "created_at": repo_data.get("created_at"),
                "updated_at": repo_data.get("updated_at"),
                "homepage": repo_data.get("homepage"),
                "topics": repo_data.get("topics", []),
                "full_name": repo_data.get("full_name"),
            }
        except Exception as e:
            logger.error(f"Failed to get repository info for {repo}: {e}")
            return None
    
    def calculate_days_ago(self, date_str: str) -> Optional[int]:
        """Calculate days ago from an ISO date string."""
        if not date_str:
            return None
        try:
            date = datetime.fromisoformat(date_str.rstrip("Z"))
            return (CURRENT_DATE - date).days
        except (ValueError, TypeError):
            return None
    
    async def analyze_community_extensions(self, client: httpx.AsyncClient) -> Tuple[List[Dict], Dict]:
        """Analyze community extensions and return detailed data and statistics."""
        extensions = await self.get_community_extensions(client)
        extension_data = []
        
        for ext in extensions:
            logger.info(f"Processing {ext}")
            metadata = await self.get_extension_metadata(client, ext)
            
            ext_info = {
                "name": ext,
                "metadata": metadata,
                "repo_info": None,
                "error": None,
                "status": "❌ Error",
                "last_push_days": None,
            }
            
            if metadata and "repo" in metadata and "github" in metadata["repo"]:
                repo = metadata["repo"]["github"]
                repo_info = await self.get_repository_info(client, repo)
                if repo_info:
                    ext_info["repo_info"] = repo_info
                    ext_info["last_push_days"] = self.calculate_days_ago(repo_info["last_push"])
                    
                    if repo_info["archived"]:
                        ext_info["status"] = "🔴 Discontinued"
                    else:
                        ext_info["status"] = "✅ Ongoing"
                else:
                    ext_info["error"] = "Failed to fetch repository info"
            else:
                ext_info["error"] = "No repository found"
                
            extension_data.append(ext_info)
        
        # Sort by last activity (most recent first)
        extension_data.sort(
            key=lambda x: x["last_push_days"] if x["last_push_days"] is not None else 999999
        )
        
        # Calculate statistics
        stats = {
            "total": len(extension_data),
            "active": sum(1 for ext in extension_data if ext["status"] == "✅ Ongoing"),
            "discontinued": sum(1 for ext in extension_data if ext["status"] == "🔴 Discontinued"),
            "errors": sum(1 for ext in extension_data if ext["status"] == "❌ Error"),
        }
        
        self.extension_data = extension_data
        return extension_data, stats
    
    def print_community_analysis(self, extension_data: List[Dict], stats: Dict):
        """Print community extensions analysis to console."""
        logger.info("=== Community Extensions Analysis ===")
        
        for ext_info in extension_data:
            name = ext_info["name"]
            status = ext_info["status"]
            
            if ext_info["repo_info"]:
                repo = ext_info["metadata"]["repo"]["github"]
                last_push_days = ext_info["last_push_days"]
                last_push_str = f"{last_push_days} days ago" if last_push_days is not None else "Unknown"
                logger.info(f"{name} (Repo: {repo}): {status.replace('✅ ', '').replace('🔴 ', '').replace('❌ ', '')} | Last push: {last_push_str}")
            else:
                logger.info(f"{name}: {ext_info['error']}")
        
        logger.info(f"\n=== Community Extensions Summary ===")
        logger.info(f"Total: {stats['total']}")
        logger.info(f"Active: {stats['active']} ({stats['active']/stats['total']*100:.1f}%)")
        logger.info(f"Discontinued: {stats['discontinued']} ({stats['discontinued']/stats['total']*100:.1f}%)")
        logger.info(f"Errors: {stats['errors']} ({stats['errors']/stats['total']*100:.1f}%)")
    
    def print_core_analysis(self):
        """Print core extensions analysis to console."""
        logger.info("=== Core Extensions Analysis ===")
        
        extensions = self.get_core_extensions()
        duckdb_lag_days = (CURRENT_DATE - DUCKDB_RELEASE_DATE).days
        
        for ext in extensions:
            stage = ext['stage'] if ext['stage'] else 'Stable'
            logger.info(f"{ext['name']} (Core, Stage: {stage}): Ongoing | Last updated: {duckdb_lag_days} days ago (in {DUCKDB_VERSION})")
        
        logger.info(f"\n=== Core Extensions Summary ===")
        logger.info(f"Total: {len(extensions)}")
        logger.info(f"All core extensions are ongoing and updated with DuckDB releases")
    
    def generate_markdown_report(self, extension_data: List[Dict], stats: Dict) -> str:
        """Generate comprehensive markdown report."""
        logger.info("Generating markdown report")
        
        # Report header
        report = [
            f"# DuckDB Extensions Status Report",
            f"",
            f"Generated on: **{CURRENT_DATE.strftime('%Y-%m-%d %H:%M:%S UTC')}**",
            f"",
            f"This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.",
            f"",
        ]
        
        # Core extensions section
        core_extensions = self.get_core_extensions()
        duckdb_lag_days = (CURRENT_DATE - DUCKDB_RELEASE_DATE).days
        
        report.extend([
            "## Core Extensions\n",
            f"DuckDB core extensions from version **{DUCKDB_VERSION}** (released {duckdb_lag_days} days ago).\n",
            "| Extension | Development Stage | Status | Last Updated |",
            "|-----------|-------------------|--------|--------------|",
        ])
        
        for ext in core_extensions:
            stage = ext['stage'] if ext['stage'] else 'Stable'
            status = "✅ Ongoing"
            last_updated = f"{duckdb_lag_days} days ago (in {DUCKDB_VERSION})"
            report.append(f"| **{ext['name']}** | {stage} | {status} | {last_updated} |")
        
        report.extend([
            f"\n**Total Core Extensions**: {len(core_extensions)}\n",
            "",
        ])
        
        # Community extensions section
        report.extend([
            "## Community Extensions\n",
            "| Extension | Repository | Status | Last Push | Stars | Language | Description |",
            "|-----------|------------|--------|-----------|-------|----------|-------------|",
        ])
        
        for ext_info in extension_data:
            name = ext_info["name"]
            
            if ext_info["error"]:
                status = "❌ No Repo"
                repo_link = "N/A"
                last_push = "N/A"
                stars = "N/A"
                language = "N/A"
                description = ext_info["error"]
            elif ext_info["repo_info"]:
                repo_info = ext_info["repo_info"]
                repo = ext_info["metadata"]["repo"]["github"]
                repo_link = f"[{repo}](https://github.com/{repo})"
                status = ext_info["status"]
                
                last_push_days = ext_info["last_push_days"]
                last_push = f"{last_push_days} days ago" if last_push_days is not None else "Unknown"
                stars = str(repo_info["stars"])
                language = repo_info["language"] or "N/A"
                description = (repo_info["description"] or "No description")[:50]
                if len(repo_info["description"] or "") > 50:
                    description += "..."
            else:
                status = "❌ Error"
                repo_link = "N/A"
                last_push = "N/A"
                stars = "N/A"
                language = "N/A"
                description = "Failed to fetch info"
            
            # Escape pipe characters in description
            description = description.replace("|", "\\|")
            
            report.append(f"| **{name}** | {repo_link} | {status} | {last_push} | {stars} | {language} | {description} |")
        
        # Community extensions summary
        report.extend([
            f"\n### Community Extensions Summary",
            f"- **Total Extensions**: {stats['total']}",
            f"- **Active Extensions**: {stats['active']} ({stats['active']/stats['total']*100:.1f}%)",
            f"- **Discontinued Extensions**: {stats['discontinued']} ({stats['discontinued']/stats['total']*100:.1f}%)",
            f"- **Extensions with Issues**: {stats['errors']} ({stats['errors']/stats['total']*100:.1f}%)",
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
            f"Report generated using the [duckdb-extensions-analysis](https://github.com/Mjboothaus/duckdb-extensions-analysis) tool.",
        ])
        
        return "\n".join(report)
    
    def save_report(self, content: str) -> Tuple[Path, Path]:
        """Save the markdown report to files."""
        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)
        
        timestamp = CURRENT_DATE.strftime("%Y%m%d_%H%M%S")
        report_file = report_dir / f"duckdb_extensions_report_{timestamp}.md"
        latest_file = report_dir / "latest.md"
        
        # Save timestamped report
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Save latest report
        with open(latest_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        return report_file, latest_file


async def main():
    """Main function with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Analyze DuckDB extensions with intelligent caching",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s community           # Analyze only community extensions
    %(prog)s core               # Analyze only core extensions  
    %(prog)s full               # Analyze both core and community
    %(prog)s report             # Generate markdown report
    %(prog)s --clear-cache      # Clear cache and run full analysis
        """
    )
    
    parser.add_argument(
        "mode",
        choices=["community", "core", "full", "report"],
        help="Analysis mode to run"
    )
    
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear cache before running analysis"
    )
    
    parser.add_argument(
        "--cache-info",
        action="store_true",
        help="Show cache statistics"
    )
    
    args = parser.parse_args()
    
    # Handle cache operations
    if args.clear_cache:
        logger.info("Clearing cache...")
        cache.clear()
        logger.info("Cache cleared")
    
    if args.cache_info:
        logger.info(f"Cache directory: {CACHE_DIR}")
        logger.info(f"Cache size: {len(cache)} entries")
        logger.info(f"Cache disk usage: {sum(f.stat().st_size for f in CACHE_DIR.rglob('*') if f.is_file()) / 1024 / 1024:.2f} MB")
    
    # Initialize analyzer
    analyzer = ExtensionAnalyzer()
    
    # Run analysis based on mode
    if args.mode == "core":
        logger.info("Starting core extensions analysis")
        analyzer.print_core_analysis()
        
    elif args.mode == "community":
        logger.info("Starting community extensions analysis")
        async with httpx.AsyncClient() as client:
            extension_data, stats = await analyzer.analyze_community_extensions(client)
            analyzer.print_community_analysis(extension_data, stats)
            
    elif args.mode == "full":
        logger.info("Starting full extensions analysis")
        analyzer.print_core_analysis()
        async with httpx.AsyncClient() as client:
            extension_data, stats = await analyzer.analyze_community_extensions(client)
            analyzer.print_community_analysis(extension_data, stats)
            
    elif args.mode == "report":
        logger.info("Generating comprehensive markdown report")
        async with httpx.AsyncClient() as client:
            extension_data, stats = await analyzer.analyze_community_extensions(client)
            report_content = analyzer.generate_markdown_report(extension_data, stats)
            
            report_file, latest_file = analyzer.save_report(report_content)
            logger.info(f"Report generated successfully: {report_file}")
            logger.info(f"Latest report updated: {latest_file}")


if __name__ == "__main__":
    logger.info("Starting DuckDB extensions analysis")
    asyncio.run(main())
    logger.info("Analysis complete")