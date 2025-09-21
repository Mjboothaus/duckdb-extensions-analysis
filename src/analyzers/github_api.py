"""
GitHub API client for DuckDB Extensions Analysis.

Provides centralized GitHub API access with intelligent caching and error handling.
"""

import hashlib
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

import httpx
import diskcache as dc
from loguru import logger
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


class GitHubAPIClient:
    """GitHub API client with caching and retry logic."""
    
    def __init__(self, config, cache_hours: int = 1):
        self.config = config
        self.cache_hours = cache_hours
        self.cache = dc.Cache(str(config.cache_dir))
        self.headers = config.headers
        self.github_api_base = config.github_api_base
        self.community_repo = config.community_repo
        self.duckdb_repo = config.duckdb_repo
    
    def get_cache_key(self, url: str, headers: Dict[str, str]) -> str:
        """Generate a cache key for a request."""
        key_data = f"{url}_{str(sorted(headers.items()))}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((httpx.RequestError, httpx.HTTPStatusError)),
        before=lambda _: logger.debug("Retrying GitHub API request..."),
    )
    async def fetch_cached(
        self, client: httpx.AsyncClient, url: str, cache_hours: Optional[int] = None
    ) -> dict:
        """Fetch from GitHub API with intelligent caching."""
        cache_hours = cache_hours or self.cache_hours
        cache_key = self.get_cache_key(url, self.headers)

        # Check cache first
        cached_data = self.cache.get(cache_key)
        if cached_data:
            cached_time, data = cached_data
            if datetime.now() - cached_time < timedelta(hours=cache_hours):
                logger.debug(f"Using cached data for {url}")
                return data

        # Fetch fresh data
        logger.debug(f"Fetching fresh data from {url}")
        response = await client.get(url, headers=self.headers, timeout=10, follow_redirects=True)
        response.raise_for_status()
        data = response.json()

        # Cache the response
        self.cache.set(cache_key, (datetime.now(), data))
        return data
    
    async def get_repository_info(self, client: httpx.AsyncClient, repo_path: str) -> Optional[Dict]:
        """Get repository information from GitHub API."""
        try:
            url = f"{self.github_api_base}/repos/{repo_path}"
            return await self.fetch_cached(client, url)
        except Exception as e:
            logger.warning(f"Failed to fetch repository info for {repo_path}: {e}")
            return None
    
    async def get_repository_commits(
        self, client: httpx.AsyncClient, repo_path: str, path: Optional[str] = None, limit: int = 1
    ) -> List[Dict]:
        """Get repository commits, optionally filtered by path."""
        try:
            url = f"{self.github_api_base}/repos/{repo_path}/commits"
            params = {"per_page": limit}
            if path:
                params["path"] = path
            
            # Add params to URL
            param_str = "&".join([f"{k}={v}" for k, v in params.items()])
            full_url = f"{url}?{param_str}"
            
            commits = await self.fetch_cached(client, full_url)
            return commits if isinstance(commits, list) else []
        except Exception as e:
            logger.warning(f"Failed to fetch commits for {repo_path}: {e}")
            return []
    
    async def get_community_extensions_list(self, client: httpx.AsyncClient) -> List[str]:
        """Fetch the list of community extensions from the community repo."""
        try:
            # Fetch directory listing of extensions
            url = f"{self.github_api_base}/repos/{self.community_repo}/contents/extensions"
            contents = await self.fetch_cached(client, url)
            
            # Extract directory names (each extension has its own directory)
            extensions = [item["name"] for item in contents if item["type"] == "dir"]
            
            return extensions
        except Exception as e:
            logger.error(f"Failed to fetch community extensions list: {e}")
            return []
    
    async def get_latest_duckdb_release(self, client: httpx.AsyncClient) -> tuple[Optional[str], Optional[datetime]]:
        """Get the latest DuckDB release information."""
        try:
            url = f"{self.github_api_base}/repos/{self.duckdb_repo}/releases/latest"
            release_data = await self.fetch_cached(client, url)
            
            if release_data and "tag_name" in release_data:
                version = release_data["tag_name"]
                published_at = release_data.get("published_at")
                
                if published_at:
                    # Parse the ISO format date
                    release_date = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
                    return version, release_date
                
                return version, None
            
            return None, None
        except Exception as e:
            logger.warning(f"Failed to fetch latest DuckDB release: {e}")
            # Fallback to configured values
            # Return None for both values since config doesn't have fallback attribute
            return None, None
    
    async def get_duckdb_releases(self, client: httpx.AsyncClient, limit: int = 10) -> List[Dict]:
        """Get recent DuckDB releases with comprehensive information."""
        try:
            url = f"{self.github_api_base}/repos/{self.duckdb_repo}/releases"
            params = {"per_page": limit}
            param_str = "&".join([f"{k}={v}" for k, v in params.items()])
            full_url = f"{url}?{param_str}"
            
            releases_data = await self.fetch_cached(client, full_url)
            
            if not isinstance(releases_data, list):
                return []
            
            processed_releases = []
            for release in releases_data:
                if "tag_name" in release:
                    processed_release = {
                        "version": release["tag_name"],
                        "name": release.get("name", release["tag_name"]),
                        "published_at": release.get("published_at"),
                        "prerelease": release.get("prerelease", False),
                        "draft": release.get("draft", False),
                        "body": release.get("body", ""),
                        "html_url": release.get("html_url", ""),
                        "assets_count": len(release.get("assets", [])),
                        "author": release.get("author", {}).get("login", "unknown")
                    }
                    
                    # Parse and add formatted date
                    if processed_release["published_at"]:
                        try:
                            pub_date = datetime.fromisoformat(processed_release["published_at"].replace("Z", "+00:00"))
                            processed_release["published_date"] = pub_date
                            processed_release["days_ago"] = (datetime.now().replace(tzinfo=pub_date.tzinfo) - pub_date).days
                        except Exception:
                            processed_release["published_date"] = None
                            processed_release["days_ago"] = None
                    
                    processed_releases.append(processed_release)
            
            return processed_releases
        except Exception as e:
            logger.warning(f"Failed to fetch DuckDB releases: {e}")
            return []
