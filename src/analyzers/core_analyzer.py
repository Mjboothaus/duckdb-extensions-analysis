"""
Core Extensions Analyzer for DuckDB Extensions Analysis.

Handles analysis of DuckDB core extensions from official documentation.
"""

import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import platform

import httpx
import requests
from bs4 import BeautifulSoup
from loguru import logger
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from .base import BaseAnalyzer, ExtensionInfo
from .github_api import GitHubAPIClient


class WebContentClient:
    """Client for fetching web content with caching."""
    
    def __init__(self, config):
        self.config = config
        # Set up cache from configuration
        import diskcache as dc
        self.cache = dc.Cache(str(config.cache_dir))
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((requests.RequestException,)),
        before=lambda _: logger.debug("Retrying web content request..."),
    )
    def fetch_cached(self, url: str, cache_hours: int = 24) -> str:
        """Fetch web content with caching."""
        import hashlib
        from datetime import timedelta
        
        cache_key = f"web_{hashlib.md5(url.encode()).hexdigest()}"

        # Check cache first if available
        if self.cache:
            cached_data = self.cache.get(cache_key)
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

        # Cache the response if cache available
        if self.cache:
            self.cache.set(cache_key, (datetime.now(), content))
        
        return content


class CoreExtensionAnalyzer(BaseAnalyzer):
    """Analyzer for DuckDB core extensions."""
    
    def __init__(self, config, github_client: GitHubAPIClient, cache_hours: int = 1):
        super().__init__(config, cache_hours)
        self.github_client = github_client
        self.web_client = WebContentClient(config)
        self.core_extensions: List[Dict] = []
        self.extensions_base_url = "https://extensions.duckdb.org"
        # Platform identifiers used by DuckDB extension repository
        self.platforms = {
            'linux_amd64': 'Linux x64',
            'linux_arm64': 'Linux ARM64', 
            'osx_amd64': 'macOS x64',
            'osx_arm64': 'macOS ARM64',
            'windows_amd64': 'Windows x64'
        }
        self.current_platform = self._detect_current_platform()
        
        # Known repository paths for core extensions in DuckDB repository
        self.core_extension_paths = {
            'autocomplete': 'extension/autocomplete',
            'delta': 'extension/delta', 
            'excel': 'extension/excel',
            'fts': 'extension/fts',
            'httpfs': 'extension/httpfs',
            'icu': 'extension/icu',
            'inet': 'extension/inet',
            'jemalloc': 'extension/jemalloc',
            'json': 'extension/json',
            'parquet': 'extension/parquet',  # In the main repo directory
            'tpcds': 'extension/tpcds',
            'tpch': 'extension/tpch',
            # Extensions without dedicated directories - these are integrated into core DuckDB
            # and their "updates" are typically part of general DuckDB releases
            'avro': None,  # Integrated into core
            'aws': None,   # Integrated into core  
            'azure': None, # Integrated into core
            'ducklake': None, # Integrated into core
            'encodings': None, # Integrated into core
            'iceberg': None,   # Integrated into core
            'mysql': None,     # Integrated into core
            'postgres': None,  # Integrated into core
            'spatial': None,   # Integrated into core
            'sqlite': None,    # Integrated into core
            'ui': None,        # Integrated into core
            'vss': None,       # Integrated into core
        }
    
    def get_core_extensions_from_docs(self) -> List[Dict]:
        """Fetch core extensions from DuckDB documentation."""
        if self.core_extensions:
            return self.core_extensions

        logger.info("Fetching core extensions from DuckDB documentation")
        url = self.config.core_extensions_url
        html = self.web_client.fetch_cached(url, cache_hours=self.config.web_cache_hours)
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
        logger.info(
            f"Found {len(extensions)} core extensions from DuckDB documentation"
        )
        return extensions
    
    async def get_core_extension_github_info(
        self, client: httpx.AsyncClient, ext_name: str
    ) -> Optional[Dict]:
        """Get GitHub repository information for core extensions using known paths."""
        repo_path = self.core_extension_paths.get(ext_name)
        
        if repo_path is None:
            # This extension is integrated into core DuckDB without a dedicated directory
            logger.debug(f"Extension {ext_name} is integrated into core DuckDB (no dedicated directory)")
            return {
                "repository_path": "integrated_core",
                "note": "This extension is integrated into core DuckDB without a dedicated source directory"
            }
        
        if not repo_path:
            # Fallback to the old method for completely unknown extensions
            logger.debug(f"No known repository path for {ext_name}, using fallback")
            return await self._get_github_info_fallback(client, ext_name)
        
        try:
            commits = await self.github_client.get_repository_commits(
                client, self.github_client.duckdb_repo, repo_path, limit=1
            )

            if commits and len(commits) > 0:
                last_commit = commits[0]
                return {
                    "last_commit_date": last_commit["commit"]["committer"]["date"],
                    "last_commit_sha": last_commit["sha"],
                    "last_commit_message": last_commit["commit"]["message"][:100],
                    "repository_path": repo_path
                }
        except Exception as e:
            logger.debug(
                f"Could not get GitHub info for {ext_name} at {repo_path}: {e}"
            )

        return {"repository_path": repo_path}
    
    async def _get_github_info_fallback(
        self, client: httpx.AsyncClient, ext_name: str
    ) -> Optional[Dict]:
        """Fallback method for extensions without known repository paths."""
        try:
            commits = await self.github_client.get_repository_commits(
                client, self.github_client.duckdb_repo, f"extensions/{ext_name}", limit=1
            )

            if commits and len(commits) > 0:
                last_commit = commits[0]
                return {
                    "last_commit_date": last_commit["commit"]["committer"]["date"],
                    "last_commit_sha": last_commit["sha"],
                    "last_commit_message": last_commit["commit"]["message"][:100],
                    "repository_path": f"extensions/{ext_name}"
                }
        except Exception as e:
            logger.debug(f"Fallback GitHub lookup failed for {ext_name}: {e}")

        return {"repository_path": "not_found"}
    
    async def get_featured_extensions(self, client: httpx.AsyncClient) -> set[str]:
        """Get the list of featured community extensions from the official DuckDB website."""
        try:
            logger.info("Fetching featured extensions list from DuckDB website")
            featured_extensions = set()

            for url in self.config.featured_extensions_pages:
                try:
                    html = self.web_client.fetch_cached(url, cache_hours=self.cache_hours)
                    soup = BeautifulSoup(html, "html.parser")

                    # Look for extension names in various formats
                    for element in soup.find_all(["code", "strong", "b"]):
                        text = element.get_text(strip=True)
                        # Filter for extension-like names
                        if self._is_valid_extension_name(text):
                            featured_extensions.add(text.lower())

                    # Also look for extension names in links
                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        if "extension" in href.lower() or "community" in href.lower():
                            text = link.get_text(strip=True)
                            if self._is_valid_extension_name(text):
                                featured_extensions.add(text.lower())

                except Exception as e:
                    logger.debug(f"Failed to fetch from {url}: {e}")
                    continue

            # If we can't find featured extensions dynamically, use the configured popular list
            if len(featured_extensions) < 5:
                logger.warning(
                    "Could not detect featured extensions dynamically, using configured popular list"
                )
                featured_extensions = set(self.config.popular_extensions)

            logger.info(f"Found {len(featured_extensions)} featured extensions")
            return featured_extensions

        except Exception as e:
            logger.warning(f"Failed to get featured extensions: {e}")
            return set(self.config.popular_extensions)
    
    def _is_valid_extension_name(self, text: str) -> bool:
        """Check if a text string looks like a valid extension name."""
        return (
            text
            and len(text) > 2
            and len(text) < 30
            and text.replace("_", "")
            .replace("-", "")
            .replace(".", "")
            .isalnum()
            and not text.startswith("http")
            and "/" not in text
            and " " not in text
        )
    
    async def analyze(self) -> List[ExtensionInfo]:
        """Analyze core extensions and return ExtensionInfo objects."""
        extensions = self.get_core_extensions_from_docs()
        extension_infos = []
        
        async with httpx.AsyncClient() as client:
            for ext in extensions:
                # Get GitHub info if available
                github_info = await self.get_core_extension_github_info(client, ext["name"])
                
                # Create ExtensionInfo object
                ext_info = ExtensionInfo(
                    name=ext["name"],
                    type="core",
                    stage=ext["stage"],
                    repository=f"{self.github_client.duckdb_repo}/extensions/{ext['name']}"
                )
                
                # Add GitHub metadata if available
                if github_info:
                    ext_info.metadata = github_info
                    ext_info.last_push = github_info.get("last_commit_date")
                
                extension_infos.append(ext_info)
        
        return extension_infos
    
    def _detect_current_platform(self) -> str:
        """Detect the current platform for DuckDB extension format."""
        system = platform.system().lower()
        machine = platform.machine().lower()
        
        if system == 'linux':
            if machine in ['x86_64', 'amd64']:
                return 'linux_amd64'
            elif machine in ['aarch64', 'arm64']:
                return 'linux_arm64'
        elif system == 'darwin':
            if machine in ['x86_64', 'amd64']:
                return 'osx_amd64' 
            elif machine in ['arm64']:
                return 'osx_arm64'
        elif system == 'windows':
            if machine in ['x86_64', 'amd64']:
                return 'windows_amd64'
        
        return 'unknown'
    
    async def _check_extension_availability(self, extension_name: str, version: str, platform: str) -> Tuple[bool, Optional[datetime], Optional[str]]:
        """Check if an extension is available for download on a specific platform.
        
        Returns:
            (is_available, availability_date, error_message)
        """
        url = f"{self.extensions_base_url}/{version}/{platform}/{extension_name}.duckdb_extension.gz"
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                # First check if file exists
                response = await client.head(url)
                
                if response.status_code == 200:
                    # Try to get last-modified date as proxy for availability date
                    last_modified = response.headers.get('last-modified')
                    availability_date = None
                    
                    if last_modified:
                        try:
                            from email.utils import parsedate_to_datetime
                            availability_date = parsedate_to_datetime(last_modified)
                        except Exception as e:
                            logger.debug(f"Could not parse last-modified date for {extension_name}: {e}")
                    
                    # Check file size as basic validation
                    content_length = response.headers.get('content-length')
                    if content_length and int(content_length) > 1000:  # Reasonable minimum size
                        return True, availability_date, None
                    else:
                        return False, None, f"Extension file too small ({content_length} bytes)"
                        
                elif response.status_code == 404:
                    return False, None, "Extension not found"
                else:
                    return False, None, f"HTTP {response.status_code}"
                    
        except Exception as e:
            logger.debug(f"Error checking {extension_name} on {platform}: {e}")
            return False, None, str(e)
    
    async def _check_extension_across_platforms(self, extension_name: str, version: str) -> Dict[str, Dict]:
        """Check extension availability across all platforms.
        
        Returns:
            Dict mapping platform -> {available, date, error, platform_name}
        """
        platform_results = {}
        
        # Check all platforms concurrently
        tasks = []
        for platform_id in self.platforms.keys():
            task = self._check_extension_availability(extension_name, version, platform_id)
            tasks.append((platform_id, task))
        
        results = await asyncio.gather(*[task for _, task in tasks], return_exceptions=True)
        
        for (platform_id, _), result in zip(tasks, results):
            if isinstance(result, Exception):
                platform_results[platform_id] = {
                    'available': False,
                    'date': None,
                    'error': str(result),
                    'platform_name': self.platforms[platform_id]
                }
            else:
                available, date, error = result
                platform_results[platform_id] = {
                    'available': available,
                    'date': date,
                    'error': error,
                    'platform_name': self.platforms[platform_id]
                }
        
        return platform_results
    
    async def analyze_with_platform_availability(self, duckdb_version: str) -> List[ExtensionInfo]:
        """Analyze core extensions with detailed platform availability information."""
        extensions = self.get_core_extensions_from_docs()
        extension_infos = []
        
        async with httpx.AsyncClient() as client:
            for ext in extensions:
                # Get GitHub info if available
                github_info = await self.get_core_extension_github_info(client, ext["name"])
                
                # Check platform availability
                platform_availability = await self._check_extension_across_platforms(ext["name"], duckdb_version)
                
                # Create ExtensionInfo object
                ext_info = ExtensionInfo(
                    name=ext["name"],
                    type="core",
                    stage=ext["stage"],
                    repository=f"{self.github_client.duckdb_repo}/extensions/{ext['name']}"
                )
                
                # Add GitHub metadata if available
                if github_info:
                    ext_info.metadata = github_info
                    ext_info.last_push = github_info.get("last_commit_date")
                
                # Add platform availability information
                ext_info.platform_availability = platform_availability
                
                # Determine overall availability status and earliest date
                available_platforms = [p for p, data in platform_availability.items() if data['available']]
                if available_platforms:
                    # Find earliest availability date across platforms
                    earliest_date = None
                    for platform_data in platform_availability.values():
                        if platform_data['available'] and platform_data['date']:
                            if earliest_date is None or platform_data['date'] < earliest_date:
                                earliest_date = platform_data['date']
                    
                    ext_info.availability_date = earliest_date
                    ext_info.available_platforms = available_platforms
                
                extension_infos.append(ext_info)
        
        return extension_infos
