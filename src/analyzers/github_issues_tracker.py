"""
GitHub Issues Tracker for DuckDB Extensions Analysis.

Monitors GitHub issues related to extension availability, installation problems,
and platform-specific issues to provide context for extension delays.
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass

import httpx
from loguru import logger
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from .base import ExtensionInfo


@dataclass
class ExtensionIssue:
    """Represents a GitHub issue related to an extension."""
    issue_number: int
    title: str
    body: str
    state: str  # 'open' or 'closed'
    created_at: datetime
    updated_at: datetime
    closed_at: Optional[datetime]
    labels: List[str]
    extension_names: Set[str]  # Extensions mentioned in this issue
    platforms: Set[str]  # Platforms mentioned in this issue
    issue_type: str  # 'installation', 'availability', 'platform', 'other'
    severity: str  # 'high', 'medium', 'low'
    html_url: str


class GitHubIssuesTracker:
    """Tracks GitHub issues related to DuckDB extensions."""
    
    def __init__(self, github_client, cache_hours: int = 6):
        self.github_client = github_client
        self.cache_hours = cache_hours
        self.repo_owner = "duckdb"
        self.repo_name = "duckdb"
        
        # Keywords to identify extension-related issues
        self.extension_keywords = {
            'installation': ['install', 'loading', 'load', 'cannot load', 'failed to load'],
            'availability': ['missing', 'not found', 'unavailable', 'download', 'HTTP 404', 'HTTP 403'],
            'platform': ['macos', 'linux', 'windows', 'arm64', 'amd64', 'platform', 'architecture'],
            'build': ['build', 'compile', 'cmake', 'make', 'CI/CD']
        }
        
        # Platform identifiers
        self.platform_keywords = {
            'linux_amd64': ['linux', 'ubuntu', 'x64', 'amd64'],
            'linux_arm64': ['linux', 'arm64', 'aarch64'],
            'osx_amd64': ['macos', 'darwin', 'osx', 'x64', 'amd64', 'intel'],
            'osx_arm64': ['macos', 'darwin', 'osx', 'arm64', 'aarch64', 'm1', 'm2', 'm3', 'apple silicon'],
            'windows_amd64': ['windows', 'win32', 'win64', 'x64', 'amd64']
        }
    
    async def fetch_extension_issues_from_repos(self, 
                                              extension_repos: Dict[str, str],
                                              days_back: int = 90,
                                              include_closed: bool = True) -> List[ExtensionIssue]:
        """
        Fetch GitHub issues directly from individual extension repositories.
        
        Args:
            extension_repos: Dict mapping extension names to their repository paths (e.g., 'duckdb/duckdb-excel')
            days_back: How many days back to search for issues
            include_closed: Whether to include closed issues
            
        Returns:
            List of ExtensionIssue objects
        """
        logger.info(f"Fetching GitHub issues directly from {len(extension_repos)} extension repositories")
        
        all_issues = []
        since_date = datetime.now() - timedelta(days=days_back)
        
        async with httpx.AsyncClient(timeout=30) as client:
            for ext_name, repo_path in extension_repos.items():
                try:
                    logger.debug(f"Fetching issues for {ext_name} from {repo_path}")
                    
                    # Fetch issues from the specific repository
                    issues = await self._fetch_repository_issues(client, repo_path, since_date, include_closed)
                    
                    # Process and enrich issues
                    for issue in issues:
                        issue.extension_names = {ext_name}
                        issue.platforms = self._extract_mentioned_platforms(issue)
                        issue.issue_type = self._classify_issue_type(issue)
                        issue.severity = self._determine_severity(issue)
                        all_issues.append(issue)
                    
                    # Rate limiting - sleep between repository requests
                    await asyncio.sleep(0.1)
                        
                except Exception as e:
                    logger.warning(f"Failed to fetch issues for {ext_name} from {repo_path}: {e}")
                    continue
        
        logger.info(f"Found {len(all_issues)} issues across all extension repositories")
        return all_issues
    
    async def fetch_extension_issues(self, 
                                   extension_names: List[str], 
                                   days_back: int = 90,
                                   include_closed: bool = True) -> List[ExtensionIssue]:
        """
        Fetch GitHub issues related to specific extensions using the efficient repository-based approach.
        
        Args:
            extension_names: List of extension names to search for
            days_back: How many days back to search for issues
            include_closed: Whether to include closed issues
            
        Returns:
            List of ExtensionIssue objects
        """
        logger.info(f"Fetching GitHub issues for {len(extension_names)} extensions")
        
        # First, try to determine repository paths for extensions with known repositories
        extension_repos = {}
        
        # For core extensions with external repositories
        from .extension_metadata import ExtensionMetadata
        from pathlib import Path
        metadata = ExtensionMetadata(Path("conf"))
        
        for ext_name in extension_names:
            external_repo = metadata.get_external_repository(ext_name)
            if external_repo:
                extension_repos[ext_name] = external_repo
        
        # Use the more efficient repository-based approach if we have repositories
        if extension_repos:
            return await self.fetch_extension_issues_from_repos(extension_repos, days_back, include_closed)
        
        # Fallback to the original search approach for extensions without known repositories
        logger.info("No known repositories found, falling back to search-based approach")
        return await self._fetch_extension_issues_fallback(extension_names, days_back, include_closed)
    
    async def _fetch_repository_issues(self,
                                      client: httpx.AsyncClient,
                                      repo_path: str,
                                      since_date: datetime,
                                      include_closed: bool) -> List[ExtensionIssue]:
        """Fetch issues directly from a specific repository."""
        issues = []
        
        # Fetch open issues
        open_issues = await self._fetch_issues_by_state(client, repo_path, 'open', since_date)
        issues.extend(open_issues)
        
        # Fetch closed issues if requested
        if include_closed:
            closed_issues = await self._fetch_issues_by_state(client, repo_path, 'closed', since_date)
            issues.extend(closed_issues)
        
        return issues
    
    async def _fetch_issues_by_state(self,
                                   client: httpx.AsyncClient,
                                   repo_path: str,
                                   state: str,
                                   since_date: datetime) -> List[ExtensionIssue]:
        """Fetch issues from a repository with a specific state."""
        url = f"https://api.github.com/repos/{repo_path}/issues"
        params = {
            'state': state,
            'since': since_date.isoformat(),
            'per_page': 100,
            'sort': 'updated',
            'direction': 'desc'
        }
        
        # Add authentication if available
        headers = {}
        if hasattr(self.github_client, 'headers') and self.github_client.headers:
            headers.update(self.github_client.headers)
        
        try:
            response = await self._make_api_request(client, url, params, headers)
            response.raise_for_status()
            
            data = response.json()
            issues = []
            
            for item in data:
                try:
                    # Skip pull requests (GitHub API includes them in issues endpoint)
                    if 'pull_request' in item:
                        continue
                        
                    issue = ExtensionIssue(
                        issue_number=item['number'],
                        title=item['title'],
                        body=item.get('body', ''),
                        state=item['state'],
                        created_at=datetime.fromisoformat(item['created_at'].rstrip('Z')),
                        updated_at=datetime.fromisoformat(item['updated_at'].rstrip('Z')),
                        closed_at=datetime.fromisoformat(item['closed_at'].rstrip('Z')) if item.get('closed_at') else None,
                        labels=[label['name'] for label in item.get('labels', [])],
                        extension_names=set(),
                        platforms=set(),
                        issue_type='other',
                        severity='medium',
                        html_url=item['html_url']
                    )
                    issues.append(issue)
                except Exception as e:
                    logger.warning(f"Failed to parse issue {item.get('number', 'unknown')}: {e}")
                    continue
            
            return issues
            
        except Exception as e:
            logger.warning(f"Failed to fetch {state} issues from {repo_path}: {e}")
            return []
    
    async def _fetch_extension_issues_fallback(self, 
                                             extension_names: List[str], 
                                             days_back: int = 90,
                                             include_closed: bool = True) -> List[ExtensionIssue]:
        """Fallback method using the original search approach (less efficient but broader)."""
        logger.info("Using fallback search-based approach for GitHub issues")
        
        # Build more targeted search queries to avoid rate limits
        extension_queries = []
        for ext_name in extension_names[:10]:  # Limit to first 10 extensions to avoid rate limits
            extension_queries.append(f'extension {ext_name}')
        
        # Also search for general extension issues
        general_queries = [
            'extension install error',
            'extension load error',
            'extension not found',
        ]
        
        all_queries = extension_queries + general_queries
        all_issues = []
        
        async with httpx.AsyncClient(timeout=30) as client:
            for i, query in enumerate(all_queries):
                try:
                    logger.debug(f"Searching issues with query {i+1}/{len(all_queries)}: {query}")
                    issues = await self._search_issues(client, query, days_back, include_closed)
                    all_issues.extend(issues)
                    
                    # Longer rate limiting delay for search API
                    if i < len(all_queries) - 1:
                        await asyncio.sleep(2.0)
                        
                except Exception as e:
                    logger.warning(f"Failed to search issues with query '{query}': {e}")
                    continue
        
        # Deduplicate issues by issue number
        unique_issues = {}
        for issue in all_issues:
            if issue.issue_number not in unique_issues:
                unique_issues[issue.issue_number] = issue
        
        # Filter and enrich issues
        extension_issues = []
        for issue in unique_issues.values():
            mentioned_extensions = self._extract_mentioned_extensions(
                issue, set(extension_names)
            )
            
            if mentioned_extensions or self._is_general_extension_issue(issue):
                issue.extension_names = mentioned_extensions
                issue.platforms = self._extract_mentioned_platforms(issue)
                issue.issue_type = self._classify_issue_type(issue)
                issue.severity = self._determine_severity(issue)
                extension_issues.append(issue)
        
        logger.info(f"Found {len(extension_issues)} extension-related issues using fallback method")
        return extension_issues
    
    async def _search_issues(self, 
                           client: httpx.AsyncClient, 
                           query: str, 
                           days_back: int,
                           include_closed: bool) -> List[ExtensionIssue]:
        """Search GitHub issues using the GitHub search API (legacy method)."""
        since_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
        
        # Build GitHub search query
        search_query = f"repo:{self.repo_owner}/{self.repo_name} {query} created:>={since_date}"
        if not include_closed:
            search_query += " state:open"
        
        url = "https://api.github.com/search/issues"
        params = {
            'q': search_query,
            'sort': 'updated',
            'order': 'desc',
            'per_page': 100
        }
        
        # Add authentication if available
        headers = {}
        if hasattr(self.github_client, 'headers') and self.github_client.headers:
            headers.update(self.github_client.headers)
        
        response = await self._make_api_request(client, url, params, headers)
        response.raise_for_status()
        
        data = response.json()
        issues = []
        
        for item in data.get('items', []):
            try:
                issue = ExtensionIssue(
                    issue_number=item['number'],
                    title=item['title'],
                    body=item.get('body', ''),
                    state=item['state'],
                    created_at=datetime.fromisoformat(item['created_at'].rstrip('Z')),
                    updated_at=datetime.fromisoformat(item['updated_at'].rstrip('Z')),
                    closed_at=datetime.fromisoformat(item['closed_at'].rstrip('Z')) if item.get('closed_at') else None,
                    labels=[label['name'] for label in item.get('labels', [])],
                    extension_names=set(),
                    platforms=set(),
                    issue_type='other',
                    severity='medium',
                    html_url=item['html_url']
                )
                issues.append(issue)
            except Exception as e:
                logger.warning(f"Failed to parse issue {item.get('number', 'unknown')}: {e}")
                continue
        
        return issues
    
    def _extract_mentioned_extensions(self, issue: ExtensionIssue, known_extensions: Set[str]) -> Set[str]:
        """Extract extension names mentioned in the issue."""
        mentioned = set()
        text = f"{issue.title} {issue.body}".lower()
        
        for ext_name in known_extensions:
            # Look for exact matches and common variations
            patterns = [
                ext_name.lower(),
                f"{ext_name.lower()} extension",
                f"extension {ext_name.lower()}",
                f"`{ext_name.lower()}`",
                f"'{ext_name.lower()}'",
                f'"{ext_name.lower()}"'
            ]
            
            for pattern in patterns:
                if pattern in text:
                    mentioned.add(ext_name)
                    break
        
        return mentioned
    
    def _extract_mentioned_platforms(self, issue: ExtensionIssue) -> Set[str]:
        """Extract platforms mentioned in the issue."""
        mentioned_platforms = set()
        text = f"{issue.title} {issue.body}".lower()
        
        for platform, keywords in self.platform_keywords.items():
            for keyword in keywords:
                if keyword.lower() in text:
                    mentioned_platforms.add(platform)
                    break
        
        return mentioned_platforms
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=2, max=30),
        retry=retry_if_exception_type((httpx.RequestError, httpx.HTTPStatusError)),
        before=lambda _: logger.debug("Retrying GitHub issues search..."),
    )
    async def _make_api_request(self, client: httpx.AsyncClient, url: str, params: dict, headers: dict) -> httpx.Response:
        """Make API request with retry logic for rate limits and temporary failures."""
        response = await client.get(url, params=params, headers=headers)
        
        # Handle specific status codes
        if response.status_code == 403:
            # Check if it's a rate limit issue
            if 'rate limit' in response.text.lower() or 'x-ratelimit-remaining' in response.headers:
                remaining = response.headers.get('x-ratelimit-remaining', '0')
                reset_time = response.headers.get('x-ratelimit-reset', 'unknown')
                logger.warning(f"GitHub API rate limit hit. Remaining: {remaining}, Reset: {reset_time}")
                
                # If we have no remaining requests, wait longer
                if remaining == '0':
                    await asyncio.sleep(60)  # Wait 1 minute before retry
            else:
                logger.warning(f"GitHub API returned 403 Forbidden: {response.text[:200]}...")
        
        return response
    
    def _classify_issue_type(self, issue: ExtensionIssue) -> str:
        """Classify the type of extension issue."""
        text = f"{issue.title} {issue.body}".lower()
        
        # Check for installation issues
        for keyword in self.extension_keywords['installation']:
            if keyword in text:
                return 'installation'
        
        # Check for availability issues
        for keyword in self.extension_keywords['availability']:
            if keyword in text:
                return 'availability'
        
        # Check for platform issues
        for keyword in self.extension_keywords['platform']:
            if keyword in text:
                return 'platform'
        
        # Check for build issues
        for keyword in self.extension_keywords['build']:
            if keyword in text:
                return 'build'
        
        return 'other'
    
    def _determine_severity(self, issue: ExtensionIssue) -> str:
        """Determine the severity of the issue."""
        text = f"{issue.title} {issue.body}".lower()
        
        # High severity indicators
        high_severity_keywords = [
            'critical', 'urgent', 'crash', 'error', 'fail', 'broken',
            'cannot', 'unable', 'not working', 'not available'
        ]
        
        # Low severity indicators
        low_severity_keywords = [
            'enhancement', 'feature request', 'documentation', 'typo',
            'minor', 'improvement', 'suggestion'
        ]
        
        # Check labels
        for label in issue.labels:
            label_lower = label.lower()
            if any(word in label_lower for word in ['critical', 'urgent', 'bug', 'high']):
                return 'high'
            elif any(word in label_lower for word in ['enhancement', 'low', 'minor']):
                return 'low'
        
        # Check content
        for keyword in high_severity_keywords:
            if keyword in text:
                return 'high'
        
        for keyword in low_severity_keywords:
            if keyword in text:
                return 'low'
        
        return 'medium'
    
    def _is_general_extension_issue(self, issue: ExtensionIssue) -> bool:
        """Check if this is a general extension-related issue."""
        text = f"{issue.title} {issue.body}".lower()
        
        general_patterns = [
            'extension',
            'load extension',
            'install extension',
            'extension not found',
            'extension missing'
        ]
        
        return any(pattern in text for pattern in general_patterns)
    
    def get_extension_issues_summary(self, 
                                   issues: List[ExtensionIssue], 
                                   extension_name: str) -> Dict[str, Any]:
        """Get a summary of issues for a specific extension."""
        ext_issues = [issue for issue in issues if extension_name in issue.extension_names]
        
        if not ext_issues:
            return {
                'extension_name': extension_name,
                'total_issues': 0,
                'open_issues': 0,
                'closed_issues': 0,
                'recent_issues': 0,
                'platform_issues': {},
                'issue_types': {},
                'severity_breakdown': {}
            }
        
        # Count recent issues (last 30 days)
        recent_cutoff = datetime.now() - timedelta(days=30)
        recent_issues = [issue for issue in ext_issues if issue.created_at >= recent_cutoff]
        
        # Platform breakdown
        platform_issues = {}
        for issue in ext_issues:
            for platform in issue.platforms:
                if platform not in platform_issues:
                    platform_issues[platform] = {'open': 0, 'closed': 0}
                platform_issues[platform][issue.state] += 1
        
        # Issue type breakdown
        issue_types = {}
        for issue in ext_issues:
            issue_type = issue.issue_type
            if issue_type not in issue_types:
                issue_types[issue_type] = {'open': 0, 'closed': 0}
            issue_types[issue_type][issue.state] += 1
        
        # Severity breakdown
        severity_breakdown = {}
        for issue in ext_issues:
            severity = issue.severity
            if severity not in severity_breakdown:
                severity_breakdown[severity] = {'open': 0, 'closed': 0}
            severity_breakdown[severity][issue.state] += 1
        
        return {
            'extension_name': extension_name,
            'total_issues': len(ext_issues),
            'open_issues': len([i for i in ext_issues if i.state == 'open']),
            'closed_issues': len([i for i in ext_issues if i.state == 'closed']),
            'recent_issues': len(recent_issues),
            'platform_issues': platform_issues,
            'issue_types': issue_types,
            'severity_breakdown': severity_breakdown,
            'latest_issues': sorted(ext_issues, key=lambda x: x.updated_at, reverse=True)[:5]
        }