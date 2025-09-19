#!/usr/bin/env python3
"""
⚠️  DEPRECATED: Unified DuckDB Extensions Analysis Tool (Legacy Version)

THIS SCRIPT HAS BEEN DEPRECATED and moved to deprecated/ directory.
Please use scripts/analyze_extensions.py instead, which provides:

- Improved modular architecture with better separation of concerns
- SQL queries extracted to separate .sql files for maintainability
- Enhanced error handling and logging
- Better code organization and reusability

This legacy version is kept for reference and fallback purposes only.

Original functionality:
- Community extensions analysis
- Core extensions analysis  
- Full analysis combining both
- Markdown report generation
- Intelligent caching to speed up subsequent runs
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
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
import yaml
import pandas as pd
import duckdb

# Configure logger
logger.remove()
logger.add(
    sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO"
)

# Import configuration (add parent directory to path)
sys.path.insert(0, str(Path(__file__).parent.parent))
from conf.config import config

# Set up derived values from configuration
SCRIPT_VERSION = config.version_full
GITHUB_API_BASE = config.github_api_base
COMMUNITY_REPO = config.community_repo
DUCKDB_REPO = config.duckdb_repo
CURRENT_DATE = config.current_date

# DuckDB release info will be fetched dynamically
DUCKDB_VERSION = None
DUCKDB_RELEASE_DATE = None

# Set up caching from configuration
config.ensure_directories()
cache = dc.Cache(str(config.cache_dir))

# GitHub headers from configuration
HEADERS = config.headers
has_token, token_msg = config.get_github_token_info()
if has_token:
    logger.info(token_msg)
else:
    logger.warning(token_msg)


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
async def fetch_github_api_cached(
    client: httpx.AsyncClient, url: str, cache_hours: int = 1
) -> dict:
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

    def __init__(self, cache_hours: int = 1):
        self.core_extensions: List[Dict] = []
        self.community_extensions: List[str] = []
        self.extension_data: List[Dict] = []
        self.cache_hours = cache_hours
        self.duckdb_version: Optional[str] = None
        self.duckdb_release_date: Optional[datetime] = None

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
        logger.info(
            f"Found {len(extensions)} core extensions from DuckDB documentation"
        )
        return extensions

    async def get_core_extension_github_info(
        self, client: httpx.AsyncClient, ext_name: str
    ) -> Optional[Dict]:
        """Get GitHub repository information for core extensions."""
        # Most core extensions are in the main DuckDB repo under extensions/
        try:
            # Try to get the last commit for this extension in the main DuckDB repo
            commits_url = f"{GITHUB_API_BASE}/repos/{DUCKDB_REPO}/commits?path=extensions/{ext_name}&per_page=1"
            commits = await fetch_github_api_cached(
                client, commits_url, cache_hours=self.cache_hours
            )

            if commits and len(commits) > 0:
                last_commit = commits[0]
                return {
                    "last_commit_date": last_commit["commit"]["committer"]["date"],
                    "last_commit_sha": last_commit["sha"],
                    "last_commit_message": last_commit["commit"]["message"][:100],
                }
        except Exception as e:
            logger.debug(
                f"Could not get GitHub info for core extension {ext_name}: {e}"
            )

        return None

    async def get_featured_extensions(self, client: httpx.AsyncClient) -> set[str]:
        """Get the list of featured community extensions from the official DuckDB website."""
        try:
            logger.info("Fetching featured extensions list from DuckDB website")

            # Try multiple pages where featured extensions might be listed
            featured_pages = [
                "https://duckdb.org/docs/stable/extensions/community_extensions.html",
                "https://duckdb.org/community_extensions/list_of_extensions",
                "https://duckdb.org/docs/extensions/community_extensions.html",
            ]

            featured_extensions = set()

            for url in featured_pages:
                try:
                    html = fetch_web_content_cached(url, cache_hours=self.cache_hours)
                    soup = BeautifulSoup(html, "html.parser")

                    # Look for extension names in various formats
                    # Look for code blocks, strong tags, or specific classes
                    for element in soup.find_all(["code", "strong", "b"]):
                        text = element.get_text(strip=True)
                        # Filter for extension-like names (lowercase, underscores, hyphens)
                        if (
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
                        ):
                            featured_extensions.add(text.lower())

                    # Also look for extension names in links
                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        if "extension" in href.lower() or "community" in href.lower():
                            text = link.get_text(strip=True)
                            if (
                                text
                                and len(text) > 2
                                and len(text) < 30
                                and text.replace("_", "")
                                .replace("-", "")
                                .replace(".", "")
                                .isalnum()
                                and " " not in text
                            ):
                                featured_extensions.add(text.lower())

                except Exception as e:
                    logger.debug(f"Failed to fetch from {url}: {e}")
                    continue

            # If we can't find featured extensions dynamically, use a curated list of popular ones
            if len(featured_extensions) < 5:
                logger.warning(
                    "Could not detect featured extensions dynamically, using curated list"
                )
                featured_extensions = {
                    "spatial",
                    "httpfs",
                    "parquet",
                    "json",
                    "aws",
                    "azure",
                    "postgres",
                    "mysql",
                    "sqlite",
                    "bigquery",
                    "arrow",
                    "excel",
                    "prql",
                    "substrait",
                    "h3",
                }

            # Filter to only include extensions we know about
            known_extensions = set(await self.get_community_extensions(client))
            featured_extensions = featured_extensions.intersection(
                set(name.lower() for name in known_extensions)
            )

            logger.info(f"Found {len(featured_extensions)} featured extensions")
            return featured_extensions

        except Exception as e:
            logger.error(f"Failed to fetch featured extensions: {e}")
            return set()

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

    async def get_latest_duckdb_release(
        self, client: httpx.AsyncClient
    ) -> Tuple[str, datetime]:
        """Get the latest DuckDB release version and date."""
        if self.duckdb_version and self.duckdb_release_date:
            return self.duckdb_version, self.duckdb_release_date

        logger.info("Fetching latest DuckDB release information")
        releases_url = f"{GITHUB_API_BASE}/repos/{DUCKDB_REPO}/releases/latest"

        try:
            release_data = await fetch_github_api_cached(
                client, releases_url, cache_hours=self.cache_hours
            )

            version = release_data["tag_name"]
            published_at = release_data["published_at"]

            # Parse the published date
            release_date = datetime.fromisoformat(published_at.rstrip("Z"))

            # Cache the results
            self.duckdb_version = version
            self.duckdb_release_date = release_date

            logger.info(
                f"Found latest DuckDB release: {version} (published {release_date.strftime('%Y-%m-%d')})"
            )
            return version, release_date

        except Exception as e:
            logger.error(f"Failed to fetch DuckDB release info: {e}")
            # Fallback to hardcoded values as last resort
            fallback_version = "v1.4.0"
            fallback_date = datetime(2025, 9, 16)
            logger.warning(
                f"Using fallback values: {fallback_version} ({fallback_date.strftime('%Y-%m-%d')})"
            )

            self.duckdb_version = fallback_version
            self.duckdb_release_date = fallback_date
            return fallback_version, fallback_date

    def create_database_schema(self, conn: duckdb.DuckDBPyConnection) -> None:
        """Create the database schema for storing extension data with proper historical tracking."""
        logger.info("Creating database schema with historical tracking")

        # Create sequences for auto-incrementing IDs
        conn.execute("CREATE SEQUENCE IF NOT EXISTS core_ext_hist_seq;")
        conn.execute("CREATE SEQUENCE IF NOT EXISTS community_ext_hist_seq;")
        conn.execute("CREATE SEQUENCE IF NOT EXISTS analysis_runs_seq;")

        # Create core extensions history table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS core_extensions_history (
                id INTEGER PRIMARY KEY DEFAULT nextval('core_ext_hist_seq'),
                name VARCHAR NOT NULL,
                development_stage VARCHAR,
                status VARCHAR,
                last_updated_date TIMESTAMP,
                last_commit_date TIMESTAMP,
                last_commit_sha VARCHAR,
                last_commit_message VARCHAR,
                repository VARCHAR,
                duckdb_version VARCHAR,
                analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create community extensions history table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS community_extensions_history (
                id INTEGER PRIMARY KEY DEFAULT nextval('community_ext_hist_seq'),
                name VARCHAR NOT NULL,
                repository VARCHAR,
                status VARCHAR,
                last_push_date TIMESTAMP,
                last_push_days INTEGER,
                stars INTEGER,
                forks INTEGER,
                language VARCHAR,
                description TEXT,
                improved_description TEXT,
                homepage VARCHAR,
                license VARCHAR,
                topics VARCHAR[],
                archived BOOLEAN,
                created_at TIMESTAMP,
                updated_at TIMESTAMP,
                featured BOOLEAN DEFAULT FALSE,
                github_url VARCHAR,
                community_repo_url VARCHAR,
                install_url VARCHAR,
                duckdb_version VARCHAR,
                analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create current views for latest data (for backwards compatibility)
        conn.execute("""
            CREATE OR REPLACE VIEW core_extensions AS
            SELECT DISTINCT ON (name) *
            FROM core_extensions_history
            ORDER BY name, analysis_date DESC
        """)

        conn.execute("""
            CREATE OR REPLACE VIEW community_extensions AS
            SELECT DISTINCT ON (name) *
            FROM community_extensions_history
            ORDER BY name, analysis_date DESC
        """)

        # Create DuckDB releases table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS duckdb_releases (
                version VARCHAR PRIMARY KEY,
                published_date TIMESTAMP,
                days_since_release INTEGER,
                analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create analysis runs table to track each analysis session
        conn.execute("""
            CREATE TABLE IF NOT EXISTS analysis_runs (
                id INTEGER PRIMARY KEY DEFAULT nextval('analysis_runs_seq'),
                run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                duckdb_version VARCHAR,
                script_version VARCHAR,
                total_core_extensions INTEGER,
                total_community_extensions INTEGER,
                featured_extensions_count INTEGER,
                notes TEXT
            )
        """)

        # Create indexes for better query performance
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_core_ext_hist_name_date ON core_extensions_history(name, analysis_date)"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_community_ext_hist_name_date ON community_extensions_history(name, analysis_date)"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_core_ext_hist_duckdb_version ON core_extensions_history(duckdb_version)"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_community_ext_hist_duckdb_version ON community_extensions_history(duckdb_version)"
        )

        logger.info("Database schema created successfully with historical tracking")

    async def save_to_database(
        self, extension_data: List[Dict], db_path: str = "data/extensions.duckdb"
    ) -> None:
        """Save analysis results to DuckDB database."""
        # Ensure data directory exists
        db_dir = Path(db_path).parent
        db_dir.mkdir(exist_ok=True)

        logger.info(f"Saving analysis results to database: {db_path}")

        conn = duckdb.connect(db_path)

        try:
            # Create schema
            self.create_database_schema(conn)

            # Get DuckDB release info
            async with httpx.AsyncClient() as temp_client:
                (
                    duckdb_version,
                    duckdb_release_date,
                ) = await self.get_latest_duckdb_release(temp_client)

            # Insert/update DuckDB release info
            days_since_release = (CURRENT_DATE - duckdb_release_date).days
            conn.execute(
                """
                INSERT OR REPLACE INTO duckdb_releases 
                (version, published_date, days_since_release, analysis_date)
                VALUES (?, ?, ?, ?)
            """,
                [duckdb_version, duckdb_release_date, days_since_release, CURRENT_DATE],
            )

            # Insert analysis run record
            featured_count = sum(
                1 for ext in extension_data if ext.get("featured", False)
            )
            conn.execute(
                """
                INSERT INTO analysis_runs 
                (run_timestamp, duckdb_version, script_version, total_core_extensions, 
                 total_community_extensions, featured_extensions_count, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                [
                    CURRENT_DATE,
                    duckdb_version,
                    "1.2.0",  # You might want to add a constant for this
                    len(self.get_core_extensions()),
                    len(extension_data),
                    featured_count,
                    "Enhanced schema with historical tracking, featured extensions, and improved descriptions",
                ],
            )

            # Insert core extensions (into history table for proper versioning)
            core_extensions = self.get_core_extensions()
            for ext in core_extensions:
                # Try to get GitHub info for this extension
                github_info = None
                async with httpx.AsyncClient() as temp_client:
                    github_info = await self.get_core_extension_github_info(
                        temp_client, ext["name"]
                    )

                last_commit_date = None
                last_commit_sha = None
                last_commit_message = None

                if github_info:
                    last_commit_date = datetime.fromisoformat(
                        github_info["last_commit_date"].rstrip("Z")
                    )
                    last_commit_sha = github_info["last_commit_sha"]
                    last_commit_message = github_info["last_commit_message"]

                conn.execute(
                    """
                    INSERT INTO core_extensions_history 
                    (name, development_stage, status, last_updated_date, last_commit_date, 
                     last_commit_sha, last_commit_message, repository, duckdb_version, analysis_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    [
                        ext["name"],
                        ext["stage"] or "Stable",
                        "✅ Ongoing",
                        duckdb_release_date,
                        last_commit_date,
                        last_commit_sha,
                        last_commit_message,
                        f"{DUCKDB_REPO}",
                        duckdb_version,
                        CURRENT_DATE,
                    ],
                )

            # Insert community extensions
            for ext_info in extension_data:
                name = ext_info["name"]

                if not ext_info["error"] and ext_info["repo_info"]:
                    repo_info = ext_info["repo_info"]
                    repo = ext_info["metadata"]["repo"]["github"]

                    last_push_date = None
                    if repo_info["last_push"]:
                        last_push_date = datetime.fromisoformat(
                            repo_info["last_push"].rstrip("Z")
                        )

                    created_at = None
                    if repo_info["created_at"]:
                        created_at = datetime.fromisoformat(
                            repo_info["created_at"].rstrip("Z")
                        )

                    updated_at = None
                    if repo_info["updated_at"]:
                        updated_at = datetime.fromisoformat(
                            repo_info["updated_at"].rstrip("Z")
                        )

                    # Extract URLs
                    github_url = ext_info["urls"].get("github", None)
                    community_repo_url = ext_info["urls"].get("community_repo", None)
                    install_url = ext_info["urls"].get("install", None)

                    conn.execute(
                        """
                        INSERT INTO community_extensions_history 
                        (name, repository, status, last_push_date, last_push_days, stars, forks, 
                         language, description, improved_description, homepage, license, topics, archived, 
                         created_at, updated_at, featured, github_url, community_repo_url, install_url, 
                         duckdb_version, analysis_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                        [
                            name,
                            repo,
                            ext_info["status"],
                            last_push_date,
                            ext_info["last_push_days"],
                            repo_info["stars"],
                            repo_info["forks"],
                            repo_info["language"],
                            repo_info["description"],
                            ext_info["improved_description"],
                            repo_info["homepage"],
                            repo_info["license"],
                            repo_info["topics"],
                            repo_info["archived"],
                            created_at,
                            updated_at,
                            ext_info["featured"],
                            github_url,
                            community_repo_url,
                            install_url,
                            duckdb_version,
                            CURRENT_DATE,
                        ],
                    )
                else:
                    # Insert extensions with errors
                    # Extract URLs (even for extensions with errors)
                    community_repo_url = ext_info["urls"].get("community_repo", None)
                    install_url = ext_info["urls"].get("install", None)

                    conn.execute(
                        """
                        INSERT INTO community_extensions_history 
                        (name, repository, status, description, improved_description, featured,
                         community_repo_url, install_url, duckdb_version, analysis_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                        [
                            name,
                            "N/A",
                            "❌ No Repo" if ext_info["error"] else "❌ Error",
                            ext_info["error"] or "Failed to fetch info",
                            ext_info["improved_description"],
                            ext_info["featured"],
                            community_repo_url,
                            install_url,
                            duckdb_version,
                            CURRENT_DATE,
                        ],
                    )

            logger.info(
                f"Successfully saved {len(core_extensions)} core extensions and {len(extension_data)} community extensions to database"
            )

        finally:
            conn.close()

    async def get_community_extensions(self, client: httpx.AsyncClient) -> List[str]:
        """Fetch community extensions list from GitHub."""
        if self.community_extensions:
            return self.community_extensions

        logger.info("Fetching community extensions list")
        contents_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions"
        contents = await fetch_github_api_cached(
            client, contents_url, cache_hours=self.cache_hours
        )
        extensions = [item["name"] for item in contents if item["type"] == "dir"]

        self.community_extensions = extensions
        logger.info(f"Found {len(extensions)} community extensions")
        return extensions

    async def get_extension_metadata(
        self, client: httpx.AsyncClient, ext_name: str
    ) -> Optional[Dict]:
        """Get metadata for a community extension."""
        metadata_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions/{ext_name}/description.yml"
        try:
            metadata_raw = await fetch_github_api_cached(
                client, metadata_url, cache_hours=self.cache_hours
            )
            metadata_content = base64.b64decode(metadata_raw["content"]).decode("utf-8")
            metadata = yaml.safe_load(metadata_content)
            return metadata
        except httpx.HTTPStatusError as e:
            logger.warning(f"Description not found for {ext_name}: {e}")
            return None

    async def get_repository_info(
        self, client: httpx.AsyncClient, repo: str
    ) -> Optional[Dict]:
        """Get detailed repository information from GitHub API."""
        repo_url = f"{GITHUB_API_BASE}/repos/{repo}"
        try:
            repo_data = await fetch_github_api_cached(
                client, repo_url, cache_hours=self.cache_hours
            )
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
            return (CURRENT_DATE - date).days
        except (ValueError, TypeError):
            return None

    async def analyze_community_extensions(
        self, client: httpx.AsyncClient
    ) -> Tuple[List[Dict], Dict]:
        """Analyze community extensions and return detailed data and statistics."""
        extensions = await self.get_community_extensions(client)

        # Get featured extensions list
        featured_extensions = await self.get_featured_extensions(client)
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
                "featured": ext.lower()
                in featured_extensions,  # Mark as featured if in the list
                "urls": {},  # Will store URLs for this extension
                "improved_description": None,  # Will store improved description
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
                    ext_info["improved_description"] = self.improve_description(
                        ext, None
                    )
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

    def print_community_analysis(self, extension_data: List[Dict], stats: Dict):
        """Print community extensions analysis to console."""
        logger.info("=== Community Extensions Analysis ===")

        for ext_info in extension_data:
            name = ext_info["name"]
            status = ext_info["status"]

            if ext_info["repo_info"]:
                repo = ext_info["metadata"]["repo"]["github"]
                last_push_days = ext_info["last_push_days"]
                last_push_str = (
                    f"{last_push_days} days ago"
                    if last_push_days is not None
                    else "Unknown"
                )
                logger.info(
                    f"{name} (Repo: {repo}): {status.replace('✅ ', '').replace('🔴 ', '').replace('❌ ', '')} | Last push: {last_push_str}"
                )
            else:
                logger.info(f"{name}: {ext_info['error']}")

        logger.info("\n=== Community Extensions Summary ===")
        logger.info(f"Total: {stats['total']}")
        logger.info(
            f"Active: {stats['active']} ({stats['active'] / stats['total'] * 100:.1f}%)"
        )
        logger.info(
            f"Discontinued: {stats['discontinued']} ({stats['discontinued'] / stats['total'] * 100:.1f}%)"
        )
        logger.info(
            f"Errors: {stats['errors']} ({stats['errors'] / stats['total'] * 100:.1f}%)"
        )

    async def print_core_analysis(self, client: httpx.AsyncClient):
        """Print core extensions analysis to console."""
        logger.info("=== Core Extensions Analysis ===")

        extensions = self.get_core_extensions()

        # Get DuckDB release info
        duckdb_version, duckdb_release_date = await self.get_latest_duckdb_release(
            client
        )

        for ext in extensions:
            stage = ext["stage"] if ext["stage"] else "Stable"

            # Try to get actual GitHub activity
            github_info = await self.get_core_extension_github_info(client, ext["name"])

            if github_info:
                last_commit_days = self.calculate_days_ago(
                    github_info["last_commit_date"]
                )
                logger.info(
                    f"{ext['name']} (Core, Stage: {stage}): Ongoing | Last commit: {last_commit_days} days ago"
                )
            else:
                # Fallback to DuckDB release info
                duckdb_lag_days = (CURRENT_DATE - duckdb_release_date).days
                logger.info(
                    f"{ext['name']} (Core, Stage: {stage}): Ongoing | Last updated: {duckdb_lag_days} days ago (in {duckdb_version})"
                )

        logger.info("\n=== Core Extensions Summary ===")
        logger.info(f"Total: {len(extensions)}")
        logger.info("All core extensions are ongoing and updated with DuckDB releases")

    async def generate_markdown_report(
        self, client: httpx.AsyncClient, extension_data: List[Dict], stats: Dict
    ) -> str:
        """Generate comprehensive markdown report."""
        logger.info("Generating markdown report")

        # Report header
        report = [
            "# DuckDB Extensions Status Report",
            "",
            f"Generated on: **{CURRENT_DATE.strftime('%Y-%m-%d %H:%M:%S UTC')}**",
            "",
            "This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.",
            "",
        ]

        # Core extensions section
        core_extensions = self.get_core_extensions()

        # Get DuckDB release info
        duckdb_version, duckdb_release_date = await self.get_latest_duckdb_release(
            client
        )
        duckdb_lag_days = (CURRENT_DATE - duckdb_release_date).days

        report.extend(
            [
                "## Core Extensions\n",
                f"DuckDB core extensions from version **{duckdb_version}** (released {duckdb_lag_days} days ago).\n",
                "| Extension | Development Stage | Status | Last Updated |",
                "|-----------|-------------------|--------|--------------|",
            ]
        )

        for ext in core_extensions:
            stage = ext["stage"] if ext["stage"] else "Stable"
            status = "✅ Ongoing"
            last_updated = f"{duckdb_lag_days} days ago (in {duckdb_version})"
            report.append(
                f"| **{ext['name']}** | {stage} | {status} | {last_updated} |"
            )

        report.extend(
            [
                f"\n**Total Core Extensions**: {len(core_extensions)}\n",
                "",
            ]
        )

        # Community extensions section
        report.extend(
            [
                "## Community Extensions\n",
                "| Extension | Repository | Status | Last Push | Stars | Language | Description |",
                "|-----------|------------|--------|-----------|-------|----------|-------------|",
            ]
        )

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
                last_push = (
                    f"{last_push_days} days ago"
                    if last_push_days is not None
                    else "Unknown"
                )
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

            report.append(
                f"| **{name}** | {repo_link} | {status} | {last_push} | {stars} | {language} | {description} |"
            )

        # Community extensions summary
        report.extend(
            [
                "\n### Community Extensions Summary",
                f"- **Total Extensions**: {stats['total']}",
                f"- **Active Extensions**: {stats['active']} ({stats['active'] / stats['total'] * 100:.1f}%)",
                f"- **Discontinued Extensions**: {stats['discontinued']} ({stats['discontinued'] / stats['total'] * 100:.1f}%)",
                f"- **Extensions with Issues**: {stats['errors']} ({stats['errors'] / stats['total'] * 100:.1f}%)",
                "",
            ]
        )

        # Add methodology section
        report.extend(
            [
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
            ]
        )

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

    async def save_csv_report(
        self, client: httpx.AsyncClient, extension_data: List[Dict], stats: Dict
    ) -> Path:
        """Save the analysis results to CSV format."""
        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)

        timestamp = CURRENT_DATE.strftime("%Y%m%d_%H%M%S")
        csv_file = report_dir / f"duckdb_extensions_report_{timestamp}.csv"

        # Prepare data for CSV
        rows = []

        # Get DuckDB release info
        duckdb_version, duckdb_release_date = await self.get_latest_duckdb_release(
            client
        )

        # Add core extensions
        core_extensions = self.get_core_extensions()
        for ext in core_extensions:
            rows.append(
                {
                    "Extension": ext["name"],
                    "Type": "Core",
                    "Repository": "duckdb/duckdb",
                    "Status": "✅ Ongoing",
                    "Development Stage": ext["stage"] or "Stable",
                    "Last Push Days": (CURRENT_DATE - duckdb_release_date).days,
                    "Stars": "N/A",
                    "Language": "C++",
                    "Description": "Core DuckDB extension",
                    "Homepage": "https://duckdb.org",
                    "License": "MIT",
                    "Topics": "",
                }
            )

        # Add community extensions
        for ext_info in extension_data:
            name = ext_info["name"]

            if ext_info["error"]:
                rows.append(
                    {
                        "Extension": name,
                        "Type": "Community",
                        "Repository": "N/A",
                        "Status": "❌ No Repo",
                        "Development Stage": "N/A",
                        "Last Push Days": "N/A",
                        "Stars": "N/A",
                        "Language": "N/A",
                        "Description": ext_info["error"],
                        "Homepage": "N/A",
                        "License": "N/A",
                        "Topics": "N/A",
                    }
                )
            elif ext_info["repo_info"]:
                repo_info = ext_info["repo_info"]
                repo = ext_info["metadata"]["repo"]["github"]

                rows.append(
                    {
                        "Extension": name,
                        "Type": "Community",
                        "Repository": repo,
                        "Status": ext_info["status"],
                        "Development Stage": "Community",
                        "Last Push Days": ext_info["last_push_days"] or "Unknown",
                        "Stars": repo_info["stars"],
                        "Language": repo_info["language"] or "N/A",
                        "Description": repo_info["description"] or "No description",
                        "Homepage": repo_info["homepage"] or "N/A",
                        "License": repo_info["license"] or "N/A",
                        "Topics": ",".join(repo_info["topics"])
                        if repo_info["topics"]
                        else "",
                    }
                )

        # Create DataFrame and save to CSV
        df = pd.DataFrame(rows)
        df.to_csv(csv_file, index=False, encoding="utf-8")
        logger.info(f"CSV report saved: {csv_file}")

        return csv_file

    async def save_excel_report(
        self, client: httpx.AsyncClient, extension_data: List[Dict], stats: Dict
    ) -> Path:
        """Save the analysis results to Excel format with multiple sheets."""
        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)

        timestamp = CURRENT_DATE.strftime("%Y%m%d_%H%M%S")
        excel_file = report_dir / f"duckdb_extensions_report_{timestamp}.xlsx"

        # Prepare data for Excel
        core_rows = []
        community_rows = []

        # Get DuckDB release info
        duckdb_version, duckdb_release_date = await self.get_latest_duckdb_release(
            client
        )

        # Core extensions data
        core_extensions = self.get_core_extensions()
        for ext in core_extensions:
            core_rows.append(
                {
                    "Extension": ext["name"],
                    "Development Stage": ext["stage"] or "Stable",
                    "Status": "✅ Ongoing",
                    "Last Updated": f"{(CURRENT_DATE - duckdb_release_date).days} days ago",
                    "Repository": "duckdb/duckdb",
                    "Language": "C++",
                    "Description": "Core DuckDB extension",
                }
            )

        # Community extensions data
        for ext_info in extension_data:
            name = ext_info["name"]

            if ext_info["error"]:
                community_rows.append(
                    {
                        "Extension": name,
                        "Repository": "N/A",
                        "Status": "❌ No Repo",
                        "Last Push": "N/A",
                        "Stars": "N/A",
                        "Language": "N/A",
                        "Description": ext_info["error"],
                        "Homepage": "N/A",
                        "License": "N/A",
                        "Topics": "N/A",
                    }
                )
            elif ext_info["repo_info"]:
                repo_info = ext_info["repo_info"]
                repo = ext_info["metadata"]["repo"]["github"]

                community_rows.append(
                    {
                        "Extension": name,
                        "Repository": repo,
                        "Status": ext_info["status"],
                        "Last Push": f"{ext_info['last_push_days']} days ago"
                        if ext_info["last_push_days"] is not None
                        else "Unknown",
                        "Stars": repo_info["stars"],
                        "Language": repo_info["language"] or "N/A",
                        "Description": repo_info["description"] or "No description",
                        "Homepage": repo_info["homepage"] or "N/A",
                        "License": repo_info["license"] or "N/A",
                        "Topics": ",".join(repo_info["topics"])
                        if repo_info["topics"]
                        else "",
                    }
                )

        # Create Excel writer and save sheets
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            # Core Extensions sheet
            core_df = pd.DataFrame(core_rows)
            core_df.to_excel(writer, sheet_name="Core Extensions", index=False)

            # Community Extensions sheet
            community_df = pd.DataFrame(community_rows)
            community_df.to_excel(
                writer, sheet_name="Community Extensions", index=False
            )

            # Summary sheet
            summary_data = [
                ["Metric", "Core Extensions", "Community Extensions", "Total"],
                [
                    "Total Count",
                    len(core_extensions),
                    stats["total"],
                    len(core_extensions) + stats["total"],
                ],
                [
                    "Active Count",
                    len(core_extensions),
                    stats["active"],
                    len(core_extensions) + stats["active"],
                ],
                ["Discontinued Count", 0, stats["discontinued"], stats["discontinued"]],
                ["Error Count", 0, stats["errors"], stats["errors"]],
            ]
            summary_df = pd.DataFrame(summary_data[1:], columns=summary_data[0])
            summary_df.to_excel(writer, sheet_name="Summary", index=False)

        logger.info(f"Excel report saved: {excel_file}")
        return excel_file


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
    %(prog)s report --csv       # Generate report in CSV format
    %(prog)s report --excel     # Generate report in Excel format
    %(prog)s database           # Save analysis to DuckDB database
    %(prog)s --clear-cache      # Clear cache and run full analysis
    %(prog)s --no-cache         # Bypass cache for this run
        """,
    )

    parser.add_argument(
        "mode",
        choices=["community", "core", "full", "report", "database"],
        help="Analysis mode to run",
    )

    parser.add_argument(
        "--clear-cache", action="store_true", help="Clear cache before running analysis"
    )

    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Bypass cache for this run (fetch fresh data)",
    )

    parser.add_argument(
        "--csv", action="store_true", help="Generate CSV output (only for report mode)"
    )

    parser.add_argument(
        "--excel",
        action="store_true",
        help="Generate Excel output (only for report mode)",
    )

    parser.add_argument(
        "--cache-info", action="store_true", help="Show cache statistics"
    )

    args = parser.parse_args()

    # Handle cache operations
    if args.clear_cache:
        logger.info("Clearing cache...")
        cache.clear()
        logger.info("Cache cleared")

    # Set up cache behavior based on options
    cache_hours = (
        0 if args.no_cache else 1
    )  # Use 0 hours (no caching) if --no-cache is specified
    if args.no_cache:
        logger.info("Bypassing cache for this run (fetching fresh data)")

    if args.cache_info:
        logger.info(f"Cache directory: {CACHE_DIR}")
        logger.info(f"Cache size: {len(cache)} entries")
        logger.info(
            f"Cache disk usage: {sum(f.stat().st_size for f in CACHE_DIR.rglob('*') if f.is_file()) / 1024 / 1024:.2f} MB"
        )

    # Initialize analyzer
    analyzer = ExtensionAnalyzer(cache_hours=cache_hours)

    # Run analysis based on mode
    if args.mode == "core":
        logger.info("Starting core extensions analysis")
        async with httpx.AsyncClient() as client:
            await analyzer.print_core_analysis(client)

    elif args.mode == "community":
        logger.info("Starting community extensions analysis")
        async with httpx.AsyncClient() as client:
            extension_data, stats = await analyzer.analyze_community_extensions(client)
            analyzer.print_community_analysis(extension_data, stats)

    elif args.mode == "full":
        logger.info("Starting full extensions analysis")
        async with httpx.AsyncClient() as client:
            await analyzer.print_core_analysis(client)
            extension_data, stats = await analyzer.analyze_community_extensions(client)
            analyzer.print_community_analysis(extension_data, stats)

    elif args.mode == "report":
        logger.info("Generating comprehensive markdown report")
        async with httpx.AsyncClient() as client:
            extension_data, stats = await analyzer.analyze_community_extensions(client)

            # Generate markdown report (default)
            report_content = await analyzer.generate_markdown_report(
                client, extension_data, stats
            )
            report_file, latest_file = analyzer.save_report(report_content)
            logger.info(f"Report generated successfully: {report_file}")
            logger.info(f"Latest report updated: {latest_file}")

            # Generate CSV report if requested
            if args.csv:
                csv_file = await analyzer.save_csv_report(client, extension_data, stats)
                logger.info(f"CSV report saved: {csv_file}")

            # Generate Excel report if requested
            if args.excel:
                excel_file = await analyzer.save_excel_report(
                    client, extension_data, stats
                )
                logger.info(f"Excel report saved: {excel_file}")

    elif args.mode == "database":
        logger.info("Saving analysis to DuckDB database")
        async with httpx.AsyncClient() as client:
            extension_data, stats = await analyzer.analyze_community_extensions(client)
            await analyzer.save_to_database(extension_data)
            logger.info("Analysis saved to database: data/extensions.duckdb")


if __name__ == "__main__":
    logger.info("Starting DuckDB extensions analysis")
    asyncio.run(main())
    logger.info("Analysis complete")
