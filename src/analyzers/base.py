"""
Base classes and interfaces for the DuckDB Extensions Analysis framework.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExtensionInfo:
    """Data class representing extension information."""
    name: str
    type: str  # 'core' or 'community'
    description: Optional[str] = None
    repository: Optional[str] = None
    stars: Optional[int] = None
    last_push: Optional[str] = None
    days_ago: Optional[int] = None
    stage: Optional[str] = None  # For core extensions
    links: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, Any]] = None
    # Platform availability information (for core extensions)
    platform_availability: Optional[Dict[str, Dict]] = None  # platform -> {available, date, error}
    availability_date: Optional[datetime] = None  # Earliest availability date across platforms
    available_platforms: Optional[List[str]] = None  # List of platforms where extension is available


@dataclass
class AnalysisResult:
    """Data class representing analysis results."""
    core_extensions: List[ExtensionInfo]
    community_extensions: List[ExtensionInfo]
    duckdb_version: Optional[str] = None
    duckdb_release_date: Optional[datetime] = None
    analysis_timestamp: datetime = None
    github_issues: Optional[List[Any]] = None  # GitHub issues related to extensions
    installation_results: Optional[List[Any]] = None  # Installation test results
    trend_data: Optional[Dict[str, Any]] = None  # Historical trend metrics
    
    def __post_init__(self):
        if self.analysis_timestamp is None:
            self.analysis_timestamp = datetime.now()


class BaseAnalyzer(ABC):
    """Base class for all analyzers."""
    
    def __init__(self, config, cache_hours: int = 1):
        self.config = config
        self.cache_hours = cache_hours
    
    @abstractmethod
    async def analyze(self) -> List[ExtensionInfo]:
        """Perform the analysis and return extension information."""
        pass


class BaseReportGenerator(ABC):
    """Base class for report generators."""
    
    def __init__(self, config):
        self.config = config
    
    @abstractmethod
    async def generate(self, analysis_result: AnalysisResult, format_type: str) -> str:
        """Generate a report in the specified format."""
        pass
    
    @abstractmethod
    def save_report(self, content: str, filename: str) -> str:
        """Save the report to a file."""
        pass


class BaseDatabaseManager(ABC):
    """Base class for database operations."""
    
    def __init__(self, config):
        self.config = config
    
    @abstractmethod
    def create_schema(self) -> None:
        """Create the database schema."""
        pass
    
    @abstractmethod
    async def save_analysis(self, analysis_result: AnalysisResult) -> None:
        """Save analysis results to database."""
        pass