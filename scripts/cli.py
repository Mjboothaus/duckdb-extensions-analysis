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
      report generate --format csv        # Generate CSV report
      status core                          # Quick check if core extensions are fresh
      status community h3 prql bigquery   # Check specific community extensions
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


@cli.group()
def status():
    """Quick extension status checks."""
    pass


# Status check commands
@status.command('core')
@click.option('--max-age', type=int, default=7, 
              help='Maximum age in days before flagging as outdated (default: 7)')
@click.option('--as-of-date', type=str, default=None,
              help='Check status as of this date (YYYY-MM-DD format). Defaults to current date.')
@click.option('--json', 'output_json', is_flag=True, 
              help='Output results as JSON')
def status_core(max_age, as_of_date, output_json):
    """Check if core extensions are up-to-date with latest DuckDB release.
    
    Examples:
      status core                              # Check as of today
      status core --as-of-date 2025-09-16     # Check as of DuckDB v1.4.0 release date
      status core --max-age 14 --as-of-date 2025-09-01  # Custom age threshold and reference date
    """
    asyncio.run(_check_core_extensions_status(max_age, as_of_date, output_json))


@status.command('community')
@click.argument('extensions', nargs=-1)
@click.option('--max-age', type=int, default=30, 
              help='Maximum age in days before flagging as outdated (default: 30)')
@click.option('--as-of-date', type=str, default=None,
              help='Check status as of this date (YYYY-MM-DD format). Defaults to current date.')
@click.option('--json', 'output_json', is_flag=True, 
              help='Output results as JSON')
def status_community(extensions, max_age, as_of_date, output_json):
    """Check if specified community extensions are up-to-date.
    
    Examples:
      status community airport bigquery spatial
      status community --max-age 14 h3 prql
      status community --as-of-date 2025-09-16 h3 prql  # Check as of DuckDB v1.4.0 release
    """
    if not extensions:
        click.echo("❌ No extensions specified. Use: status community <extension1> <extension2> ...")
        return
    
    asyncio.run(_check_community_extensions_status(list(extensions), max_age, as_of_date, output_json))


@status.command('all')
@click.option('--max-age-core', type=int, default=7,
              help='Maximum age in days for core extensions (default: 7)')
@click.option('--max-age-community', type=int, default=30,
              help='Maximum age in days for community extensions (default: 30)')
@click.option('--as-of-date', type=str, default=None,
              help='Check status as of this date (YYYY-MM-DD format). Defaults to current date.')
@click.option('--json', 'output_json', is_flag=True,
              help='Output results as JSON')
@click.argument('community_extensions', nargs=-1)
def status_all(max_age_core, max_age_community, as_of_date, output_json, community_extensions):
    """Check status of core extensions and optionally specified community extensions.
    
    Examples:
      status all h3 prql                           # Check as of today
      status all --as-of-date 2025-09-16 h3 prql  # Check as of DuckDB v1.4.0 release date
    """
    asyncio.run(_check_all_extensions_status(max_age_core, max_age_community, as_of_date, list(community_extensions), output_json))


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
@click.option('--with-compatibility-testing', is_flag=True,
              help='Enable extension installation testing for version compatibility (slower, requires DuckDB installations)')
def analyze_community(cache_hours, with_compatibility_testing):
    """Analyze community extensions only."""
    asyncio.run(_run_analysis('community', cache_hours, with_compatibility_testing))


@analyze.command('core')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
@click.option('--with-compatibility-testing', is_flag=True,
              help='Enable extension installation testing for version compatibility (slower, requires DuckDB installations)')
def analyze_core(cache_hours, with_compatibility_testing):
    """Analyze core extensions only."""
    asyncio.run(_run_analysis('core', cache_hours, with_compatibility_testing))


@analyze.command('all')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
@click.option('--with-issues', is_flag=True, 
              help='Enable GitHub issues analysis (slower, may hit rate limits)')
@click.option('--with-compatibility-testing', is_flag=True,
              help='Enable extension installation testing for version compatibility (slower, requires DuckDB installations)')
def analyze_all(cache_hours, with_issues, with_compatibility_testing):
    """Analyze both core and community extensions."""
    if with_issues:
        config.enable_issues_analysis = True
        logger.info("Enabling GitHub issues analysis (--with-issues flag)")
    else:
        config.enable_issues_analysis = False
        logger.info("Skipping GitHub issues analysis (default behavior)")
    
    asyncio.run(_run_analysis('full', cache_hours, with_compatibility_testing))


# Report commands
@report.command('generate')
@click.option('--format', 'formats', multiple=True, 
              type=click.Choice(['markdown', 'csv', 'excel', 'url_validation_csv']), 
              default=['markdown'],
              help='Output format(s) - can specify multiple times. url_validation_csv generates CSV of URL validation results.')
@click.option('--with-issues', is_flag=True,
              help='Enable GitHub issues analysis (slower, may hit rate limits)')
@click.option('--cache-hours', type=int, default=None,
              help='Cache duration in hours (0 to bypass cache)')
@click.option('--as-of-date', type=str, default=None,
              help='Generate report as of this date (YYYY-MM-DD format, e.g., 2024-09-16 for DuckDB v1.4.0 release)')
def report_generate(formats, with_issues, cache_hours, as_of_date):
    """Generate analysis report in specified format(s)."""
    if with_issues:
        config.enable_issues_analysis = True
        logger.info("Enabling GitHub issues analysis (--with-issues flag)")
    else:
        config.enable_issues_analysis = False
        logger.info("Skipping GitHub issues analysis (default behavior)")
    
    asyncio.run(_run_report_generation(list(formats), cache_hours, as_of_date))


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
              type=click.Choice(['markdown', 'csv', 'excel', 'url_validation_csv']),
              default=['markdown'],
              help='Output format(s)')
def quick_report(formats):
    """Quick report generation (same as default behavior now)."""
    config.enable_issues_analysis = False
    logger.info("Quick mode: Using default fast behavior (no GitHub issues)")
    asyncio.run(_run_report_generation(list(formats), cache_hours=1))


# Hidden implementation functions
async def _run_analysis(mode: str, cache_hours: Optional[int], with_compatibility_testing: bool = False):
    """Run analysis in specified mode."""
    cache_hours = cache_hours if cache_hours is not None else config.default_cache_hours
    
    if cache_hours == 0:
        logger.info("Bypassing cache for this run (fetching fresh data)")
    
    if with_compatibility_testing:
        logger.info("Enabling extension compatibility testing (--with-compatibility-testing flag)")
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=cache_hours, enable_compatibility_testing=with_compatibility_testing)
    
    try:
        analysis_result = await orchestrator.run_analysis_mode(mode)
        await orchestrator.save_to_database(analysis_result)
        logger.info(f"Analysis saved to database: {config.database_path}")
        orchestrator.print_analysis_summary(analysis_result)
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise click.ClickException(f"Analysis failed: {e}")


async def _run_report_generation(formats: List[str], cache_hours: Optional[int], as_of_date: Optional[str] = None):
    """Generate reports in specified formats."""
    cache_hours = cache_hours if cache_hours is not None else config.default_cache_hours
    
    if cache_hours == 0:
        logger.info("Bypassing cache for this run (fetching fresh data)")
    
    if as_of_date:
        logger.info(f"Generating historical report as of date: {as_of_date}")
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=cache_hours)
    
    try:
        report_files = await orchestrator.run_report_generation(formats, as_of_date)
        
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


async def _check_core_extensions_status(max_age_days: int, as_of_date: Optional[str], output_json: bool):
    """Check if core extensions are up-to-date."""
    import json
    from datetime import datetime, timedelta
    import httpx
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=1)  # Use recent cache
    
    try:
        # Parse as_of_date if provided
        reference_date = datetime.now()
        if as_of_date:
            try:
                reference_date = datetime.strptime(as_of_date, '%Y-%m-%d')
                # Set to end of day (23:59:59) for more intuitive behavior
                reference_date = reference_date.replace(hour=23, minute=59, second=59, tzinfo=None)
            except ValueError:
                error_msg = f"Invalid date format '{as_of_date}'. Use YYYY-MM-DD format (e.g., 2025-09-16)"
                if output_json:
                    click.echo(json.dumps({"error": error_msg}))
                else:
                    click.echo(f"❌ {error_msg}")
                return
        
        async with httpx.AsyncClient() as client:
            # Get DuckDB release info
            duckdb_version, duckdb_release_date = await orchestrator.github_client.get_latest_duckdb_release(client)
            
            if not duckdb_release_date:
                if output_json:
                    click.echo(json.dumps({"error": "Could not fetch DuckDB release date"}))
                else:
                    click.echo("❌ Could not fetch DuckDB release information")
                return
            
            # Calculate age of DuckDB release relative to reference date
            # Make both dates timezone-naive for consistent comparison
            duckdb_release_date_naive = duckdb_release_date.replace(tzinfo=None)
            reference_date_naive = reference_date.replace(tzinfo=None)
            release_age_days = (reference_date_naive - duckdb_release_date_naive).days
            
            # Determine status
            is_fresh = release_age_days <= max_age_days
            
            if output_json:
                result = {
                    "duckdb_version": duckdb_version,
                    "release_date": duckdb_release_date.isoformat(),
                    "reference_date": reference_date.isoformat(),
                    "release_age_days": release_age_days,
                    "max_age_days": max_age_days,
                    "is_fresh": is_fresh,
                    "status": "fresh" if is_fresh else "outdated"
                }
                click.echo(json.dumps(result, indent=2))
            else:
                status_icon = "✅" if is_fresh else "⚠️"
                status_text = "FRESH" if is_fresh else "OUTDATED"
                
                click.echo(f"{status_icon} Core Extensions Status: {status_text}")
                click.echo(f"   DuckDB Version: {duckdb_version}")
                if as_of_date:
                    if release_age_days == 0:
                        age_desc = "same day"
                    elif release_age_days > 0:
                        age_desc = f"{release_age_days} days before reference date"
                    else:
                        age_desc = f"{abs(release_age_days)} days after reference date"
                else:
                    if release_age_days >= 0:
                        age_desc = f"{release_age_days} days ago"
                    else:
                        age_desc = f"{abs(release_age_days)} days in the future"
                click.echo(f"   Release Date: {duckdb_release_date.strftime('%Y-%m-%d')} ({age_desc})")
                if as_of_date:
                    click.echo(f"   Reference Date: {reference_date.strftime('%Y-%m-%d')} (as-of-date specified)")
                click.echo(f"   Max Age: {max_age_days} days")
                
                if not is_fresh:
                    click.echo(f"   ⚠️  DuckDB release is {release_age_days - max_age_days} days older than threshold")
                    click.echo(f"   📝 Consider updating to newer core extensions")
    
    except Exception as e:
        if output_json:
            click.echo(json.dumps({"error": str(e)}))
        else:
            click.echo(f"❌ Error checking core extensions: {e}")
        raise click.ClickException(f"Status check failed: {e}")


async def _check_community_extensions_status(extension_names: List[str], max_age_days: int, as_of_date: Optional[str], output_json: bool):
    """Check if specified community extensions are up-to-date."""
    import json
    from datetime import datetime, timedelta
    import httpx
    
    orchestrator = AnalysisOrchestrator(config, cache_hours=1)
    
    results = []
    all_fresh = True
    
    try:
        # Parse as_of_date if provided
        reference_date = datetime.now()
        if as_of_date:
            try:
                reference_date = datetime.strptime(as_of_date, '%Y-%m-%d')
                # Set to end of day (23:59:59) for more intuitive behavior  
                reference_date = reference_date.replace(hour=23, minute=59, second=59, tzinfo=None)
            except ValueError:
                error_msg = f"Invalid date format '{as_of_date}'. Use YYYY-MM-DD format (e.g., 2025-09-16)"
                if output_json:
                    click.echo(json.dumps({"error": error_msg}))
                else:
                    click.echo(f"❌ {error_msg}")
                return
        
        async with httpx.AsyncClient() as client:
            # Get community extensions
            extensions_list = await orchestrator.github_client.get_community_extensions_list(client)
            
            for ext_name in extension_names:
                if ext_name not in extensions_list:
                    result = {
                        "name": ext_name,
                        "status": "not_found",
                        "error": f"Extension '{ext_name}' not found in community extensions"
                    }
                    results.append(result)
                    all_fresh = False
                    continue
                
                # Get extension metadata
                metadata = await orchestrator.community_analyzer.get_extension_metadata(client, ext_name)
                if not metadata or "repo" not in metadata or "github" not in metadata["repo"]:
                    result = {
                        "name": ext_name,
                        "status": "no_repo",
                        "error": "No repository information found"
                    }
                    results.append(result)
                    all_fresh = False
                    continue
                
                # Get repository info
                repo = metadata["repo"]["github"]
                repo_info = await orchestrator.community_analyzer.get_repository_info(client, repo)
                
                if not repo_info or "last_push" not in repo_info:
                    result = {
                        "name": ext_name,
                        "status": "no_activity",
                        "error": "Could not fetch repository activity"
                    }
                    results.append(result)
                    all_fresh = False
                    continue
                
                # Calculate age relative to reference date
                last_push_str = repo_info["last_push"]
                try:
                    last_push_date = datetime.fromisoformat(last_push_str.rstrip("Z"))
                    # Make both dates timezone-naive for consistent comparison
                    last_push_date_naive = last_push_date.replace(tzinfo=None)
                    reference_date_naive = reference_date.replace(tzinfo=None)
                    age_days = (reference_date_naive - last_push_date_naive).days
                    is_fresh = age_days <= max_age_days
                    
                    if not is_fresh:
                        all_fresh = False
                    
                    result = {
                        "name": ext_name,
                        "repository": repo,
                        "last_push_date": last_push_date.isoformat(),
                        "reference_date": reference_date.isoformat(),
                        "age_days": age_days,
                        "max_age_days": max_age_days,
                        "is_fresh": is_fresh,
                        "status": "fresh" if is_fresh else "outdated",
                        "stars": repo_info.get("stars", 0)
                    }
                    results.append(result)
                    
                except Exception as e:
                    result = {
                        "name": ext_name,
                        "status": "date_error",
                        "error": f"Could not parse date: {e}"
                    }
                    results.append(result)
                    all_fresh = False
        
        if output_json:
            output = {
                "extensions": results,
                "summary": {
                    "total": len(extension_names),
                    "fresh": sum(1 for r in results if r.get("is_fresh", False)),
                    "outdated": sum(1 for r in results if r.get("status") == "outdated"),
                    "errors": sum(1 for r in results if "error" in r),
                    "all_fresh": all_fresh
                }
            }
            click.echo(json.dumps(output, indent=2))
        else:
            status_icon = "✅" if all_fresh else "⚠️"
            status_text = "ALL FRESH" if all_fresh else "SOME OUTDATED"
            
            click.echo(f"{status_icon} Community Extensions Status: {status_text}")
            if as_of_date:
                click.echo(f"   Reference Date: {reference_date.strftime('%Y-%m-%d')} (as-of-date specified)")
            click.echo(f"   Max Age: {max_age_days} days\n")
            
            for result in results:
                name = result["name"]
                if "error" in result:
                    click.echo(f"   ❌ {name}: {result['error']}")
                elif result.get("is_fresh", False):
                    age = result["age_days"]
                    if as_of_date:
                        if age == 0:
                            age_desc = "same day as reference"
                        elif age > 0:
                            age_desc = f"{age} days before reference date"
                        else:
                            age_desc = f"{abs(age)} days after reference date"
                    else:
                        age_desc = f"{age} days{' ago' if age >= 0 else ' in the future'}"
                    click.echo(f"   ✅ {name}: Fresh ({age_desc})")
                else:
                    age = result["age_days"]
                    if as_of_date:
                        if age == 0:
                            age_desc = "same day as reference"
                        elif age > 0:
                            age_desc = f"{age} days before reference date"
                        else:
                            age_desc = f"{abs(age)} days after reference date"
                    else:
                        age_desc = f"{age} days{' ago' if age >= 0 else ' in the future'}"
                    click.echo(f"   ⚠️  {name}: Outdated ({age_desc})")
    
    except Exception as e:
        if output_json:
            click.echo(json.dumps({"error": str(e)}))
        else:
            click.echo(f"❌ Error checking community extensions: {e}")
        raise click.ClickException(f"Status check failed: {e}")


async def _check_all_extensions_status(max_age_core: int, max_age_community: int, as_of_date: Optional[str], community_extensions: List[str], output_json: bool):
    """Check status of both core and community extensions."""
    import json
    
    if output_json:
        # For JSON output, we need to collect all results
        core_result = {}
        community_result = {}
        
        # Temporarily capture JSON output
        import io
        import contextlib
        
        # Check core extensions
        try:
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                await _check_core_extensions_status(max_age_core, as_of_date, True)
            core_json = f.getvalue()
            core_result = json.loads(core_json) if core_json.strip() else {}
        except Exception as e:
            core_result = {"error": str(e)}
        
        # Check community extensions if specified
        if community_extensions:
            try:
                f = io.StringIO()
                with contextlib.redirect_stdout(f):
                    await _check_community_extensions_status(community_extensions, max_age_community, as_of_date, True)
                community_json = f.getvalue()
                community_result = json.loads(community_json) if community_json.strip() else {}
            except Exception as e:
                community_result = {"error": str(e)}
        
        # Combine results
        combined_result = {
            "core_extensions": core_result,
            "community_extensions": community_result if community_extensions else None
        }
        
        click.echo(json.dumps(combined_result, indent=2))
    else:
        # Text output - run sequentially
        click.echo("🔍 Extension Status Check\n")
        
        click.echo("⭐ CORE EXTENSIONS:")
        await _check_core_extensions_status(max_age_core, as_of_date, False)
        
        if community_extensions:
            click.echo(f"\n🌐 COMMUNITY EXTENSIONS:")
            await _check_community_extensions_status(community_extensions, max_age_community, as_of_date, False)
        
        click.echo(f"\n🏁 Status check complete!")


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