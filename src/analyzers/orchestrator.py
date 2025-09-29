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
from .github_issues_tracker import GitHubIssuesTracker
from .url_validator import URLValidator


class AnalysisOrchestrator:
    """Main orchestrator that coordinates all analysis modules."""
    
    def __init__(self, config, cache_hours: int = 1, enable_compatibility_testing: bool = False):
        self.config = config
        self.cache_hours = cache_hours
        self.enable_compatibility_testing = enable_compatibility_testing
        
        # Initialize all modules
        self.github_client = GitHubAPIClient(config, cache_hours)
        self.core_analyzer = CoreExtensionAnalyzer(config, self.github_client, cache_hours)
        self.community_analyzer = CommunityExtensionAnalyzer(config, self.github_client, cache_hours, enable_compatibility_testing)
        self.database_manager = DatabaseManager(config)
        self.report_generator = ReportGenerator(config)
        self.github_issues_tracker = GitHubIssuesTracker(self.github_client, cache_hours)
        self.url_validator = URLValidator(timeout=10)
    
    async def analyze_core_extensions(self, duckdb_version: Optional[str] = None) -> List[ExtensionInfo]:
        """Analyze core extensions only."""
        logger.info("Starting core extensions analysis")
        if duckdb_version:
            # Use enhanced analysis with platform availability checking
            return await self.core_analyzer.analyze_with_platform_availability(duckdb_version)
        else:
            return await self.core_analyzer.analyze()
    
    async def analyze_community_extensions(self) -> List[ExtensionInfo]:
        """Analyze community extensions only."""
        logger.info("Starting community extensions analysis")
        
        return await self.community_analyzer.analyze()
    
    async def analyze_core_extensions_historical(self, duckdb_version: str, cutoff_date) -> List[ExtensionInfo]:
        """Analyze core extensions as of a specific historical date."""
        logger.info(f"Starting historical core extensions analysis as of {cutoff_date.strftime('%Y-%m-%d')}")
        
        # Get current core extensions first
        current_extensions = await self.core_analyzer.analyze_with_platform_availability(duckdb_version)
        
        # Filter extensions based on their last activity relative to cutoff date
        historical_extensions = []
        for ext in current_extensions:
            # Check if the extension had activity before the cutoff date
            if hasattr(ext, 'last_push_date') and ext.last_push_date:
                from datetime import datetime
                try:
                    # Parse the last_push_date
                    if isinstance(ext.last_push_date, str):
                        if ext.last_push_date.endswith('Z'):
                            push_date = datetime.fromisoformat(ext.last_push_date.rstrip('Z'))
                        else:
                            push_date = datetime.fromisoformat(ext.last_push_date)
                    else:
                        push_date = ext.last_push_date
                    
                    # If extension had activity before cutoff date, include it but mark status appropriately
                    if push_date.replace(tzinfo=None) <= cutoff_date:
                        # Extension was active before cutoff - include it
                        historical_extensions.append(ext)
                        logger.debug(f"Core extension '{ext.name}' was active before {cutoff_date.strftime('%Y-%m-%d')} (last activity: {push_date.strftime('%Y-%m-%d')})")
                    else:
                        # Extension became active after cutoff - exclude it
                        logger.info(f"Core extension '{ext.name}' was NOT active as of {cutoff_date.strftime('%Y-%m-%d')} (first activity: {push_date.strftime('%Y-%m-%d')})")
                except Exception as e:
                    logger.warning(f"Could not parse date for core extension '{ext.name}': {e}")
                    # If we can't parse the date, include it to be safe
                    historical_extensions.append(ext)
            else:
                # If no date info available, include it
                historical_extensions.append(ext)
        
        logger.info(f"Historical core analysis: {len(historical_extensions)} of {len(current_extensions)} core extensions were active as of {cutoff_date.strftime('%Y-%m-%d')}")
        return historical_extensions
    
    async def analyze_community_extensions_historical(self, cutoff_date) -> List[ExtensionInfo]:
        """Analyze community extensions as of a specific historical date."""
        logger.info(f"Starting historical community extensions analysis as of {cutoff_date.strftime('%Y-%m-%d')}")
        
        # Get current community extensions first
        current_extensions = await self.community_analyzer.analyze()
        
        # Filter extensions based on their last activity relative to cutoff date
        historical_extensions = []
        for ext in current_extensions:
            # Check if the extension had activity before the cutoff date
            if hasattr(ext, 'last_push_date') and ext.last_push_date:
                from datetime import datetime
                try:
                    # Parse the last_push_date
                    if isinstance(ext.last_push_date, str):
                        if ext.last_push_date.endswith('Z'):
                            push_date = datetime.fromisoformat(ext.last_push_date.rstrip('Z'))
                        else:
                            push_date = datetime.fromisoformat(ext.last_push_date)
                    else:
                        push_date = ext.last_push_date
                    
                    # If extension had activity before cutoff date, include it
                    if push_date.replace(tzinfo=None) <= cutoff_date:
                        historical_extensions.append(ext)
                        logger.debug(f"Community extension '{ext.name}' was active before {cutoff_date.strftime('%Y-%m-%d')} (last activity: {push_date.strftime('%Y-%m-%d')})")
                    else:
                        # Extension became active after cutoff - exclude it
                        logger.info(f"Community extension '{ext.name}' was NOT active as of {cutoff_date.strftime('%Y-%m-%d')} (first activity: {push_date.strftime('%Y-%m-%d')})")
                except Exception as e:
                    logger.warning(f"Could not parse date for community extension '{ext.name}': {e}")
                    # If we can't parse the date, include it to be safe
                    historical_extensions.append(ext)
            else:
                # If no date info available, include it
                historical_extensions.append(ext)
        
        logger.info(f"Historical community analysis: {len(historical_extensions)} of {len(current_extensions)} community extensions were active as of {cutoff_date.strftime('%Y-%m-%d')}")
        return historical_extensions
    
    async def analyze_full(self) -> AnalysisResult:
        """Perform full analysis of both core and community extensions."""
        logger.info("Starting DuckDB extensions analysis")
        
        async with httpx.AsyncClient() as client:
            # Get DuckDB release information
            duckdb_version, duckdb_release_date = await self.github_client.get_latest_duckdb_release(client)
            logger.info(f"Found latest DuckDB release: {duckdb_version} (published {duckdb_release_date.strftime('%Y-%m-%d')})")
            
            # Analyze core extensions with platform availability checking
            core_extensions = await self.analyze_core_extensions(duckdb_version)
            logger.info(f"Analyzed {len(core_extensions)} core extensions")
            
            # Analyze community extensions
            community_extensions = await self.analyze_community_extensions()
            logger.info(f"Analyzed {len(community_extensions)} community extensions")
            
            # Analyze GitHub issues for all extensions (if enabled)
            github_issues = []
            if self.config.enable_issues_analysis:
                all_extension_names = [ext.name for ext in core_extensions + community_extensions]
                github_issues = await self.analyze_github_issues(all_extension_names)
            else:
                logger.info("Skipping GitHub issues analysis (disabled in configuration)")
            
            # Run installation tests for a subset of extensions (prioritize core for database mode)
            # Installation testing is disabled by default for faster report generation
            # installation_results = await self.run_installation_tests(core_extensions, community_extensions)
            installation_results = []
            
            # Validate URLs in all extensions
            all_extensions = core_extensions + community_extensions
            url_validation_results = await self.validate_extension_urls(all_extensions)
            
            # Create analysis result
            analysis_result = AnalysisResult(
                core_extensions=core_extensions,
                community_extensions=community_extensions,
                duckdb_version=duckdb_version,
                duckdb_release_date=duckdb_release_date
            )
            
            # Add GitHub issues, installation results, and URL validation to metadata
            analysis_result.github_issues = github_issues
            analysis_result.installation_results = installation_results
            analysis_result.url_validation_results = url_validation_results
            
            # Log comprehensive analysis summary for persistent tracking
            logger.info(f"ANALYSIS SUMMARY: DuckDB {duckdb_version} | Core: {len(core_extensions)} | Community: {len(community_extensions)} | Total: {len(core_extensions) + len(community_extensions)}")
            
            return analysis_result
    
    async def validate_extension_urls(self, extensions: List[ExtensionInfo]) -> Dict[str, Dict]:
        """Validate all URLs in extension data and return validation results."""
        logger.info(f"Validating URLs for {len(extensions)} extensions")
        
        standard_urls_to_validate = {}  # For standard HTTP validation
        docs_urls_to_validate = {}      # For enhanced content validation
        
        # Import report generator to get access to documentation URLs
        from .report_generator import ReportGenerator
        report_generator = ReportGenerator(self.config)
        extension_urls = report_generator._discover_core_extension_urls()
        
        for ext in extensions:
            # Collect repository URLs for standard validation
            if hasattr(ext, 'repository') and ext.repository:
                if ext.repository.startswith('http'):
                    standard_urls_to_validate[f"{ext.name}_repository"] = ext.repository
                elif '/' in ext.repository and not ext.repository.startswith('integrated_core'):
                    # For core extensions, only validate if it's NOT the main duckdb/duckdb repo
                    # since that will always be valid
                    if ext.repository != 'duckdb/duckdb':
                        standard_urls_to_validate[f"{ext.name}_repository"] = f"https://github.com/{ext.repository}"
            
            # Get documentation URLs based on extension type
            docs_url = None
            if ext.type == 'core':
                # For core extensions, use the discovered URLs
                docs_url = extension_urls.get(ext.name.lower())
            elif ext.type == 'community':
                # For community extensions, use the correct community documentation pattern
                docs_url = f"https://duckdb.org/community_extensions/extensions/{ext.name}.html"
            
            # Add documentation URLs for enhanced validation
            if docs_url:
                docs_urls_to_validate[f"{ext.name}_documentation"] = (docs_url, ext.name)
                
            # Check metadata for additional URLs
            if hasattr(ext, 'metadata') and ext.metadata:
                # Check for external repository URLs
                if isinstance(ext.metadata, dict) and 'external_repository' in ext.metadata:
                    repo_url = f"https://github.com/{ext.metadata['external_repository']}"
                    standard_urls_to_validate[f"{ext.name}_external_repo"] = repo_url
        
        # Validate standard URLs (repositories, etc.)
        validation_results = {}
        if standard_urls_to_validate:
            standard_results = await self.url_validator.validate_urls_batch(standard_urls_to_validate)
            validation_results.update(standard_results)
            logger.info(f"Validated {len(standard_urls_to_validate)} standard URLs")
        
        # Validate documentation URLs with content checking
        if docs_urls_to_validate:
            docs_results = await self.url_validator.validate_urls_with_content_batch(docs_urls_to_validate)
            validation_results.update(docs_results)
            logger.info(f"Validated {len(docs_urls_to_validate)} documentation URLs with content checking")
        
        if validation_results:
            # Post-process results to normalize status field
            normalized_results = self._normalize_validation_results(validation_results)
            logger.info(f"Total validated {len(normalized_results)} URLs")
            return normalized_results
        else:
            logger.info("No URLs found to validate")
            return {}
    
    def _normalize_validation_results(self, validation_results: Dict[str, Dict]) -> Dict[str, Dict]:
        """Normalize validation results to have consistent status field."""
        normalized = {}
        
        for key, result in validation_results.items():
            normalized_result = result.copy()
            
            # Determine status based on validation results
            if result.get('is_valid', False):
                # URL is accessible
                content_validation = result.get('content_validation')
                extension_name_found = result.get('extension_name_found')
                
                if content_validation == 'likely_wrong' or extension_name_found is False:
                    normalized_result['status'] = 'LIKELY_WRONG'
                else:
                    normalized_result['status'] = 'OK'
            else:
                # URL is not accessible
                normalized_result['status'] = 'BROKEN'
            
            # Ensure consistent fields
            if 'response_time' not in normalized_result:
                normalized_result['response_time'] = None
            if 'content_validation' not in normalized_result:
                normalized_result['content_validation'] = False
            if 'extension_name_found' not in normalized_result:
                normalized_result['extension_name_found'] = None
            
            normalized[key] = normalized_result
        
        return normalized
    
    async def analyze_full_historical(self, as_of_date: str) -> AnalysisResult:
        """Perform full analysis as of a specific historical date."""
        logger.info(f"Starting historical DuckDB extensions analysis as of {as_of_date}")
        
        from datetime import datetime
        try:
            cutoff_date = datetime.strptime(as_of_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format '{as_of_date}'. Use YYYY-MM-DD format.")
        
        async with httpx.AsyncClient() as client:
            # Get DuckDB release information (this will be current, but we'll adjust analysis)
            duckdb_version, duckdb_release_date = await self.github_client.get_latest_duckdb_release(client)
            logger.info(f"Using DuckDB release: {duckdb_version} for historical context")
            
            # Analyze core extensions with historical context
            core_extensions = await self.analyze_core_extensions_historical(duckdb_version, cutoff_date)
            logger.info(f"Analyzed {len(core_extensions)} core extensions as of {as_of_date}")
            
            # Analyze community extensions with historical context  
            community_extensions = await self.analyze_community_extensions_historical(cutoff_date)
            logger.info(f"Analyzed {len(community_extensions)} community extensions as of {as_of_date}")
            
            # Skip GitHub issues analysis for historical mode
            github_issues = []
            logger.info("Skipping GitHub issues analysis for historical mode")
            
            # Skip installation tests for historical mode
            installation_results = []
            
            # Create analysis result with historical timestamp
            analysis_result = AnalysisResult(
                core_extensions=core_extensions,
                community_extensions=community_extensions,
                duckdb_version=duckdb_version,
                duckdb_release_date=duckdb_release_date
            )
            
            # Override the analysis timestamp to reflect the historical date
            analysis_result.analysis_timestamp = cutoff_date
            
            # Add GitHub issues and installation results to metadata
            analysis_result.github_issues = github_issues
            analysis_result.installation_results = installation_results
            
            # Log comprehensive analysis summary for historical tracking
            logger.info(f"HISTORICAL ANALYSIS SUMMARY ({as_of_date}): DuckDB {duckdb_version} | Core: {len(core_extensions)} | Community: {len(community_extensions)} | Total: {len(core_extensions) + len(community_extensions)}")
            
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
                    # Try new template-based generation first, fall back to legacy if needed
                    content = await self.report_generator.generate_markdown_template(analysis_result)
                    filename = f"duckdb_extensions_report_{timestamp}.md"
                    filepath = self.report_generator.save_report(content, filename)
                    results[format_type] = filepath
                    
                elif format_type.lower() == "csv":
                    filepath = await self.report_generator.generate_csv(analysis_result)
                    results[format_type] = filepath
                    
                elif format_type.lower() == "excel":
                    filepath = await self.report_generator.generate_excel(analysis_result)
                    results[format_type] = filepath
                    
                elif format_type.lower() == "url_validation_csv":
                    filepath = await self.report_generator.generate_url_validation_csv(analysis_result)
                    if filepath:
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
            # Get DuckDB version for platform checking
            async with httpx.AsyncClient() as client:
                duckdb_version, duckdb_release_date = await self.github_client.get_latest_duckdb_release(client)
                
            core_extensions = await self.analyze_core_extensions(duckdb_version)
            
            # Run installation tests for core extensions
            # Installation testing is disabled by default for faster analysis
            # installation_results = await self.run_installation_tests(core_extensions, [])
            installation_results = []
            
            analysis_result = AnalysisResult(
                core_extensions=core_extensions,
                community_extensions=[],
                duckdb_version=duckdb_version,
                duckdb_release_date=duckdb_release_date
            )
            
            # Add installation results to metadata
            analysis_result.installation_results = installation_results
            
            return analysis_result
        
        elif mode == "community":
            community_extensions = await self.analyze_community_extensions()
            return AnalysisResult(
                core_extensions=[],
                community_extensions=community_extensions
            )
        
        elif mode == "full":
            return await self.analyze_full()
        
        else:
            raise ValueError(f"Unknown analysis mode: {mode}")
    
    async def analyze_github_issues(self, extension_names: List[str]) -> List[Any]:
        """Analyze GitHub issues related to extensions."""
        logger.info(f"Analyzing GitHub issues for {len(extension_names)} extensions")
        
        try:
            issues = await self.github_issues_tracker.fetch_extension_issues(
                extension_names=extension_names,
                days_back=self.config.issues_analysis_days_back,
                include_closed=True
            )
            return issues
        except Exception as e:
            logger.warning(f"Failed to fetch GitHub issues: {e}")
            return []
    
    async def run_installation_tests(self, core_extensions: List, community_extensions: List) -> List[Any]:
        """Run installation tests for selected extensions."""
        from .installation_tester import InstallationTester
        
        logger.info("Starting installation testing...")
        installation_tester = InstallationTester()
        
        # Select extensions to test: prioritize core extensions and featured community extensions
        extensions_to_test = set()
        
        # Add all core extensions
        extensions_to_test.update(ext.name for ext in core_extensions)
        
        # Add some community extensions (limit to avoid excessive runtime)
        for ext in community_extensions[:10]:  # Take first 10
            extensions_to_test.add(ext.name)
        
        # Limit the number of tests to avoid excessive runtime
        extensions_to_test = list(extensions_to_test)[:25]
        
        logger.info(f"Running installation tests for {len(extensions_to_test)} extensions: {extensions_to_test}")
        
        try:
            installation_results = await installation_tester.test_extensions_batch(
                extensions_to_test
            )
            logger.info(f"Installation testing completed. {len(installation_results)} results.")
            return installation_results
        except Exception as e:
            logger.warning(f"Installation testing failed: {e}")
            return []
    
    async def run_report_generation(self, formats: List[str] = None, as_of_date: str = None) -> Dict[str, str]:
        """Generate reports from cached analysis data."""
        logger.info("Generating comprehensive markdown report")
        
        if as_of_date:
            logger.info(f"Running historical analysis as of {as_of_date}")
            analysis_result = await self.analyze_full_historical(as_of_date)
        else:
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
        if analysis_result.duckdb_version:
            print(f"DuckDB Version: {analysis_result.duckdb_version}")
        print(f"Analysis Timestamp: {analysis_result.analysis_timestamp}")
        print("Analysis complete")
