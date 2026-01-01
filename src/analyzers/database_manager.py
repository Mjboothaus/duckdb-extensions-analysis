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
                "07_indexes.sql",
                "08_extension_availability_history.sql",
                "09_availability_views.sql",
                "10_github_issues_history.sql",
                "11_github_issues_views.sql",
                "12_installation_test_history.sql",
                "13_installation_test_views.sql",
                "14_extension_trends_summary.sql",
                "15_extension_metrics_daily.sql",
                "16_trends_views.sql",
                "17_duckdb_releases_enhancement.sql"
            ]
            
            for sql_file in schema_files:
                try:
                    sql = self._load_sql(sql_file)
                    # Execute the complete SQL file content
                    if sql.strip():
                        conn.execute(sql)
                    logger.debug(f"Successfully executed {sql_file}")
                except Exception as e:
                    logger.error(f"Failed to execute {sql_file}: {e}")
                    raise

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
            sql = self._load_sql("insert_analysis_run.sql")
            conn.execute(
                sql,
                [
                    analysis_result.analysis_timestamp,
                    analysis_result.duckdb_version,
                    self.config.version_full,
                    len(analysis_result.core_extensions),
                    len(analysis_result.community_extensions),
                    0,  # featured_count (deprecated)
                    "Enhanced schema with CE metadata integration and deprecation analysis",
                ],
            )

            # Insert core extensions (into history table for proper versioning)
            await self._save_core_extensions(conn, analysis_result)
            
            # Insert community extensions
            await self._save_community_extensions(conn, analysis_result)
            
            # Insert extension availability history
            await self._save_extension_availability(conn, analysis_result)
            
            # Insert GitHub issues if available
            if hasattr(analysis_result, 'github_issues') and analysis_result.github_issues:
                await self._save_github_issues(conn, analysis_result)
            
            # Insert installation test results if available
            if hasattr(analysis_result, 'installation_results') and analysis_result.installation_results:
                await self._save_installation_results(conn, analysis_result)

            logger.info(
                f"Successfully saved {len(analysis_result.core_extensions)} core extensions and {len(analysis_result.community_extensions)} community extensions to database"
            )

        finally:
            conn.close()
    
    async def _save_core_extensions(self, conn: duckdb.DuckDBPyConnection, analysis_result: AnalysisResult) -> None:
        """Save core extensions to database."""
        import json
        
        for ext in analysis_result.core_extensions:
            last_commit_date = None
            last_commit_sha = None
            last_commit_message = None
            
            # Extract GitHub info from metadata if available
            if ext.metadata and isinstance(ext.metadata, dict):
                last_commit_date = self._parse_date_string(ext.metadata.get("last_commit_date"))
                last_commit_sha = ext.metadata.get("last_commit_sha")
                last_commit_message = ext.metadata.get("last_commit_message")
            
            # Prepare platform availability data
            platform_availability_json = None
            earliest_availability_date = None
            available_platforms = []
            
            if ext.platform_availability:
                # Convert datetime objects to ISO strings for JSON serialization
                serializable_platform_data = {}
                for platform, info in ext.platform_availability.items():
                    serializable_info = dict(info)
                    if 'date' in serializable_info and isinstance(serializable_info['date'], datetime):
                        serializable_info['date'] = serializable_info['date'].isoformat()
                    serializable_platform_data[platform] = serializable_info
                
                platform_availability_json = json.dumps(serializable_platform_data)
                available_dates = []
                
                for platform, info in ext.platform_availability.items():
                    if info.get('available'):
                        available_platforms.append(platform)
                        if info.get('date'):
                            date_obj = info['date'] if isinstance(info['date'], datetime) else self._parse_date_string(info['date'])
                            if date_obj:
                                available_dates.append(date_obj)
                
                if available_dates:
                    earliest_availability_date = min(available_dates)

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
                    platform_availability_json,
                    earliest_availability_date,
                    available_platforms,
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
                        False,  # featured (deprecated)
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
                        False,  # featured (deprecated)
                        community_repo_url,
                        install_url,
                        analysis_result.duckdb_version,
                        analysis_result.analysis_timestamp,
                    ],
                )
    
    async def _save_extension_availability(self, conn: duckdb.DuckDBPyConnection, analysis_result: AnalysisResult) -> None:
        """Save extension platform availability data to database."""
        availability_sql = self._load_sql("insert_extension_availability.sql")
        
        # Calculate days since release for this analysis
        days_since_release = None
        if analysis_result.duckdb_release_date:
            days_since_release = (analysis_result.analysis_timestamp.replace(tzinfo=None) - analysis_result.duckdb_release_date.replace(tzinfo=None)).days
        
        # Save core extension availability data
        for ext in analysis_result.core_extensions:
            if ext.platform_availability:
                for platform, availability_info in ext.platform_availability.items():
                    # Determine availability date (when first became available)
                    availability_date = None
                    if availability_info.get('available') and availability_info.get('date'):
                        if isinstance(availability_info['date'], str):
                            availability_date = self._parse_date_string(availability_info['date'])
                        else:
                            availability_date = availability_info['date']
                    
                    conn.execute(
                        availability_sql,
                        [
                            ext.name,
                            'core',
                            platform,
                            analysis_result.duckdb_version,
                            availability_info.get('available', False),
                            availability_date,
                            analysis_result.analysis_timestamp,
                            availability_info.get('http_status'),
                            availability_info.get('file_size'),
                            availability_info.get('error'),
                            days_since_release,
                        ]
                    )
        
        # Save community extension availability data (if they have platform info)
        for ext in analysis_result.community_extensions:
            if ext.platform_availability:
                for platform, availability_info in ext.platform_availability.items():
                    availability_date = None
                    if availability_info.get('available') and availability_info.get('date'):
                        if isinstance(availability_info['date'], str):
                            availability_date = self._parse_date_string(availability_info['date'])
                        else:
                            availability_date = availability_info['date']
                    
                    conn.execute(
                        availability_sql,
                        [
                            ext.name,
                            'community',
                            platform,
                            analysis_result.duckdb_version,
                            availability_info.get('available', False),
                            availability_date,
                            analysis_result.analysis_timestamp,
                            availability_info.get('http_status'),
                            availability_info.get('file_size'),
                            availability_info.get('error'),
                            days_since_release,
                        ]
                    )
    
    async def _save_github_issues(self, conn: duckdb.DuckDBPyConnection, analysis_result: AnalysisResult) -> None:
        """Save GitHub issues data to database."""
        logger.info(f"Saving {len(analysis_result.github_issues)} GitHub issues to database")
        
        issues_sql = self._load_sql("insert_github_issue.sql")
        mapping_sql = self._load_sql("insert_extension_issue_mapping.sql")
        
        # Determine extension types for mapping
        core_extension_names = {ext.name for ext in analysis_result.core_extensions}
        
        for issue in analysis_result.github_issues:
            try:
                # Insert the issue
                conn.execute(
                    issues_sql,
                    [
                        issue.issue_number,
                        issue.title,
                        issue.body,
                        issue.state,
                        issue.created_at,
                        issue.updated_at,
                        issue.closed_at,
                        list(issue.labels),
                        list(issue.extension_names),
                        list(issue.platforms),
                        issue.issue_type,
                        issue.severity,
                        issue.html_url,
                        analysis_result.analysis_timestamp,
                    ]
                )
                
                # Insert extension-issue mappings
                for ext_name in issue.extension_names:
                    ext_type = 'core' if ext_name in core_extension_names else 'community'
                    
                    # Calculate relevance score based on how specifically the extension is mentioned
                    relevance_score = 1.0  # Default high relevance for named extensions
                    
                    conn.execute(
                        mapping_sql,
                        [
                            ext_name,
                            ext_type,
                            issue.issue_number,
                            relevance_score,
                            analysis_result.analysis_timestamp,
                        ]
                    )
                
            except Exception as e:
                logger.warning(f"Failed to save GitHub issue {issue.issue_number}: {e}")
                continue
        
        logger.info(f"Successfully saved GitHub issues to database")
    
    async def _save_installation_results(self, conn: duckdb.DuckDBPyConnection, analysis_result: AnalysisResult) -> None:
        """Save installation test results to database."""
        logger.info(f"Saving {len(analysis_result.installation_results)} installation test results to database")
        
        install_sql = self._load_sql("insert_installation_test.sql")
        
        # Determine extension types for classification
        core_extension_names = {ext.name for ext in analysis_result.core_extensions}
        
        for result in analysis_result.installation_results:
            try:
                ext_type = 'core' if result.extension_name in core_extension_names else 'community'
                
                # Determine error type based on error message and test environment
                error_type = None
                if result.test_environment == 'special_case':
                    error_type = 'special_case'
                elif result.error_message:
                    error_msg_lower = result.error_message.lower()
                    if 'statically linked' in error_msg_lower or 'built into' in error_msg_lower:
                        error_type = 'special_case'
                    elif 'timeout' in error_msg_lower:
                        error_type = 'timeout'
                    elif 'http' in error_msg_lower or 'network' in error_msg_lower:
                        error_type = 'download'
                    elif 'load' in error_msg_lower:
                        error_type = 'load'
                    elif 'environment' in error_msg_lower:
                        error_type = 'environment'
                    else:
                        error_type = 'install'
                
                # Get platform from installation tester
                from .installation_tester import InstallationTester
                platform = InstallationTester()._get_current_platform()
                
                conn.execute(
                    install_sql,
                    [
                        result.extension_name,
                        platform,
                        result.success,
                        result.install_time,
                        result.load_time,
                        result.error_message,
                        error_type,
                        analysis_result.duckdb_version,
                        analysis_result.analysis_timestamp,
                    ]
                )
                
            except Exception as e:
                logger.warning(f"Failed to save installation test result for {result.extension_name}: {e}")
                continue
        
        logger.info(f"Successfully saved installation test results to database")
