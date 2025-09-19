"""
Database Manager for DuckDB Extensions Analysis.

Handles database schema creation and data persistence for analysis results.
"""

from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict

import duckdb
from loguru import logger

from .base import BaseDatabaseManager, AnalysisResult, ExtensionInfo


class DatabaseManager(BaseDatabaseManager):
    """Manager for DuckDB database operations."""
    
    def __init__(self, config):
        super().__init__(config)
        self.database_path = config.database_path
        self.sql_dir = Path(config.project_root) / "sql"
        self._sql_cache: Dict[str, str] = {}
    
    def _load_sql(self, filename: str) -> str:
        """Load SQL query from file, with caching."""
        if filename in self._sql_cache:
            return self._sql_cache[filename]
        
        sql_file = self.sql_dir / filename
        if not sql_file.exists():
            raise FileNotFoundError(f"SQL file not found: {sql_file}")
        
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql = f.read().strip()
        
        self._sql_cache[filename] = sql
        return sql
    
    def create_schema(self) -> None:
        """Create the database schema for storing extension data with proper historical tracking."""
        self.config.ensure_directories()
        
        conn = duckdb.connect(str(self.database_path))
        try:
            logger.info("Creating database schema with historical tracking")

            # Execute schema creation SQL files in order
            schema_files = [
                "01_sequences.sql",
                "02_core_extensions_history.sql", 
                "03_community_extensions_history.sql",
                "04_views.sql",
                "05_duckdb_releases.sql",
                "06_analysis_runs.sql",
                "07_indexes.sql"
            ]
            
            for sql_file in schema_files:
                sql = self._load_sql(sql_file)
                # Split and execute each statement (in case file contains multiple statements)
                for statement in sql.split(';'):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

            logger.info("Database schema created successfully with historical tracking")
        
        finally:
            conn.close()
    
    def _parse_date_string(self, date_str: Optional[str]) -> Optional[datetime]:
        """Parse ISO date string to datetime object."""
        if not date_str:
            return None
        try:
            return datetime.fromisoformat(date_str.rstrip("Z"))
        except (ValueError, TypeError):
            return None
    
    async def save_analysis(self, analysis_result: AnalysisResult) -> None:
        """Save analysis results to DuckDB database."""
        logger.info(f"Saving analysis results to database: {self.database_path}")

        # Ensure schema exists
        self.create_schema()
        
        conn = duckdb.connect(str(self.database_path))
        try:
            # Insert/update DuckDB release info
            if analysis_result.duckdb_version and analysis_result.duckdb_release_date:
                days_since_release = (analysis_result.analysis_timestamp.replace(tzinfo=None) - analysis_result.duckdb_release_date.replace(tzinfo=None)).days
                sql = self._load_sql("insert_duckdb_release.sql")
                conn.execute(
                    sql,
                    [
                        analysis_result.duckdb_version, 
                        analysis_result.duckdb_release_date, 
                        days_since_release, 
                        analysis_result.analysis_timestamp
                    ],
                )

            # Insert analysis run record
            featured_count = len(analysis_result.featured_extensions)
            sql = self._load_sql("insert_analysis_run.sql")
            conn.execute(
                sql,
                [
                    analysis_result.analysis_timestamp,
                    analysis_result.duckdb_version,
                    self.config.version_full,
                    len(analysis_result.core_extensions),
                    len(analysis_result.community_extensions),
                    featured_count,
                    "Enhanced schema with historical tracking, featured extensions, and improved descriptions",
                ],
            )

            # Insert core extensions (into history table for proper versioning)
            await self._save_core_extensions(conn, analysis_result)
            
            # Insert community extensions
            await self._save_community_extensions(conn, analysis_result)

            logger.info(
                f"Successfully saved {len(analysis_result.core_extensions)} core extensions and {len(analysis_result.community_extensions)} community extensions to database"
            )

        finally:
            conn.close()
    
    async def _save_core_extensions(self, conn: duckdb.DuckDBPyConnection, analysis_result: AnalysisResult) -> None:
        """Save core extensions to database."""
        for ext in analysis_result.core_extensions:
            last_commit_date = None
            last_commit_sha = None
            last_commit_message = None
            
            # Extract GitHub info from metadata if available
            if ext.metadata and isinstance(ext.metadata, dict):
                last_commit_date = self._parse_date_string(ext.metadata.get("last_commit_date"))
                last_commit_sha = ext.metadata.get("last_commit_sha")
                last_commit_message = ext.metadata.get("last_commit_message")

            sql = self._load_sql("insert_core_extension.sql")
            conn.execute(
                sql,
                [
                    ext.name,
                    ext.stage or "Stable",
                    "✅ Ongoing",
                    analysis_result.duckdb_release_date,
                    last_commit_date,
                    last_commit_sha,
                    last_commit_message,
                    ext.repository or f"{self.config.duckdb_repo}",
                    analysis_result.duckdb_version,
                    analysis_result.analysis_timestamp,
                ],
            )
    
    async def _save_community_extensions(self, conn: duckdb.DuckDBPyConnection, analysis_result: AnalysisResult) -> None:
        """Save community extensions to database."""
        for ext in analysis_result.community_extensions:
            if ext.metadata and ext.metadata.get("status") != "❌ Error" and ext.metadata.get("repo_info"):
                # Extension with valid repository info
                repo_info = ext.metadata["repo_info"]
                
                last_push_date = self._parse_date_string(ext.last_push)
                created_at = self._parse_date_string(repo_info.get("created_at"))
                updated_at = self._parse_date_string(repo_info.get("updated_at"))

                # Extract URLs from links
                github_url = ext.links.get("github") if ext.links else None
                community_repo_url = ext.links.get("community_repo") if ext.links else None
                install_url = ext.links.get("install") if ext.links else None

                sql = self._load_sql("insert_community_extension_full.sql")
                conn.execute(
                    sql,
                    [
                        ext.name,
                        ext.repository,
                        ext.metadata["status"],
                        last_push_date,
                        ext.days_ago,
                        ext.stars,
                        repo_info.get("forks"),
                        repo_info.get("language"),
                        repo_info.get("description"),
                        ext.description,  # This is the improved description
                        repo_info.get("homepage"),
                        repo_info.get("license"),
                        repo_info.get("topics", []),
                        repo_info.get("archived", False),
                        created_at,
                        updated_at,
                        ext.featured,
                        github_url,
                        community_repo_url,
                        install_url,
                        analysis_result.duckdb_version,
                        analysis_result.analysis_timestamp,
                    ],
                )
            else:
                # Extension with errors or no repository info
                community_repo_url = ext.links.get("community_repo") if ext.links else None
                install_url = ext.links.get("install") if ext.links else None
                
                error_msg = ext.metadata.get("error") if ext.metadata else "Failed to fetch info"
                status = "❌ No Repo" if error_msg == "No repository found" else "❌ Error"

                sql = self._load_sql("insert_community_extension_error.sql")
                conn.execute(
                    sql,
                    [
                        ext.name,
                        "N/A",
                        status,
                        error_msg,
                        ext.description,
                        ext.featured,
                        community_repo_url,
                        install_url,
                        analysis_result.duckdb_version,
                        analysis_result.analysis_timestamp,
                    ],
                )
