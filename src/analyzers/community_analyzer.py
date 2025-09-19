"""
Community Extensions Analyzer for DuckDB Extensions Analysis.

Handles analysis of DuckDB community extensions from the community repository.
"""

import base64
import yaml
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import httpx
from loguru import logger

from .base import BaseAnalyzer, ExtensionInfo
from .github_api import GitHubAPIClient


class CommunityExtensionAnalyzer(BaseAnalyzer):
    """Analyzer for DuckDB community extensions."""
    
    def __init__(self, config, github_client: GitHubAPIClient, cache_hours: int = 1):
        super().__init__(config, cache_hours)
        self.github_client = github_client
        self.community_extensions: List[str] = []
        self.extension_data: List[Dict] = []
    
    async def get_community_extensions_list(self, client: httpx.AsyncClient) -> List[str]:
        """Fetch community extensions list from GitHub."""
        if self.community_extensions:
            return self.community_extensions

        logger.info("Fetching community extensions list")
        
        # Use the improved method from github_client
        extensions = await self.github_client.get_community_extensions_list(client)
        
        self.community_extensions = extensions
        logger.info(f"Found {len(extensions)} community extensions")
        return extensions
    
    async def get_extension_metadata(
        self, client: httpx.AsyncClient, ext_name: str
    ) -> Optional[Dict]:
        """Get metadata for a community extension."""
        metadata_url = f"{self.github_client.github_api_base}/repos/{self.github_client.community_repo}/contents/extensions/{ext_name}/description.yml"
        try:
            metadata_raw = await self.github_client.fetch_cached(client, metadata_url)
            metadata_content = base64.b64decode(metadata_raw["content"]).decode("utf-8")
            metadata = yaml.safe_load(metadata_content)
            return metadata
        except Exception as e:
            logger.debug(f"Description not found for {ext_name}: {e}")
            return None
    
    async def get_repository_info(
        self, client: httpx.AsyncClient, repo: str
    ) -> Optional[Dict]:
        """Get detailed repository information from GitHub API."""
        try:
            repo_data = await self.github_client.get_repository_info(client, repo)
            if not repo_data:
                return None
                
            return {
                "archived": repo_data.get("archived", False),
                "last_push": repo_data.get("pushed_at"),
                "stars": repo_data.get("stargazers_count", 0),
                "forks": repo_data.get("forks_count", 0),
                "language": repo_data.get("language"),
                "description": repo_data.get("description"),
                "license": repo_data.get("license", {}).get("spdx_id")
                if repo_data.get("license")
                else None,
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
            return (self.config.current_date - date).days
        except (ValueError, TypeError):
            return None
    
    def get_extension_links(self, ext_name: str, repo: str = None) -> Dict[str, str]:
        """Generate links for an extension."""
        links = {}

        # Community extension repository page
        links["community_repo"] = (
            f"https://github.com/duckdb/community-extensions/tree/main/extensions/{ext_name}"
        )

        # If we have repository info, add GitHub link
        if repo:
            links["github"] = f"https://github.com/{repo}"
            links["issues"] = f"https://github.com/{repo}/issues"
            links["releases"] = f"https://github.com/{repo}/releases"

        # DuckDB installation link
        links["install"] = (
            f"https://duckdb.org/docs/extensions/community_extensions.html#{ext_name}"
        )

        return links
    
    def improve_description(
        self,
        ext_name: str,
        description: str,
        repo: str = None,
        topics: List[str] = None,
    ) -> str:
        """Improve extension description using available metadata."""
        if (
            description
            and description.strip()
            and description.lower() != "no description"
        ):
            return description

        # Generate description from name and available metadata
        improved_desc = []

        # Use extension name to infer functionality
        name_lower = ext_name.lower()
        if "sql" in name_lower:
            improved_desc.append("SQL-related extension")
        elif "db" in name_lower or "database" in name_lower:
            improved_desc.append("Database connectivity extension")
        elif "http" in name_lower or "web" in name_lower:
            improved_desc.append("Web/HTTP functionality extension")
        elif "json" in name_lower or "xml" in name_lower or "yaml" in name_lower:
            improved_desc.append("Data format handling extension")
        elif "geo" in name_lower or "spatial" in name_lower:
            improved_desc.append("Geospatial data extension")
        elif "aws" in name_lower or "azure" in name_lower or "gcp" in name_lower:
            improved_desc.append("Cloud platform integration extension")
        elif "crypto" in name_lower or "hash" in name_lower:
            improved_desc.append("Cryptographic functions extension")
        else:
            improved_desc.append(f"DuckDB extension: {ext_name}")

        # Add info from topics if available
        if topics:
            topic_hints = []
            for topic in topics[:3]:  # Use first 3 topics
                if topic.lower() not in ["duckdb", "extension", "database"]:
                    topic_hints.append(topic)
            if topic_hints:
                improved_desc.append(f"({', '.join(topic_hints)})")

        # Add repository info if available
        if repo and "/" in repo:
            org = repo.split("/")[0]
            if org not in ["duckdb", "query-farm"]:  # Don't mention obvious orgs
                improved_desc.append(f"by {org}")

        return " ".join(improved_desc)
    
    async def analyze_community_extensions(
        self, client: httpx.AsyncClient, featured_extensions: set[str]
    ) -> Tuple[List[Dict], Dict]:
        """Analyze community extensions and return detailed data and statistics."""
        extensions = await self.get_community_extensions_list(client)
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
                "featured": ext.lower() in featured_extensions,
                "urls": {},
                "improved_description": None,
            }

            # Generate URLs for the extension
            ext_info["urls"] = self.get_extension_links(ext)

            if metadata and "repo" in metadata and "github" in metadata["repo"]:
                repo = metadata["repo"]["github"]
                repo_info = await self.get_repository_info(client, repo)
                if repo_info:
                    ext_info["repo_info"] = repo_info
                    ext_info["last_push_days"] = self.calculate_days_ago(
                        repo_info["last_push"]
                    )

                    # Update URLs with repo information
                    ext_info["urls"] = self.get_extension_links(ext, repo)

                    # Generate improved description if needed
                    ext_info["improved_description"] = self.improve_description(
                        ext,
                        repo_info.get("description"),
                        repo,
                        repo_info.get("topics", []),
                    )

                    if repo_info["archived"]:
                        ext_info["status"] = "🔴 Discontinued"
                    else:
                        ext_info["status"] = "✅ Ongoing"
                else:
                    ext_info["error"] = "Failed to fetch repository info"
                    ext_info["improved_description"] = self.improve_description(ext, None)
            else:
                ext_info["error"] = "No repository found"
                ext_info["improved_description"] = self.improve_description(ext, None)

            extension_data.append(ext_info)

        # Sort by last activity (most recent first)
        extension_data.sort(
            key=lambda x: x["last_push_days"]
            if x["last_push_days"] is not None
            else 999999
        )

        # Calculate statistics
        stats = {
            "total": len(extension_data),
            "active": sum(1 for ext in extension_data if ext["status"] == "✅ Ongoing"),
            "discontinued": sum(
                1 for ext in extension_data if ext["status"] == "🔴 Discontinued"
            ),
            "errors": sum(1 for ext in extension_data if ext["status"] == "❌ Error"),
        }

        self.extension_data = extension_data
        return extension_data, stats
    
    async def analyze(self, featured_extensions: set[str] = None) -> List[ExtensionInfo]:
        """Analyze community extensions and return ExtensionInfo objects."""
        async with httpx.AsyncClient() as client:
            if featured_extensions is None:
                featured_extensions = set()
            
            extension_data, stats = await self.analyze_community_extensions(client, featured_extensions)
            extension_infos = []
            
            for ext_data in extension_data:
                # Create ExtensionInfo object
                ext_info = ExtensionInfo(
                    name=ext_data["name"],
                    type="community",
                    featured=ext_data["featured"],
                    links=ext_data["urls"],
                    description=ext_data.get("improved_description")
                )
                
                # Add repository information if available
                repo_info = ext_data.get("repo_info")
                if repo_info:
                    ext_info.repository = repo_info.get("full_name")
                    ext_info.stars = repo_info.get("stars")
                    ext_info.last_push = repo_info.get("last_push")
                    ext_info.days_ago = ext_data.get("last_push_days")
                
                # Add metadata
                ext_info.metadata = {
                    "status": ext_data["status"],
                    "error": ext_data.get("error"),
                    "repo_info": repo_info,
                    "metadata": ext_data.get("metadata")
                }
                
                extension_infos.append(ext_info)
            
            return extension_infos