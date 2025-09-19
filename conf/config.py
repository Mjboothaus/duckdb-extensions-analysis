#!/usr/bin/env python3
"""
Configuration loader for DuckDB Extensions Analysis Tool

This module loads configuration from both pyproject.toml (for version) and config.toml (for settings).
"""

import os
import toml
from pathlib import Path
from datetime import datetime
from typing import List


class Config:
    """Configuration class that loads settings from TOML files."""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.config_dir = self.project_root / "conf"

        # Load project metadata from pyproject.toml
        pyproject_path = self.project_root / "pyproject.toml"
        pyproject_data = toml.load(pyproject_path)
        self.project = pyproject_data["project"]

        # Load application configuration from config.toml
        config_path = self.config_dir / "config.toml"
        self.config_data = toml.load(config_path)

        # Set up derived properties
        self._setup_paths()
        self._setup_headers()
        self._setup_dates()

    def _setup_paths(self):
        """Set up directory paths."""
        dirs = self.config_data["directories"]
        self.cache_dir = Path(dirs["cache"])
        self.reports_dir = Path(dirs["reports"])
        self.data_dir = Path(dirs["data"])
        self.sql_dir = Path(dirs["sql"])

        # Database path
        self.database_path = self.data_dir / self.config_data["database"]["filename"]

    def _setup_headers(self):
        """Set up HTTP headers with optional GitHub token."""
        self.headers = {"Accept": self.config_data["github"]["accept_header"]}
        if github_token := os.getenv("GITHUB_TOKEN"):
            self.headers["Authorization"] = f"token {github_token}"
            self.has_github_token = True
        else:
            self.has_github_token = False

    def _setup_dates(self):
        """Set up date-related properties."""
        self.current_date = datetime.now()
        fallback_date_str = self.config_data["fallback"]["duckdb_release_date"]
        self.fallback_duckdb_date = datetime.strptime(fallback_date_str, "%Y-%m-%d")

    def ensure_directories(self):
        """Ensure all required directories exist."""
        self.cache_dir.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True)
        self.data_dir.mkdir(exist_ok=True)
        self.sql_dir.mkdir(exist_ok=True)

    def get_github_token_info(self) -> tuple[bool, str]:
        """Get GitHub token information for logging."""
        if self.has_github_token:
            return True, "Using GitHub authentication token"
        else:
            return (
                False,
                "No GitHub token found. Consider setting GITHUB_TOKEN environment variable for higher rate limits.",
            )

    def load_sql(self, filename: str) -> str:
        """Load SQL from a file in the sql directory."""
        sql_file = self.sql_dir / filename
        if not sql_file.exists():
            raise FileNotFoundError(f"SQL file not found: {sql_file}")
        return sql_file.read_text(encoding="utf-8")

    # Property accessors for easy access to config values
    @property
    def version(self) -> str:
        return self.project["version"]

    @property
    def name(self) -> str:
        return self.project["name"]

    @property
    def description(self) -> str:
        return self.project["description"]

    @property
    def github_api_base(self) -> str:
        return self.config_data["github"]["api_base"]

    @property
    def community_repo(self) -> str:
        return self.config_data["github"]["community_repo"]

    @property
    def duckdb_repo(self) -> str:
        return self.config_data["github"]["duckdb_repo"]

    @property
    def core_extensions_url(self) -> str:
        return self.config_data["analysis"]["core_extensions_url"]

    @property
    def featured_extensions_pages(self) -> List[str]:
        return self.config_data["analysis"]["featured_extensions_pages"]

    @property
    def popular_extensions(self) -> List[str]:
        return self.config_data["analysis"]["popular_extensions"]

    @property
    def default_cache_hours(self) -> int:
        return self.config_data["caching"]["default_hours"]

    @property
    def web_cache_hours(self) -> int:
        return self.config_data["caching"]["web_content_hours"]

    @property
    def enable_history(self) -> bool:
        return self.config_data["database"]["enable_history"]

    @property
    def request_timeout(self) -> int:
        return self.config_data["http"]["timeout_seconds"]

    @property
    def max_retries(self) -> int:
        return self.config_data["http"]["max_retries"]

    @property
    def retry_min_wait(self) -> int:
        return self.config_data["http"]["retry_min_wait_seconds"]

    @property
    def retry_max_wait(self) -> int:
        return self.config_data["http"]["retry_max_wait_seconds"]

    @property
    def fallback_duckdb_version(self) -> str:
        return self.config_data["fallback"]["duckdb_version"]

    @property
    def log_level(self) -> str:
        return self.config_data["logging"]["level"]

    @property
    def log_format(self) -> str:
        return self.config_data["logging"]["format"]


# Global config instance
config = Config()
