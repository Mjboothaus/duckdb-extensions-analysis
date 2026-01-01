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
from aiolimiter import AsyncLimiter
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
        
        # Rate limiter: 1 request per second to avoid secondary rate limits
        # GitHub's documented limit is 5000/hour (1.4/sec), but secondary limits are MUCH stricter
        # Secondary limits detect "abuse patterns" like rapid sequential requests
        # Being very conservative at 1/sec (3600/hour) avoids 403 errors from abuse detection
        # With 12-hour cache, most requests are cached anyway, so impact is minimal
        self.rate_limiter = AsyncLimiter(max_rate=1, time_period=1)
    
    def get_cache_key(self, url: str, headers: Dict[str, str]) -> str:
        """Generate a cache key for a request."""
        key_data = f"{url}_{str(sorted(headers.items()))}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def _should_retry(self, exception: Exception) -> bool:
        """Determine if an exception should trigger a retry."""
        if isinstance(exception, httpx.HTTPStatusError):
            status = exception.response.status_code
            # Retry on rate limit (429) and some 403 errors
            if status in (403, 429):
                return True
            # Retry on server errors
            if status >= 500:
                return True
        # Retry on network errors
        if isinstance(exception, httpx.RequestError):
            return True
        return False
    
    @retry(
        stop=stop_after_attempt(3),  # Reduced from 5 to avoid making abuse detection worse
        wait=wait_exponential(multiplier=3, min=5, max=120),  # Longer waits: 5s, 15s, 45s
        retry=lambda retry_state: retry_state.outcome.failed and 
              (retry_state.attempt_number == 1 or 
               (hasattr(retry_state.outcome.exception(), 'response') and 
                retry_state.outcome.exception().response.status_code in (403, 429, 500, 502, 503, 504))),
        before_sleep=lambda retry_state: logger.warning(
            f"Retry attempt {retry_state.attempt_number} for GitHub API after error: "
            f"{retry_state.outcome.exception()}"
        ),
    )
    async def fetch_cached(
        self, client: httpx.AsyncClient, url: str, cache_hours: Optional[int] = None
    ) -> dict:
        """Fetch from GitHub API with intelligent caching and rate limiting."""
        cache_hours = cache_hours or self.cache_hours
        cache_key = self.get_cache_key(url, self.headers)

        # Check cache first
        cached_data = self.cache.get(cache_key)
        if cached_data:
            cached_time, data = cached_data
            if datetime.now() - cached_time < timedelta(hours=cache_hours):
                # Extract meaningful part of URL for cleaner logging
                url_path = url.replace(self.github_api_base, "").lstrip("/")
                age = (datetime.now() - cached_time).total_seconds() / 3600
                logger.info(f"✓ Cache hit ({age:.1f}h old): {url_path}")
                return data

        # Apply rate limiting before making request
        async with self.rate_limiter:
            # Fetch fresh data
            url_path = url.replace(self.github_api_base, "").lstrip("/")
            logger.info(f"→ API fetch: {url_path}")
            
            try:
                response = await client.get(
                    url, 
                    headers=self.headers, 
                    timeout=10, 
                    follow_redirects=True
                )
                response.raise_for_status()
                data = response.json()

                # Cache the response
                self.cache.set(cache_key, (datetime.now(), data))
                return data
                
            except httpx.HTTPStatusError as e:
                # Check for rate limit headers
                if e.response.status_code in (403, 429):
                    retry_after = e.response.headers.get('Retry-After')
                    if retry_after:
                        wait_time = int(retry_after)
                        logger.warning(f"Rate limit hit, waiting {wait_time}s before retry")
                        await asyncio.sleep(wait_time)
                    else:
                        # Default wait for secondary rate limits (increased to 15s)
                        # This helps avoid making abuse detection worse through rapid retries
                        logger.warning(f"Rate limit (403/429) detected, waiting 15s before retry")
                        await asyncio.sleep(15)
                raise
    
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
