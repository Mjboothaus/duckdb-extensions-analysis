#!/usr/bin/env python3
"""
Deprecation Detection Script for DuckDB Extensions

This script analyzes extension repositories to detect potential deprecation
indicators in README files, repository descriptions, and other metadata.
It helps identify extensions that should be marked as deprecated in the
configuration file.

Usage:
    python scripts/detect_deprecated_extensions.py [--format json|markdown|csv]
    
Options:
    --cache-dir DIR      Directory to store cached data (default: .cache/deprecation_detector)
    --no-cache           Disable caching of repository data
    --cache-days DAYS    Number of days to keep cached data (default: 7)
"""

import asyncio
import json
import re
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set, Any
import csv
import pickle

import httpx
from loguru import logger

# Configure logging
logger.remove()
logger.add(
    lambda msg: print(msg, end=""),
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | {message}\n"
)

# Deprecation indicators to look for in repository content
DEPRECATION_KEYWORDS = [
    "deprecated", "deprecation", "obsolete", "unmaintained", "archived",
    "no longer maintained", "end of life", "superseded", "replaced by",
    "use instead", "migrated to", "moved to", "discontinued",
    "not recommended", "retired", "sunset", "end-of-life"
]

# Warning indicators (less certain but worth flagging)
WARNING_KEYWORDS = [
    "experimental", "alpha", "beta", "prototype", "work in progress",
    "proof of concept", "demo", "example", "test", "broken",
    "unstable", "development only", "not production ready"
]

# Positive indicators (extension is actively maintained)
ACTIVE_KEYWORDS = [
    "maintained", "actively developed", "stable", "production ready",
    "latest release", "updated recently", "new features"
]


class RepositoryCache:
    """Cache manager for repository data to reduce API calls."""
    
    def __init__(self, cache_dir: Optional[Path] = None, cache_days: int = 7, enabled: bool = True):
        self.enabled = enabled
        if not enabled:
            return
            
        self.cache_dir = cache_dir or Path('.cache/deprecation_detector')
        self.cache_days = cache_days
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Using cache directory: {self.cache_dir} (TTL: {cache_days} days)")
        
        # Clean old cache entries on startup
        self._cleanup_old_entries()
    
    def _get_cache_path(self, cache_key: str) -> Path:
        """Get the cache file path for a given key."""
        return self.cache_dir / f"{cache_key}.pkl"
    
    def _is_cache_valid(self, cache_path: Path) -> bool:
        """Check if a cache entry is still valid."""
        if not cache_path.exists():
            return False
        
        cache_age = datetime.now() - datetime.fromtimestamp(cache_path.stat().st_mtime)
        return cache_age.days < self.cache_days
    
    def get(self, cache_key: str) -> Optional[Any]:
        """Get data from cache if available and valid."""
        if not self.enabled:
            return None
            
        cache_path = self._get_cache_path(cache_key)
        
        if not self._is_cache_valid(cache_path):
            return None
        
        try:
            with open(cache_path, 'rb') as f:
                cached_data = pickle.load(f)
                logger.debug(f"Cache hit for {cache_key}")
                return cached_data
        except Exception as e:
            logger.debug(f"Cache read error for {cache_key}: {e}")
            return None
    
    def set(self, cache_key: str, data: Any) -> None:
        """Store data in cache."""
        if not self.enabled:
            return
            
        cache_path = self._get_cache_path(cache_key)
        
        try:
            with open(cache_path, 'wb') as f:
                pickle.dump(data, f)
                logger.debug(f"Cached data for {cache_key}")
        except Exception as e:
            logger.debug(f"Cache write error for {cache_key}: {e}")
    
    def _cleanup_old_entries(self) -> None:
        """Remove expired cache entries."""
        if not self.enabled or not self.cache_dir.exists():
            return
            
        cutoff_time = datetime.now() - timedelta(days=self.cache_days)
        removed_count = 0
        
        for cache_file in self.cache_dir.glob('*.pkl'):
            try:
                file_time = datetime.fromtimestamp(cache_file.stat().st_mtime)
                if file_time < cutoff_time:
                    cache_file.unlink()
                    removed_count += 1
            except Exception as e:
                logger.debug(f"Error cleaning up {cache_file}: {e}")
        
        if removed_count > 0:
            logger.info(f"Cleaned up {removed_count} expired cache entries")
    
    def clear(self) -> None:
        """Clear all cache entries."""
        if not self.enabled or not self.cache_dir.exists():
            return
            
        removed_count = 0
        for cache_file in self.cache_dir.glob('*.pkl'):
            try:
                cache_file.unlink()
                removed_count += 1
            except Exception as e:
                logger.debug(f"Error removing {cache_file}: {e}")
        
        logger.info(f"Cleared {removed_count} cache entries")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        if not self.enabled or not self.cache_dir.exists():
            return {'enabled': False}
        
        cache_files = list(self.cache_dir.glob('*.pkl'))
        total_size = sum(f.stat().st_size for f in cache_files if f.exists())
        
        return {
            'enabled': True,
            'cache_dir': str(self.cache_dir),
            'cache_days': self.cache_days,
            'entry_count': len(cache_files),
            'total_size_mb': round(total_size / (1024 * 1024), 2)
        }


class DeprecationDetector:
    """Detects potentially deprecated extensions by analyzing repository content."""
    
    def __init__(self, github_token: Optional[str] = None, cache: Optional[RepositoryCache] = None):
        self.github_token = github_token
        self.cache = cache or RepositoryCache(enabled=False)  # Default to no cache unless provided
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'DuckDB-Extensions-Analysis/1.0'
        }
        if github_token:
            self.headers['Authorization'] = f'token {github_token}'
    
    async def analyze_extension(self, client: httpx.AsyncClient, ext_name: str, repo_url: str, metadata: Optional[Dict] = None) -> Dict:
        """Analyze a single extension for deprecation indicators."""
        logger.info(f"Analyzing extension: {ext_name}")
        
        # Extract owner/repo from URL
        repo_match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
        if not repo_match:
            return {
                'extension': ext_name,
                'repository': repo_url,
                'status': 'error',
                'error': 'Invalid GitHub URL format',
                'deprecation_indicators': [],
                'warning_indicators': [],
                'active_indicators': []
            }
        
        owner, repo = repo_match.groups()
        repo = repo.rstrip('.git')  # Remove .git suffix if present
        
        result = {
            'extension': ext_name,
            'repository': repo_url,
            'owner': owner,
            'repo_name': repo,
            'status': 'analyzed',
            'deprecation_indicators': [],
            'warning_indicators': [],
            'active_indicators': [],
            'repository_archived': False,
            'last_push': None,
            'description': None,
            'readme_content': None,
            'analysis_timestamp': datetime.now().isoformat(),
            'metadata': metadata or {},
            'official_description': metadata.get('extension', {}).get('description', '') if metadata else '',
            'official_version': metadata.get('extension', {}).get('version', '') if metadata else '',
            'language': metadata.get('extension', {}).get('language', '') if metadata else '',
            'maintainers': metadata.get('extension', {}).get('maintainers', []) if metadata else [],
            'license': metadata.get('extension', {}).get('license', '') if metadata else '',
            'description_yml_url': f'https://github.com/duckdb/community-extensions/blob/main/extensions/{ext_name}/description.yml'
        }
        
        try:
            # Check official description from description.yml for deprecation indicators first
            if result['official_description']:
                result['deprecation_indicators'].extend(
                    self._find_indicators(result['official_description'], DEPRECATION_KEYWORDS, 'official_description')
                )
                result['warning_indicators'].extend(
                    self._find_indicators(result['official_description'], WARNING_KEYWORDS, 'official_description')
                )
                result['active_indicators'].extend(
                    self._find_indicators(result['official_description'], ACTIVE_KEYWORDS, 'official_description')
                )
            
            # Get repository metadata
            repo_info = await self._get_repository_info(client, owner, repo)
            if repo_info:
                result['repository_archived'] = repo_info.get('archived', False)
                result['last_push'] = repo_info.get('pushed_at')
                result['description'] = repo_info.get('description', '')
                
                # Check repository description for indicators
                if result['description']:
                    result['deprecation_indicators'].extend(
                        self._find_indicators(result['description'], DEPRECATION_KEYWORDS, 'repo_description')
                    )
                    result['warning_indicators'].extend(
                        self._find_indicators(result['description'], WARNING_KEYWORDS, 'repo_description')
                    )
                    result['active_indicators'].extend(
                        self._find_indicators(result['description'], ACTIVE_KEYWORDS, 'repo_description')
                    )
            
            # Get README content
            readme_content = await self._get_readme_content(client, owner, repo)
            if readme_content:
                result['readme_content'] = readme_content[:1000]  # First 1000 chars for reference
                
                # Analyze README for indicators
                result['deprecation_indicators'].extend(
                    self._find_indicators(readme_content, DEPRECATION_KEYWORDS, 'readme')
                )
                result['warning_indicators'].extend(
                    self._find_indicators(readme_content, WARNING_KEYWORDS, 'readme')
                )
                result['active_indicators'].extend(
                    self._find_indicators(readme_content, ACTIVE_KEYWORDS, 'readme')
                )
            
            # Calculate deprecation score
            result['deprecation_score'] = self._calculate_deprecation_score(result)
            result['recommendation'] = self._get_recommendation(result)
            
        except Exception as e:
            logger.error(f"Error analyzing {ext_name}: {e}")
            result['status'] = 'error'
            result['error'] = str(e)
        
        return result
    
    async def _get_repository_info(self, client: httpx.AsyncClient, owner: str, repo: str) -> Optional[Dict]:
        """Get repository metadata from GitHub API with caching."""
        cache_key = f"repo_info_{owner}_{repo}"
        
        # Try cache first
        cached_data = self.cache.get(cache_key)
        if cached_data is not None:
            logger.debug(f"Using cached repository info for {owner}/{repo}")
            return cached_data
        
        # Fetch from API
        try:
            url = f'https://api.github.com/repos/{owner}/{repo}'
            response = await client.get(url, headers=self.headers)
            
            repo_data = None
            if response.status_code == 200:
                repo_data = response.json()
                logger.debug(f"Fetched repository info for {owner}/{repo} from API")
            elif response.status_code == 404:
                logger.warning(f"Repository {owner}/{repo} not found")
                repo_data = {'_not_found': True}  # Cache the 404 to avoid repeated calls
            else:
                logger.warning(f"Failed to fetch repo info for {owner}/{repo}: HTTP {response.status_code}")
                return None
            
            # Cache the result (including 404s)
            self.cache.set(cache_key, repo_data)
            
            # Return None for 404s
            return None if repo_data.get('_not_found') else repo_data
                
        except Exception as e:
            logger.error(f"Error fetching repository info for {owner}/{repo}: {e}")
            return None
    
    async def _get_readme_content(self, client: httpx.AsyncClient, owner: str, repo: str) -> Optional[str]:
        """Get README content from repository with caching."""
        cache_key = f"readme_{owner}_{repo}"
        
        # Try cache first
        cached_data = self.cache.get(cache_key)
        if cached_data is not None:
            logger.debug(f"Using cached README for {owner}/{repo}")
            return cached_data if cached_data != '_not_found' else None
        
        # Fetch from API
        readme_files = ['README.md', 'README.rst', 'README.txt', 'README', 'readme.md']
        
        for readme_file in readme_files:
            try:
                url = f'https://api.github.com/repos/{owner}/{repo}/contents/{readme_file}'
                response = await client.get(url, headers=self.headers)
                
                if response.status_code == 200:
                    content = response.json()
                    if content.get('encoding') == 'base64':
                        import base64
                        readme_text = base64.b64decode(content['content']).decode('utf-8', errors='ignore')
                        logger.debug(f"Fetched README for {owner}/{repo} from API")
                        
                        # Cache the result
                        self.cache.set(cache_key, readme_text)
                        return readme_text
                        
            except Exception as e:
                logger.debug(f"Error fetching {readme_file} for {owner}/{repo}: {e}")
                continue
        
        logger.debug(f"No README found for {owner}/{repo}")
        
        # Cache the fact that no README was found
        self.cache.set(cache_key, '_not_found')
        return None
    
    def _find_indicators(self, text: str, keywords: List[str], source: str) -> List[Dict]:
        """Find keyword indicators in text."""
        if not text:
            return []
        
        text_lower = text.lower()
        indicators = []
        
        for keyword in keywords:
            if keyword.lower() in text_lower:
                # Find the context around the keyword
                pattern = re.compile(rf'.{{0,50}}{re.escape(keyword.lower())}.{{0,50}}', re.IGNORECASE)
                matches = pattern.findall(text)
                
                for match in matches[:3]:  # Limit to first 3 matches
                    indicators.append({
                        'keyword': keyword,
                        'source': source,
                        'context': match.strip()
                    })
        
        return indicators
    
    def _calculate_deprecation_score(self, result: Dict) -> float:
        """Calculate a deprecation score based on various indicators."""
        score = 0.0
        
        # Repository archived = high deprecation indicator
        if result['repository_archived']:
            score += 10.0
        
        # Deprecation keywords in content
        score += len(result['deprecation_indicators']) * 3.0
        
        # Warning indicators (less weight)
        score += len(result['warning_indicators']) * 1.0
        
        # Active indicators reduce score
        score -= len(result['active_indicators']) * 2.0
        
        # Old repositories (no recent activity) get slight score increase
        if result['last_push']:
            try:
                last_push = datetime.fromisoformat(result['last_push'].replace('Z', '+00:00'))
                days_ago = (datetime.now().replace(tzinfo=last_push.tzinfo) - last_push).days
                
                if days_ago > 365:  # No activity for over a year
                    score += 2.0
                elif days_ago > 180:  # No activity for over 6 months
                    score += 1.0
            except:
                pass
        
        return max(0.0, score)  # Don't allow negative scores
    
    def _get_recommendation(self, result: Dict) -> str:
        """Get recommendation based on analysis."""
        score = result['deprecation_score']
        
        if result['repository_archived']:
            return "DEPRECATED - Repository is archived"
        elif score >= 8.0:
            return "LIKELY DEPRECATED - High confidence"
        elif score >= 5.0:
            return "POSSIBLY DEPRECATED - Manual review recommended"
        elif score >= 3.0:
            return "REVIEW - Some deprecation indicators found"
        elif score >= 1.0:
            return "MONITOR - Minor concerns detected"
        else:
            return "ACTIVE - No significant deprecation indicators"


async def analyze_all_extensions(detector: DeprecationDetector) -> List[Dict]:
    """Analyze all extensions for deprecation indicators."""
    # For this script, we'll analyze community extensions since those are more likely to be deprecated
    # We need to get the list from the community extensions repository
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Get community extensions list
        extensions_data = await get_community_extensions_list(client, detector)
        
        if not extensions_data:
            logger.error("Could not fetch community extensions list")
            return []
        
        logger.info(f"Found {len(extensions_data)} community extensions to analyze")
        
        results = []
        for ext_name, extension_info in extensions_data.items():
            try:
                # Handle both old string format and new dict format for compatibility
                if isinstance(extension_info, str):
                    repo_url = extension_info
                    metadata = None
                else:
                    repo_url = extension_info['url']
                    metadata = extension_info.get('metadata')
                
                result = await detector.analyze_extension(client, ext_name, repo_url, metadata)
                results.append(result)
                
                # Add small delay to avoid rate limiting
                await asyncio.sleep(0.1)
                
            except Exception as e:
                logger.error(f"Failed to analyze {ext_name}: {e}")
                results.append({
                    'extension': ext_name,
                    'repository': repo_url,
                    'status': 'error',
                    'error': str(e)
                })
        
        return results


async def get_community_extensions_list(client: httpx.AsyncClient, detector: DeprecationDetector) -> Dict[str, str]:
    """Get list of community extensions from the community repository with caching."""
    cache_key = "community_extensions_list"
    
    # Try cache first
    cached_data = detector.cache.get(cache_key)
    if cached_data is not None:
        logger.info(f"Using cached community extensions list ({len(cached_data)} extensions)")
        return cached_data
    
    try:
        # Get extensions directory from community-extensions repo
        url = 'https://api.github.com/repos/duckdb/community-extensions/contents/extensions'
        response = await client.get(url, headers=detector.headers)
        
        if response.status_code != 200:
            logger.error(f"Failed to fetch community extensions list: HTTP {response.status_code}")
            return {}
        
        contents = response.json()
        extensions = {}
        
        for item in contents:
            if item['type'] == 'dir':
                ext_name = item['name']
                
                # Get the extension's metadata to find repository URL and other info
                try:
                    metadata_url = f"https://api.github.com/repos/duckdb/community-extensions/contents/extensions/{ext_name}/description.yml"
                    metadata_response = await client.get(metadata_url, headers=detector.headers)
                    
                    if metadata_response.status_code == 200:
                        import base64
                        import yaml
                        
                        metadata_content = metadata_response.json()
                        if metadata_content.get('encoding') == 'base64':
                            yaml_content = base64.b64decode(metadata_content['content']).decode('utf-8')
                            metadata = yaml.safe_load(yaml_content)
                            
                            repo_info = metadata.get('repo', {})
                            github_repo = repo_info.get('github')
                            
                            if github_repo:
                                # Store the full extension info including metadata
                                extension_info = {
                                    'url': f"https://github.com/{github_repo}",
                                    'metadata': metadata
                                }
                                extensions[ext_name] = extension_info
                                logger.debug(f"Extension {ext_name}: GitHub repo = {github_repo}, version = {metadata.get('extension', {}).get('version', 'unknown')}")
                            
                except Exception as e:
                    logger.debug(f"Could not get metadata for {ext_name}: {e}")
                
                # Small delay to avoid rate limiting
                await asyncio.sleep(0.05)
        
        # Cache the successful result
        detector.cache.set(cache_key, extensions)
        logger.info(f"Cached community extensions list ({len(extensions)} extensions)")
        
        return extensions
        
    except Exception as e:
        logger.error(f"Error fetching community extensions: {e}")
        return {}


def format_results(results: List[Dict], format_type: str = 'markdown') -> str:
    """Format analysis results in the specified format."""
    if format_type == 'json':
        return json.dumps(results, indent=2, default=str)
    
    elif format_type == 'csv':
        if not results:
            return ""
        
        output = []
        writer = csv.StringIO()
        fieldnames = ['extension', 'repository', 'recommendation', 'deprecation_score', 
                     'repository_archived', 'last_push', 'description', 'official_description',
                     'official_version', 'language', 'maintainers', 'license', 'description_yml_url']
        csv_writer = csv.DictWriter(writer, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for result in results:
            row = {field: result.get(field, '') for field in fieldnames}
            csv_writer.writerow(row)
        
        return writer.getvalue()
    
    else:  # markdown format
        output = []
        output.append("# DuckDB Extensions Deprecation Analysis Report\n")
        output.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        output.append(f"**Extensions Analyzed:** {len(results)}\n")
        
        # Summary statistics
        deprecated_count = sum(1 for r in results if 'DEPRECATED' in r.get('recommendation', ''))
        likely_deprecated = sum(1 for r in results if 'LIKELY DEPRECATED' in r.get('recommendation', ''))
        review_needed = sum(1 for r in results if 'REVIEW' in r.get('recommendation', '') or 'POSSIBLY DEPRECATED' in r.get('recommendation', ''))
        error_count = sum(1 for r in results if r.get('status') == 'error')
        
        output.append(f"**Deprecated:** {deprecated_count}")
        output.append(f"**Likely Deprecated:** {likely_deprecated}")
        output.append(f"**Need Review:** {review_needed}")
        output.append(f"**Errors:** {error_count}\n")
        
        # Sort by deprecation score (highest first)
        sorted_results = sorted(results, key=lambda x: x.get('deprecation_score', 0), reverse=True)
        
        # High priority extensions (likely deprecated)
        high_priority = [r for r in sorted_results if r.get('deprecation_score', 0) >= 5.0]
        if high_priority:
            output.append("## 🚨 High Priority - Likely Deprecated\n")
            output.append("| Extension | Repository | Version | Score | Recommendation | Last Activity |")
            output.append("|-----------|------------|---------|-------|----------------|---------------|")
            
            for result in high_priority:
                ext_name = result.get('extension', 'Unknown')
                repo = result.get('repository', '')
                owner = result.get('owner', '')
                repo_name = result.get('repo_name', '')
                score = result.get('deprecation_score', 0)
                recommendation = result.get('recommendation', 'Unknown')
                last_push = result.get('last_push', 'Unknown')
                version = result.get('official_version', 'Unknown')
                
                # Format repository as clickable link with full owner/repo
                if repo and owner and repo_name:
                    repo_display = f"[{owner}/{repo_name}]({repo})"
                elif repo:
                    repo_display = f"[{repo_name or 'repo'}]({repo})"
                else:
                    repo_display = 'Unknown'
                
                output.append(f"| {ext_name} | {repo_display} | {version} | {score:.1f} | {recommendation} | {last_push} |")
            
            output.append("")
        
        # Medium priority extensions (need review)
        medium_priority = [r for r in sorted_results if 1.0 <= r.get('deprecation_score', 0) < 5.0]
        if medium_priority:
            output.append("## ⚠️ Medium Priority - Review Recommended\n")
            output.append("| Extension | Repository | Version | Score | Recommendation |")
            output.append("|-----------|------------|---------|-------|----------------|")
            
            for result in medium_priority:
                ext_name = result.get('extension', 'Unknown')
                repo = result.get('repository', '')
                owner = result.get('owner', '')
                repo_name = result.get('repo_name', '')
                score = result.get('deprecation_score', 0)
                recommendation = result.get('recommendation', 'Unknown')
                version = result.get('official_version', 'Unknown')
                
                # Format repository as clickable link with full owner/repo
                if repo and owner and repo_name:
                    repo_display = f"[{owner}/{repo_name}]({repo})"
                elif repo:
                    repo_display = f"[{repo_name or 'repo'}]({repo})"
                else:
                    repo_display = 'Unknown'
                    
                output.append(f"| {ext_name} | {repo_display} | {version} | {score:.1f} | {recommendation} |")
            
            output.append("")
        
        # Detailed findings for high-priority extensions
        if high_priority:
            output.append("## 📋 Detailed Findings\n")
            
            for result in high_priority:
                ext_name = result.get('extension', 'Unknown')
                output.append(f"### {ext_name}\n")
                
                # Add official metadata
                if result.get('official_description'):
                    output.append(f"**Official Description:** {result.get('official_description')}\n")
                if result.get('official_version'):
                    output.append(f"**Version:** {result.get('official_version')}")
                if result.get('maintainers'):
                    maintainers = ', '.join(result.get('maintainers', []))
                    output.append(f" | **Maintainers:** {maintainers}")
                if result.get('language'):
                    output.append(f" | **Language:** {result.get('language')}")
                output.append("\n")
                
                # Link to official description.yml
                yml_url = result.get('description_yml_url', '')
                if yml_url:
                    output.append(f"**📄 [Official Metadata]({yml_url})**\n")
                
                if result.get('repository_archived'):
                    output.append("**⚠️ Repository is archived**\n")
                
                # Deprecation indicators
                deprecation_indicators = result.get('deprecation_indicators', [])
                if deprecation_indicators:
                    output.append("**Deprecation Indicators:**")
                    for indicator in deprecation_indicators[:5]:  # Limit to 5
                        keyword = indicator.get('keyword', '')
                        source = indicator.get('source', '')
                        context = indicator.get('context', '')[:100] + '...' if len(indicator.get('context', '')) > 100 else indicator.get('context', '')
                        output.append(f"- `{keyword}` in {source}: *{context}*")
                    output.append("")
                
                # Warning indicators
                warning_indicators = result.get('warning_indicators', [])
                if warning_indicators:
                    output.append("**Warning Indicators:**")
                    for indicator in warning_indicators[:3]:  # Limit to 3
                        keyword = indicator.get('keyword', '')
                        source = indicator.get('source', '')
                        output.append(f"- `{keyword}` in {source}")
                    output.append("")
        
        # Add error reporting section for debugging
        errors = [r for r in results if r.get('status') == 'error']
        if errors:
            output.append("## ❌ Analysis Errors\n")
            output.append("The following extensions had issues during analysis:\n")
            output.append("| Extension | Repository | Error |")
            output.append("|-----------|------------|-------|")
            
            for error in errors:
                ext_name = error.get('extension', 'Unknown')
                repo = error.get('repository', '')
                error_msg = error.get('error', 'Unknown error')
                
                # Format repository as clickable link
                if repo:
                    repo_display = f"[{repo}]({repo})"
                else:
                    repo_display = 'Unknown'
                    
                output.append(f"| {ext_name} | {repo_display} | {error_msg} |")
            
            output.append("")
        
        return "\n".join(output)


async def main():
    """Main function to run the deprecation analysis."""
    import argparse
    import os
    from pathlib import Path
    
    parser = argparse.ArgumentParser(description='Detect deprecated DuckDB extensions')
    parser.add_argument('--format', choices=['json', 'markdown', 'csv'], default='markdown',
                       help='Output format (default: markdown)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--github-token', help='GitHub API token (or set GITHUB_TOKEN env var)')
    parser.add_argument('--cache-dir', help='Directory to store cached data (default: .cache/deprecation_detector)')
    parser.add_argument('--no-cache', action='store_true', help='Disable caching of repository data')
    parser.add_argument('--cache-days', type=int, default=7, help='Number of days to keep cached data (default: 7)')
    
    args = parser.parse_args()
    
    # Get GitHub token
    github_token = args.github_token or os.getenv('GITHUB_TOKEN')
    if not github_token:
        logger.warning("No GitHub token provided. Rate limiting may occur.")
        logger.info("Set GITHUB_TOKEN environment variable or use --github-token option for better API limits.")
    
    # Create cache manager
    cache_enabled = not args.no_cache
    cache_dir = Path(args.cache_dir) if args.cache_dir else None
    cache = RepositoryCache(cache_dir=cache_dir, cache_days=args.cache_days, enabled=cache_enabled)
    
    # Create detector
    detector = DeprecationDetector(github_token, cache=cache)
    
    # Run analysis
    logger.info("Starting deprecation analysis...")
    results = await analyze_all_extensions(detector)
    
    # Format results
    output = format_results(results, args.format)
    
    # Save or print results
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(output, encoding='utf-8')
        logger.info(f"Results saved to: {output_path}")
    else:
        print(output)
    
    # Summary
    total = len(results)
    deprecated = sum(1 for r in results if 'DEPRECATED' in r.get('recommendation', ''))
    likely_deprecated = sum(1 for r in results if 'LIKELY DEPRECATED' in r.get('recommendation', ''))
    
    logger.success(f"Analysis complete! {total} extensions analyzed, {deprecated + likely_deprecated} flagged for review.")


if __name__ == '__main__':
    asyncio.run(main())