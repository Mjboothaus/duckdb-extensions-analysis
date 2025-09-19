"""
Analysis Orchestrator for DuckDB Extensions Analysis.

Coordinates all analysis modules and provides a unified interface.
"""

import asyncio
from datetime import datetime
from typing import List, Optional, Dict, Any

import httpx
from loguru import logger

from .base import AnalysisResult, ExtensionInfo
from .github_api import GitHubAPIClient
from .core_analyzer import CoreExtensionAnalyzer
from .community_analyzer import CommunityExtensionAnalyzer
from .database_manager import DatabaseManager
from .report_generator import ReportGenerator


class AnalysisOrchestrator:
    """Main orchestrator that coordinates all analysis modules."""
    
    def __init__(self, config, cache_hours: int = 1):
        self.config = config
        self.cache_hours = cache_hours
        
        # Initialize all modules
        self.github_client = GitHubAPIClient(config, cache_hours)
        self.core_analyzer = CoreExtensionAnalyzer(config, self.github_client, cache_hours)
        self.community_analyzer = CommunityExtensionAnalyzer(config, self.github_client, cache_hours)
        self.database_manager = DatabaseManager(config)
        self.report_generator = ReportGenerator(config)
    
    async def analyze_core_extensions(self) -> List[ExtensionInfo]:
        """Analyze core extensions only."""
        logger.info("Starting core extensions analysis")
        return await self.core_analyzer.analyze()
    
    async def analyze_community_extensions(self, featured_extensions: Optional[set[str]] = None) -> List[ExtensionInfo]:
        """Analyze community extensions only."""
        logger.info("Starting community extensions analysis")
        
        if featured_extensions is None:
            async with httpx.AsyncClient() as client:
                featured_extensions = await self.core_analyzer.get_featured_extensions(client)
        
        return await self.community_analyzer.analyze(featured_extensions)
    
    async def analyze_full(self) -> AnalysisResult:
        """Perform full analysis of both core and community extensions."""
        logger.info("Starting DuckDB extensions analysis")
        
        async with httpx.AsyncClient() as client:
            # Get DuckDB release information
            duckdb_version, duckdb_release_date = await self.github_client.get_latest_duckdb_release(client)
            logger.info(f"Found latest DuckDB release: {duckdb_version} (published {duckdb_release_date.strftime('%Y-%m-%d')})")
            
            # Get featured extensions
            featured_extensions = await self.core_analyzer.get_featured_extensions(client)
            logger.info(f"Found {len(featured_extensions)} featured extensions")
            
            # Analyze core extensions
            core_extensions = await self.analyze_core_extensions()
            
            # Analyze community extensions
            community_extensions = await self.analyze_community_extensions(featured_extensions)
            
            # Create analysis result
            analysis_result = AnalysisResult(
                core_extensions=core_extensions,
                community_extensions=community_extensions,
                featured_extensions=featured_extensions,
                duckdb_version=duckdb_version,
                duckdb_release_date=duckdb_release_date
            )
            
            return analysis_result
    
    async def generate_reports(self, analysis_result: AnalysisResult, formats: List[str] = None) -> Dict[str, str]:
        """Generate reports in specified formats."""
        if formats is None:
            formats = ["markdown"]
        
        results = {}
        timestamp = analysis_result.analysis_timestamp.strftime("%Y%m%d_%H%M%S")
        
        for format_type in formats:
            try:
                if format_type.lower() == "markdown":
                    content = await self.report_generator.generate_markdown(analysis_result)
                    filename = f"duckdb_extensions_report_{timestamp}.md"
                    filepath = self.report_generator.save_report(content, filename)
                    results[format_type] = filepath
                    
                elif format_type.lower() == "csv":
                    filepath = await self.report_generator.generate_csv(analysis_result)
                    results[format_type] = filepath
                    
                elif format_type.lower() == "excel":
                    filepath = await self.report_generator.generate_excel(analysis_result)
                    results[format_type] = filepath
                    
                else:
                    logger.warning(f"Unsupported format: {format_type}")
                    
            except Exception as e:
                logger.error(f"Failed to generate {format_type} report: {e}")
        
        return results
    
    async def save_to_database(self, analysis_result: AnalysisResult) -> None:
        """Save analysis results to database."""
        logger.info("Saving analysis to DuckDB database")
        await self.database_manager.save_analysis(analysis_result)
    
    async def run_analysis_mode(self, mode: str = "full") -> AnalysisResult:
        """Run analysis in the specified mode."""
        if mode == "core":
            core_extensions = await self.analyze_core_extensions()
            return AnalysisResult(
                core_extensions=core_extensions,
                community_extensions=[],
                featured_extensions=set()
            )
        
        elif mode == "community":
            community_extensions = await self.analyze_community_extensions()
            return AnalysisResult(
                core_extensions=[],
                community_extensions=community_extensions,
                featured_extensions=set()
            )
        
        elif mode == "full":
            return await self.analyze_full()
        
        else:
            raise ValueError(f"Unknown analysis mode: {mode}")
    
    async def run_report_generation(self, formats: List[str] = None) -> Dict[str, str]:
        """Generate reports from cached analysis data."""
        logger.info("Generating comprehensive markdown report")
        
        # For report-only mode, we need to re-run the analysis to get fresh data
        # This is because we don't have a way to load cached analysis results yet
        analysis_result = await self.analyze_full()
        
        return await self.generate_reports(analysis_result, formats)
    
    async def run_database_save(self) -> None:
        """Save analysis results to database."""
        logger.info("Saving analysis to DuckDB database")
        
        # For database-only mode, we need to re-run the analysis
        analysis_result = await self.analyze_full()
        
        await self.save_to_database(analysis_result)
    
    def print_analysis_summary(self, analysis_result: AnalysisResult) -> None:
        """Print a summary of the analysis results."""
        print(f"\n=== Analysis Summary ===")
        print(f"Core Extensions: {len(analysis_result.core_extensions)}")
        print(f"Community Extensions: {len(analysis_result.community_extensions)}")
        print(f"Featured Extensions: {len(analysis_result.featured_extensions)}")
        if analysis_result.duckdb_version:
            print(f"DuckDB Version: {analysis_result.duckdb_version}")
        print(f"Analysis Timestamp: {analysis_result.analysis_timestamp}")
        print("Analysis complete")