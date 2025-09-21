#!/usr/bin/env python3
"""
DuckDB Extensions Analysis Tool - Click-based CLI

Modern command-line interface using Click for better usability and extensibility.
"""

import asyncio
import sys
from pathlib import Path
from typing import List, Optional

import click
from loguru import logger

# Add parent directory to path for imports
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


class ClickAliasedGroup(click.Group):
    """Custom Click group that supports command aliases."""
    
    def get_command(self, ctx, cmd_name):
        # Try exact match first
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        
        # Try partial matches
        matches = [cmd for cmd in self.list_commands(ctx) if cmd.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")


@click.group(cls=ClickAliasedGroup, invoke_without_command=True)
@click.option('--version', is_flag=True, help='Show version and exit')
@click.option('--cache-info', is_flag=True, help='Show cache statistics and exit')
@click.pass_context
def cli(ctx, version, cache_info):
    """
    DuckDB Extensions Analysis Tool
    
    Analyze DuckDB extensions with intelligent caching and multiple output formats.
    
    Examples:
      analyze community                    # Analyze community extensions
      analyze core                         # Analyze core extensions  
      analyze all                          # Analyze both core and community (no GitHub issues)
      analyze all --with-issues            # Analyze with GitHub issues (may hit rate limits)
      report generate --format csv        # Generate CSV report
      database save                        # Save analysis to database
    """
    if version:
        click.echo(f"DuckDB Extensions Analysis Tool v{config.version}")
        ctx.exit()
    
    if cache_info:
        import diskcache as dc
        cache = dc.Cache(str(config.cache_dir))
        click.echo(f"Cache directory: {config.cache_dir}")
        click.echo(f"Cache size: {len(cache)} items")
        click.echo(f"Cache stats: {cache.stats()}")
        ctx.exit()
    
    # If no command specified, show help
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.group()
def analyze():
    """Analyze DuckDB extensions."""
    pass


@cli.group()
def report():
    """Generate analysis reports."""
    pass


@cli.group()
def database():
    """Database operations."""
    pass


@cli.group()
def cache():
    """Cache management."""
    pass


# Cache management commands
@cache.command('clear')
def cache_clear():
    """Clear all cached data."""
    import diskcache as dc
    cache = dc.Cache(str(config.cache_dir))
    cache.clear()
    click.echo("✅ Cache cleared")


@cache.command('info')
def cache_info():
    """Show cache information."""
    import diskcache as dc
    cache = dc.Cache(str(config.cache_dir))
    click.echo(f"Cache directory: {config.cache_dir}")
    click.echo(f"Cache size: {len(cache)} items")
    click.echo(f"Cache stats: {cache.stats()}")


# Analysis commands
@analyze.command('community')
@click.option('--cache-hours', type=int, default=None, 
              help='Cache duration in hours (0 to bypass cache)')
def analyze_community(cache_hours):
    """Analyze community extensions only."""
    asyncio.run(_run_analysis('community', cache_hours))


@analyze.command('core')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
def analyze_core(cache_hours):
    """Analyze core extensions only."""
    asyncio.run(_run_analysis('core', cache_hours))


@analyze.command('all')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
@click.option('--with-issues', is_flag=True, 
              help='Enable GitHub issues analysis (slower, may hit rate limits)')
def analyze_all(cache_hours, with_issues):
    """Analyze both core and community extensions."""
    if with_issues:
        config.enable_issues_analysis = True
        logger.info("Enabling GitHub issues analysis (--with-issues flag)")
    else:
        config.enable_issues_analysis = False
        logger.info("Skipping GitHub issues analysis (default behavior)")
    
    asyncio.run(_run_analysis('full', cache_hours))


# Report commands
@report.command('generate')
@click.option('--format', 'formats', multiple=True, 
              type=click.Choice(['markdown', 'csv', 'excel']), 
              default=['markdown'],
              help='Output format(s) - can specify multiple times')
@click.option('--with-issues', is_flag=True,
              help='Enable GitHub issues analysis (slower, may hit rate limits)')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
def report_generate(formats, with_issues, cache_hours):
    """Generate analysis report in specified format(s)."""
    if with_issues:
        config.enable_issues_analysis = True
        logger.info("Enabling GitHub issues analysis (--with-issues flag)")
    else:
        config.enable_issues_analysis = False
        logger.info("Skipping GitHub issues analysis (default behavior)")
    
    asyncio.run(_run_report_generation(list(formats), cache_hours))


# Database commands
@database.command('save')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
def database_save(cache_hours):
    """Save analysis results to database."""
    asyncio.run(_run_database_save(cache_hours))


# Shortcut commands (for backward compatibility and convenience)
@cli.command('quick')
@click.option('--format', 'formats', multiple=True,
              type=click.Choice(['markdown', 'csv', 'excel']),
              default=['markdown'],
              help='Output format(s)')
def quick_report(formats):
    """Quick report generation (same as default behavior now)."""
    config.enable_issues_analysis = False
    logger.info("Quick mode: Using default fast behavior (no GitHub issues)")
    asyncio.run(_run_report_generation(list(formats), cache_hours=1))


# Hidden implementation functions
async def _run_analysis(mode: str, cache_hours: Optional[int]):
    """Run analysis in specified mode."""
    cache_hours = cache_hours if cache_hours is not None else config.default_cache_hours
    
    if cache_hours == 0:
        logger.info("Bypassing cache for this run (fetching fresh data)")
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=cache_hours)
    
    try:
        analysis_result = await orchestrator.run_analysis_mode(mode)
        await orchestrator.save_to_database(analysis_result)
        logger.info(f"Analysis saved to database: {config.database_path}")
        orchestrator.print_analysis_summary(analysis_result)
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise click.ClickException(f"Analysis failed: {e}")


async def _run_report_generation(formats: List[str], cache_hours: Optional[int]):
    """Generate reports in specified formats."""
    cache_hours = cache_hours if cache_hours is not None else config.default_cache_hours
    
    if cache_hours == 0:
        logger.info("Bypassing cache for this run (fetching fresh data)")
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=cache_hours)
    
    try:
        report_files = await orchestrator.run_report_generation(formats)
        
        for format_type, filepath in report_files.items():
            logger.info(f"{format_type.capitalize()} report saved: {filepath}")
        
        if 'markdown' in formats:
            logger.info("Latest report updated: reports/latest.md")
            
    except Exception as e:
        logger.error(f"Report generation failed: {e}")
        raise click.ClickException(f"Report generation failed: {e}")


async def _run_database_save(cache_hours: Optional[int]):
    """Save analysis to database."""
    cache_hours = cache_hours if cache_hours is not None else config.default_cache_hours
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=cache_hours)
    
    try:
        await orchestrator.run_database_save()
        logger.info(f"Analysis saved to database: {config.database_path}")
    except Exception as e:
        logger.error(f"Database save failed: {e}")
        raise click.ClickException(f"Database save failed: {e}")


if __name__ == "__main__":
    # Configure logger - both stdout and file
    logger.remove()
    logger.add(
        sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO"
    )
    
    # Add file logging for persistent capture of analysis metrics
    from datetime import datetime
    log_file = Path(__file__).parent.parent / "logs" / f"analysis_{datetime.now().strftime('%Y%m%d')}.log"
    log_file.parent.mkdir(exist_ok=True)
    logger.add(
        str(log_file),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="INFO",
        rotation="10 MB",
        retention="30 days",
        compression="gz"
    )
    
    cli()