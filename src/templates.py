"""
Template Engine for DuckDB Extensions Analysis

Provides Jinja2-based templating with custom filters and data preparation.
Supports multiple output formats and configurable templates.
"""

import toml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import re

from jinja2 import Environment, FileSystemLoader, select_autoescape
from loguru import logger

from conf.config import Config


class TemplateEngine:
    """
    Jinja2-based template engine with custom filters and data preparation.
    """
    
    def __init__(self, config: Config, templates_dir: Optional[Path] = None):
        """Initialize the template engine."""
        self.config = config
        self.templates_dir = templates_dir or Path(__file__).parent.parent / "templates"
        
        # Load template configurations
        self.report_config = self._load_toml_config("report_templates.toml")
        self.table_config = self._load_toml_config("table_configs.toml")
        self.format_config = self._load_toml_config("output_formats.toml")
        
        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Register custom filters
        self._register_filters()
        
        logger.info(f"Template engine initialized with templates from: {self.templates_dir}")
    
    def _load_toml_config(self, filename: str) -> Dict[str, Any]:
        """Load TOML configuration file."""
        config_path = self.templates_dir / "config" / filename
        try:
            with open(config_path, 'r') as f:
                return toml.load(f)
        except FileNotFoundError:
            logger.warning(f"Configuration file not found: {config_path}")
            return {}
        except Exception as e:
            logger.error(f"Error loading configuration {filename}: {e}")
            return {}
    
    def _register_filters(self):
        """Register custom Jinja2 filters."""
        self.env.filters['strftime'] = self._filter_strftime
        self.env.filters['relative_date'] = self._filter_relative_date
        self.env.filters['datetime_with_relative'] = self._filter_datetime_with_relative
        self.env.filters['status_badge'] = self._filter_status_badge
        self.env.filters['number_format'] = self._filter_number_format
        self.env.filters['github_link'] = self._filter_github_link
        self.env.filters['extension_link'] = self._filter_extension_link
        self.env.filters['truncate'] = self._filter_truncate
        self.env.filters['validated_link'] = self._filter_validated_link
    
    def _filter_strftime(self, date: Union[datetime, str], format_str: str = '%Y-%m-%d') -> str:
        """Format datetime using strftime."""
        if isinstance(date, str):
            try:
                date = datetime.fromisoformat(date.replace('Z', '+00:00'))
            except:
                return str(date)
        
        if not isinstance(date, datetime):
            return str(date)
        
        return date.strftime(format_str)
    
    def _filter_relative_date(self, date_or_days: Union[datetime, int, str]) -> str:
        """Convert date or days to relative format."""
        if isinstance(date_or_days, int):
            days = date_or_days
        elif isinstance(date_or_days, str):
            try:
                days = int(date_or_days)
            except ValueError:
                return str(date_or_days)
        elif isinstance(date_or_days, datetime):
            days = (datetime.now() - date_or_days).days
        else:
            return str(date_or_days)
        
        # Use thresholds from config
        thresholds = self.format_config.get('formatting', {}).get('dates', {}).get('relative_thresholds', [
            {'days': 1, 'format': 'today'},
            {'days': 7, 'format': '{} days ago'},
            {'days': 30, 'format': '{} days ago'},
            {'days': 365, 'format': '{} days ago'},
            {'days': 99999, 'format': 'over a year ago'}
        ])
        
        for threshold in thresholds:
            if days <= threshold['days']:
                format_str = threshold['format']
                if '{}' in format_str:
                    return format_str.format(days)
                return format_str
        
        return f"{days} days ago"
    
    def _filter_datetime_with_relative(self, days_ago: Union[int, str], last_push: Optional[str] = None) -> str:
        """Format datetime with both relative time and full timestamp."""
        # Get relative time
        relative_time = self._filter_relative_date(days_ago)
        
        # If we have the actual datetime, add it in parentheses
        if last_push:
            try:
                # Parse the datetime string
                if isinstance(last_push, str):
                    # Handle ISO format with Z suffix
                    if last_push.endswith('Z'):
                        dt = datetime.fromisoformat(last_push.rstrip('Z'))
                    else:
                        dt = datetime.fromisoformat(last_push.replace('Z', '+00:00'))
                    
                    # Format the full datetime
                    full_datetime = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
                    return f"{relative_time} ({full_datetime})"
                    
            except Exception as e:
                logger.debug(f"Failed to parse datetime {last_push}: {e}")
        
        # Return just relative time if no datetime available
        return relative_time
    
    def _filter_status_badge(self, status: str) -> str:
        """Convert status to emoji badge."""
        status_mapping = self.format_config.get('formatting', {}).get('status', {
            'ongoing': '🟢 Ongoing',
            'deprecated': '⚠️ Deprecated',
            'archived': '🟡 Archived', 
            'discontinued': '🔴 Discontinued',
            'unknown': '❓ Unknown'
        })
        
        return status_mapping.get(status.lower(), f"❓ {status}")
    
    def _filter_number_format(self, number: Union[int, str, None]) -> str:
        """Format numbers with comma separators. Handle None for core extension stars."""
        if number is None:
            return "N/A (part of core DuckDB repo)"
        try:
            return f"{int(number):,}"
        except (ValueError, TypeError):
            return str(number)
    
    def _filter_github_link(self, repository: str, validation_results: Dict = None, ext_name: str = "") -> str:
        """Format repository as GitHub link with URL validation."""
        if not repository:
            return "N/A"
        
        # Determine the full URL
        if repository.startswith('http'):
            full_url = repository
            repo_match = re.search(r'github\.com/([^/]+/[^/]+)', repository)
            repo_name = repo_match.group(1) if repo_match else "Repository"
        else:
            # Assume it's in owner/repo format
            full_url = f"https://github.com/{repository}"
            repo_name = repository.split('/')[-1] if '/' in repository else repository
        
        # Check URL validation if available
        if validation_results and ext_name:
            url_key = f"{ext_name}_repository"
            if url_key in validation_results:
                validation_result = validation_results[url_key]
                if not validation_result.get('is_valid', True):
                    error_msg = validation_result.get('error_message', 'URL validation failed')
                    return f"~~[{repo_name}]({full_url})~~ **NOT FOUND:** {full_url} ({error_msg})"
        
        return f"[{repo_name}]({full_url})"
    
    def _filter_extension_link(self, name: str, url: Optional[str] = None, validation_results: Dict = None, ext_name: str = "", repository: Optional[str] = None) -> str:
        """Format extension name as link if URL is provided, with validation and repository fallback."""
        if not url:
            return name
            
        # Check URL validation if available
        if validation_results and ext_name:
            url_key = f"{ext_name}_documentation"
            if url_key in validation_results:
                validation_result = validation_results[url_key]
                if not validation_result.get('is_valid', True):
                    # If documentation URL is broken but we have a repository, use that instead
                    if repository:
                        repo_url = repository if repository.startswith('http') else f"https://github.com/{repository}"
                        return f"[{name}]({repo_url})"
                    # Otherwise show the broken link with error
                    error_msg = validation_result.get('error_message', 'URL validation failed')
                    return f"~~[{name}]({url})~~ **NOT FOUND:** {url} ({error_msg})"
            
        return f"[{name}]({url})"
    
    def _filter_truncate(self, text: str, length: int = 100, suffix: str = "...") -> str:
        """Truncate text to specified length."""
        if not text or len(text) <= length:
            return text
        return text[:length - len(suffix)].rstrip() + suffix
    
    def _filter_validated_link(self, name: str, url: Optional[str] = None, validation_results: Dict = None, ext_name: str = "") -> str:
        """Format link with URL validation status."""
        if not url:
            return name
            
        # Check validation results for this URL
        if validation_results:
            # Look for validation result for this extension's repository or documentation
            url_key_patterns = [f"{ext_name}_repository", f"{ext_name}_documentation", f"{ext_name}_external_repo"]
            validation_result = None
            
            for pattern in url_key_patterns:
                if pattern in validation_results and validation_results[pattern].get('url') == url:
                    validation_result = validation_results[pattern]
                    break
            
            # If URL is validated and broken, mark it as NOT FOUND
            if validation_result and not validation_result.get('is_valid', True):
                error_msg = validation_result.get('error_message', 'URL validation failed')
                return f"~~[{name}]({url})~~ **NOT FOUND:** {url} ({error_msg})"
        
        # URL is valid or not checked - return normal link
        return f"[{name}]({url})"
    
    def prepare_template_data(self, analysis_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepare data for template rendering.
        
        Transforms the analysis result into a structure suitable for Jinja2 templates.
        """
        # Extract basic data
        core_extensions = analysis_result.get('core_extensions', [])
        community_extensions = analysis_result.get('community_extensions', [])
        duckdb_info = analysis_result.get('duckdb_version_info', {})
        
        # Calculate statistics
        recently_active = self._count_recent_activity(community_extensions, 30)
        very_active = self._count_recent_activity(community_extensions, 7)
        
        # Extract URL validation results if available
        url_validation_results = analysis_result.get('url_validation_results', {})
        
        # Prepare template data structure
        template_data = {
            'report': {
                'name': self.report_config.get('reports', {}).get('full_analysis', {}).get('name', 'DuckDB Extensions Analysis'),
                'description': self.report_config.get('reports', {}).get('full_analysis', {}).get('description', ''),
                'timestamp': datetime.now()
            },
            'metadata': self.report_config.get('metadata', {}),
            'tables': self.table_config.get('tables', {}),
            'url_validation': url_validation_results,
            'stats': {
                'core_count': len(core_extensions),
                'community_count': len(community_extensions),
                'total_count': len(core_extensions) + len(community_extensions),
                'recently_active_count': recently_active,
                'very_active_count': very_active
            },
            'core_extensions': self._prepare_extensions_data(core_extensions),
            'community_extensions': self._prepare_extensions_data(community_extensions),
            'duckdb': {
                'version': duckdb_info.get('version'),
                'release_date': duckdb_info.get('release_date')
            },
            'tool': {
                'version': self.config.version,
                'cache_hours': getattr(self.config, 'default_cache_hours', 24),
                'issues_enabled': getattr(self.config, 'enable_issues_analysis', False)
            },
            'timestamp': datetime.now()
        }
        
        return template_data
    
    def _prepare_extensions_data(self, extensions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Prepare extensions data for template rendering."""
        prepared = []
        
        for ext in extensions:
            # Standardize extension data structure
            prepared_ext = {
                'name': ext.get('name', 'Unknown'),
                'repository': ext.get('repository', ''),
                'docs_url': ext.get('docs_url', ''),
                'status': ext.get('status', 'unknown'),
                'last_activity': ext.get('last_push_days') or ext.get('days_ago', 0),  # Handle both field names
                'last_push': ext.get('last_push'),  # Include actual datetime
                'stars': ext.get('stars', 0),
                'language': ext.get('language', 'N/A'),
                'description': ext.get('description', 'No description available'),
                'version': ext.get('version', ''),
                'topics': ext.get('topics', [])
            }
            prepared.append(prepared_ext)
        
        return prepared
    
    def _count_recent_activity(self, extensions: List[Dict[str, Any]], days_threshold: int) -> int:
        """Count extensions with recent activity within threshold."""
        count = 0
        for ext in extensions:
            last_push_days = ext.get('last_push_days', float('inf'))
            if isinstance(last_push_days, (int, float)) and last_push_days <= days_threshold:
                count += 1
        return count
    
    def render_report(self, template_name: str, analysis_result: Dict[str, Any]) -> str:
        """
        Render a report using the specified template.
        
        Args:
            template_name: Name of the template (e.g., 'full_analysis', 'core_only')
            analysis_result: Analysis data from the orchestrator
            
        Returns:
            Rendered report as string
        """
        # Get template configuration
        report_config = self.report_config.get('reports', {}).get(template_name)
        if not report_config:
            raise ValueError(f"Unknown report template: {template_name}")
        
        template_file = report_config.get('template', f'reports/{template_name}.md.j2')
        
        # Prepare data
        template_data = self.prepare_template_data(analysis_result)
        
        # Override report metadata
        template_data['report'].update({
            'name': report_config.get('name', template_data['report']['name']),
            'description': report_config.get('description', template_data['report']['description'])
        })
        
        try:
            # Load and render template
            template = self.env.get_template(template_file)
            rendered = template.render(**template_data)
            
            logger.info(f"Successfully rendered report using template: {template_file}")
            return rendered
            
        except Exception as e:
            logger.error(f"Error rendering template {template_file}: {e}")
            raise
    
    def render_component(self, component_name: str, template_data: Dict[str, Any]) -> str:
        """
        Render a specific component template.
        
        Args:
            component_name: Name of the component
            template_data: Data for template rendering
            
        Returns:
            Rendered component as string
        """
        component_config = self.report_config.get('components', {}).get(component_name)
        if not component_config:
            raise ValueError(f"Unknown component: {component_name}")
        
        template_file = component_config.get('template', f'components/{component_name}.md.j2')
        
        try:
            template = self.env.get_template(template_file)
            return template.render(**template_data)
        except Exception as e:
            logger.error(f"Error rendering component {component_name}: {e}")
            raise
    
    def get_available_templates(self) -> List[str]:
        """Get list of available report templates."""
        return list(self.report_config.get('reports', {}).keys())
    
    def get_available_components(self) -> List[str]:
        """Get list of available template components.""" 
        return list(self.report_config.get('components', {}).keys())