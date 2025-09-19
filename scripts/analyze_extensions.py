#!/usr/bin/env python3
"""
Refactored DuckDB Extensions Analysis Tool

This script provides comprehensive analysis of DuckDB extensions using a modular architecture.
Features intelligent caching to speed up subsequent runs.
"""

import argparse
import asyncio
import sys
from pathlib import Path

from loguru import logger

# Configure logger
logger.remove()
logger.add(
    sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO"
)

# Import configuration and analyzers (add parent directory to path)
sys.path.insert(0, str(Path(__file__).parent.parent))
from conf.config import Config
from src.analyzers import AnalysisOrchestrator

# Initialize configuration
config = Config()

# Log GitHub token status
has_token, token_msg = config.get_github_token_info()
if has_token:
    logger.info(token_msg)
else:
    logger.warning(token_msg)


async def main():
    """Main entry point for the DuckDB extensions analysis tool."""
    parser = argparse.ArgumentParser(
        description="Analyze DuckDB extensions with intelligent caching",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    analyze_extensions_new.py community           # Analyze only community extensions
    analyze_extensions_new.py core               # Analyze only core extensions  
    analyze_extensions_new.py full               # Analyze both core and community
    analyze_extensions_new.py report             # Generate markdown report
    analyze_extensions_new.py report --csv       # Generate report in CSV format
    analyze_extensions_new.py report --excel     # Generate report in Excel format
    analyze_extensions_new.py database           # Save analysis to DuckDB database
    analyze_extensions_new.py --clear-cache      # Clear cache and run full analysis
    analyze_extensions_new.py --no-cache         # Bypass cache for this run
        """,
    )
    
    parser.add_argument(
        "mode",
        choices=["community", "core", "full", "report", "database"],
        help="Analysis mode to run",
    )
    
    parser.add_argument(
        "--clear-cache", 
        action="store_true", 
        help="Clear cache before running analysis"
    )
    
    parser.add_argument(
        "--no-cache", 
        action="store_true", 
        help="Bypass cache for this run (fetch fresh data)"
    )
    
    parser.add_argument(
        "--csv", 
        action="store_true", 
        help="Generate CSV output (only for report mode)"
    )
    
    parser.add_argument(
        "--excel", 
        action="store_true", 
        help="Generate Excel output (only for report mode)"
    )
    
    parser.add_argument(
        "--cache-info", 
        action="store_true", 
        help="Show cache statistics"
    )

    args = parser.parse_args()

    # Clear cache if requested
    if args.clear_cache:
        logger.info("Clearing cache...")
        import diskcache as dc
        cache = dc.Cache(str(config.cache_dir))
        cache.clear()
        logger.info("Cache cleared")

    # Set cache hours (1 hour default, 0 if bypassing cache)
    cache_hours = 0 if args.no_cache else config.default_cache_hours
    if args.no_cache:
        logger.info("Bypassing cache for this run (fetching fresh data)")

    # Show cache info if requested
    if args.cache_info:
        import diskcache as dc
        cache = dc.Cache(str(config.cache_dir))
        logger.info(f"Cache directory: {config.cache_dir}")
        logger.info(f"Cache size: {len(cache)} items")
        logger.info(f"Cache stats: {cache.stats()}")
        return

    # Initialize the orchestrator
    orchestrator = AnalysisOrchestrator(config, cache_hours=cache_hours)

    try:
        if args.mode in ["community", "core", "full"]:
            # Run analysis
            analysis_result = await orchestrator.run_analysis_mode(args.mode)
            
            # Save to database automatically for all analysis modes
            await orchestrator.save_to_database(analysis_result)
            logger.info(f"Analysis saved to database: {config.database_path}")
            
            orchestrator.print_analysis_summary(analysis_result)
            
        elif args.mode == "report":
            # Determine report formats
            formats = ["markdown"]  # Default
            if args.csv:
                formats.append("csv")
            if args.excel:
                formats.append("excel")
            
            # Generate reports
            report_files = await orchestrator.run_report_generation(formats)
            
            for format_type, filepath in report_files.items():
                logger.info(f"{format_type.capitalize()} report saved: {filepath}")
            
            if not args.csv and not args.excel:
                logger.info("Latest report updated: reports/latest.md")
            
        elif args.mode == "database":
            # Save to database
            await orchestrator.run_database_save()
            logger.info(f"Analysis saved to database: {config.database_path}")

    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        if logger.level("DEBUG").no >= logger._core.min_level:
            logger.exception("Full traceback:")
        sys.exit(1)

    logger.info("Analysis complete")


if __name__ == "__main__":
    asyncio.run(main())