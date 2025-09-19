"""
DuckDB Extensions Analysis Framework

This package provides a modular architecture for analyzing DuckDB extensions,
including core extensions, community extensions, GitHub API interactions,
database operations, and report generation.
"""

from .orchestrator import AnalysisOrchestrator
from .github_api import GitHubAPIClient
from .core_analyzer import CoreExtensionAnalyzer
from .community_analyzer import CommunityExtensionAnalyzer
from .database_manager import DatabaseManager
from .report_generator import ReportGenerator

__all__ = [
    "AnalysisOrchestrator",
    "GitHubAPIClient",
    "CoreExtensionAnalyzer", 
    "CommunityExtensionAnalyzer",
    "DatabaseManager",
    "ReportGenerator",
]