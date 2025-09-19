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
    
    async def fetch_extension_issues(self, 
                                   extension_names: List[str], 
                                   days_back: int = 90,
                                   include_closed: bool = True) -> List[ExtensionIssue]:
        """
        Fetch GitHub issues related to specific extensions.
        
        Args:
            extension_names: List of extension names to search for
            days_back: How many days back to search for issues
            include_closed: Whether to include closed issues
            
        Returns:
            List of ExtensionIssue objects
        """
        logger.info(f"Fetching GitHub issues for {len(extension_names)} extensions")
        
        # Build search queries for extensions
        extension_queries = []
        for ext_name in extension_names:
            # Search for issues mentioning the extension name
            queries = [
                f'"{ext_name}" extension',
                f'"{ext_name}" install',
                f'"{ext_name}" load',
                f'extension {ext_name}'
            ]
            extension_queries.extend(queries)
        
        # Also search for general extension issues
        general_queries = [
            'extension install',
            'extension load',
            'extension missing',
            'extension not found',
            'extension unavailable',
            'HTTP 403 extension',
            'HTTP 404 extension'
        ]
        
        all_queries = extension_queries + general_queries
        
        # Fetch issues for all queries
        all_issues = []
        
        async with httpx.AsyncClient(timeout=30) as client:
            for i, query in enumerate(all_queries):
                try:
                    logger.debug(f"Searching issues with query {i+1}/{len(all_queries)}: {query}")
                    issues = await self._search_issues(client, query, days_back, include_closed)
                    all_issues.extend(issues)
                    
                    # Rate limiting - sleep between requests
                    if i < len(all_queries) - 1:
                        await asyncio.sleep(0.5)
                        
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
            # Determine which extensions this issue relates to
            mentioned_extensions = self._extract_mentioned_extensions(
                issue, set(extension_names)
            )
            
            if mentioned_extensions or self._is_general_extension_issue(issue):
                issue.extension_names = mentioned_extensions
                issue.platforms = self._extract_mentioned_platforms(issue)
                issue.issue_type = self._classify_issue_type(issue)
                issue.severity = self._determine_severity(issue)
                extension_issues.append(issue)
        
        logger.info(f"Found {len(extension_issues)} extension-related issues")
        return extension_issues
    
    async def _search_issues(self, 
                           client: httpx.AsyncClient, 
                           query: str, 
                           days_back: int,
                           include_closed: bool) -> List[ExtensionIssue]:
        """Search GitHub issues using the GitHub API."""
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
        
        response = await client.get(url, params=params, headers=headers)
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