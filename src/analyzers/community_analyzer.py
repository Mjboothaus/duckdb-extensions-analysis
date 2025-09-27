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
from tqdm import tqdm

from .base import BaseAnalyzer, ExtensionInfo
from .github_api import GitHubAPIClient

# Import deprecation detection functionality
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../scripts'))
from detect_deprecated_extensions import DeprecationDetector, RepositoryCache


class CommunityExtensionAnalyzer(BaseAnalyzer):
    """Analyzer for DuckDB community extensions."""
    
    def __init__(self, config, github_client: GitHubAPIClient, cache_hours: int = 1):
        super().__init__(config, cache_hours)
        self.github_client = github_client
        self.community_extensions: List[str] = []
        self.extension_data: List[Dict] = []
        
        # Initialize deprecation detector with caching
        cache_dir = config.cache_dir / 'deprecation_detector' if hasattr(config, 'cache_dir') else None
        deprecation_cache = RepositoryCache(cache_dir=cache_dir, cache_days=cache_hours * 24, enabled=True)
        self.deprecation_detector = DeprecationDetector(
            github_token=config.github_token if hasattr(config, 'github_token') else None,
            cache=deprecation_cache
        )
    
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

        # DuckDB documentation link
        links["install"] = (
            f"https://duckdb.org/community_extensions/extensions/{ext_name}.html"
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
    
    async def analyze_extension_deprecation(
        self, client: httpx.AsyncClient, ext_name: str, repo_url: str, ce_metadata: Optional[Dict] = None
    ) -> Optional[Dict]:
        """Analyze an extension for deprecation indicators using the deprecation detector."""
        try:
            # Run deprecation analysis
            deprecation_result = await self.deprecation_detector.analyze_extension(
                client, ext_name, repo_url, ce_metadata
            )
            
            if deprecation_result.get('status') == 'analyzed':
                return {
                    'deprecation_score': deprecation_result.get('deprecation_score', 0.0),
                    'recommendation': deprecation_result.get('recommendation', 'ACTIVE'),
                    'deprecation_indicators': deprecation_result.get('deprecation_indicators', []),
                    'warning_indicators': deprecation_result.get('warning_indicators', []),
                    'active_indicators': deprecation_result.get('active_indicators', []),
                    'repository_archived': deprecation_result.get('repository_archived', False),
                    'analysis_timestamp': deprecation_result.get('analysis_timestamp')
                }
            else:
                logger.debug(f"Deprecation analysis failed for {ext_name}: {deprecation_result.get('error', 'Unknown error')}")
                return None
                
        except Exception as e:
            logger.debug(f"Error during deprecation analysis for {ext_name}: {e}")
            return None
    
    async def analyze_community_extensions(
        self, client: httpx.AsyncClient
    ) -> Tuple[List[Dict], Dict]:
        """Analyze community extensions and return detailed data and statistics."""
        extensions = await self.get_community_extensions_list(client)
        extension_data = []
        
        # Use tqdm progress bar only when processing many extensions
        logger.info(f"Processing {len(extensions)} community extensions...")
        
        # Only show progress bar if processing more than 10 extensions 
        # (avoids clutter when most data is cached)
        show_progress = len(extensions) > 10
        
        if show_progress:
            pbar = tqdm(extensions, desc="Analyzing community extensions", unit="ext")
            iterator = pbar
        else:
            iterator = extensions
            pbar = None
            
        for ext in iterator:
            if pbar:
                pbar.set_description(f"Processing {ext}")
                metadata = await self.get_extension_metadata(client, ext)

                ext_info = {
                    "name": ext,
                    "metadata": metadata,
                    "repo_info": None,
                    "error": None,
                    "status": "❌ Error",
                    "last_push_days": None,
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

                        # Check extension status using metadata configuration
                        from .extension_metadata import ExtensionMetadata
                        metadata_helper = ExtensionMetadata(self.config.config_dir)
                        
                        # Add CE metadata to extension info
                        if metadata:
                            ext_info["ce_metadata"] = {
                                "official_description": metadata.get("extension", {}).get("description"),
                                "version": metadata.get("extension", {}).get("version"),
                                "language": metadata.get("extension", {}).get("language"),
                                "maintainers": metadata.get("extension", {}).get("maintainers", []),
                                "license": metadata.get("extension", {}).get("license"),
                                "build_system": metadata.get("extension", {}).get("build"),
                                "description_yml_url": f"https://github.com/duckdb/community-extensions/blob/main/extensions/{ext}/description.yml"
                            }
                        
                        # Perform automated deprecation analysis
                        repo_url = f"https://github.com/{repo}"
                        deprecation_analysis = await self.analyze_extension_deprecation(
                            client, ext, repo_url, metadata
                        )
                        if deprecation_analysis:
                            ext_info["deprecation_analysis"] = deprecation_analysis
                        
                        # Determine status based on configuration, repo state, and deprecation analysis
                        if metadata_helper.is_deprecated_extension(ext):
                            ext_info["status"] = "⚠️ Deprecated"
                            ext_info["deprecated_info"] = metadata_helper.get_deprecated_extension_info(ext)
                        elif metadata_helper.is_review_required_extension(ext):
                            ext_info["status"] = "⚠️ Review Required"
                            ext_info["review_info"] = metadata_helper.get_review_required_extension_info(ext)
                        elif metadata_helper.is_template_extension(ext):
                            ext_info["status"] = "🔧 Template"
                            ext_info["template_info"] = metadata_helper.get_template_extension_info(ext)
                        elif repo_info["archived"]:
                            ext_info["status"] = "🔴 Discontinued"
                        elif deprecation_analysis and deprecation_analysis.get('deprecation_score', 0) >= 5.0:
                            # High deprecation score from automated analysis
                            ext_info["status"] = "⚠️ Likely Deprecated"
                            ext_info["auto_deprecation_detected"] = True
                        elif deprecation_analysis and deprecation_analysis.get('deprecation_score', 0) >= 3.0:
                            # Medium deprecation score from automated analysis
                            ext_info["status"] = "⚠️ Review Recommended"
                            ext_info["auto_review_recommended"] = True
                        else:
                            ext_info["status"] = "✅ Ongoing"
                    else:
                        ext_info["error"] = "Failed to fetch repository info"
                        ext_info["improved_description"] = self.improve_description(ext, None)
                else:
                    ext_info["error"] = "No repository found"
                    ext_info["improved_description"] = self.improve_description(ext, None)

                extension_data.append(ext_info)
        
        # Close progress bar if it was used
        if pbar:
            pbar.close()

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
            "deprecated": sum(1 for ext in extension_data if ext["status"] == "⚠️ Deprecated"),
            "review_required": sum(1 for ext in extension_data if ext["status"] == "⚠️ Review Required"),
            "likely_deprecated": sum(1 for ext in extension_data if ext["status"] == "⚠️ Likely Deprecated"),
            "review_recommended": sum(1 for ext in extension_data if ext["status"] == "⚠️ Review Recommended"),
            "templates": sum(1 for ext in extension_data if ext["status"] == "🔧 Template"),
            "discontinued": sum(
                1 for ext in extension_data if ext["status"] == "🔴 Discontinued"
            ),
            "errors": sum(1 for ext in extension_data if ext["status"] == "❌ Error"),
            "auto_deprecation_detected": sum(1 for ext in extension_data if ext.get("auto_deprecation_detected", False)),
            "auto_review_recommended": sum(1 for ext in extension_data if ext.get("auto_review_recommended", False)),
        }

        self.extension_data = extension_data
        return extension_data, stats
    
    async def analyze(self) -> List[ExtensionInfo]:
        """Analyze community extensions and return ExtensionInfo objects."""
        async with httpx.AsyncClient() as client:
            extension_data, stats = await self.analyze_community_extensions(client)
            extension_infos = []
            
            for ext_data in extension_data:
                # Create ExtensionInfo object
                ext_info = ExtensionInfo(
                    name=ext_data["name"],
                    type="community",
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
                
                # Add metadata including CE metadata and deprecation analysis
                ext_info.metadata = {
                    "status": ext_data["status"],
                    "error": ext_data.get("error"),
                    "repo_info": repo_info,
                    "metadata": ext_data.get("metadata"),
                    "ce_metadata": ext_data.get("ce_metadata"),
                    "deprecation_analysis": ext_data.get("deprecation_analysis"),
                    "deprecated_info": ext_data.get("deprecated_info"),
                    "review_info": ext_data.get("review_info"),
                    "template_info": ext_data.get("template_info"),
                    "auto_deprecation_detected": ext_data.get("auto_deprecation_detected", False),
                    "auto_review_recommended": ext_data.get("auto_review_recommended", False)
                }
                
                extension_infos.append(ext_info)
            
            return extension_infos