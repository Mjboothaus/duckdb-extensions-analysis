#!/usr/bin/env python3
"""
Validate Release History Table Against GitHub Releases

This script checks if the hardcoded release history table in the report template
matches the actual DuckDB releases from GitHub API, helping detect when manual
updates are needed.
"""

import asyncio
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

import httpx
from loguru import logger

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.analyzers.github_api import GitHubAPIClient
from conf.config import Config


class ReleaseHistoryValidator:
    """Validates the release history table against GitHub releases."""
    
    def __init__(self):
        self.config = Config()
        self.github_client = GitHubAPIClient(self.config)
        self.template_path = Path("templates/components/duckdb_release_info.md.j2")
        
    def parse_template_releases(self) -> Dict[str, Dict[str, str]]:
        """Parse release data from the template file."""
        if not self.template_path.exists():
            raise FileNotFoundError(f"Template file not found: {self.template_path}")
        
        content = self.template_path.read_text()
        releases = {}
        
        # Extract table rows between the header and next section
        in_table = False
        for line in content.split('\n'):
            line = line.strip()
            
            # Start parsing after table header
            if line.startswith('|---------|'):
                in_table = True
                continue
            
            # Stop at next section header (###) but not empty lines
            if in_table and (line.startswith('###') or line.startswith('**Note')):
                break
                
            # Parse table rows (handle all formats: |||, ||, and |)
            if in_table and (line.startswith('|||') or line.startswith('|| ') or (line.startswith('| ') and not line.startswith('|--'))):
                # Parse: || **v1.4.1** | 2025-10-07 | – | – | – | [Blog](url) |
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 5:  # Minimum columns needed
                    # Extract version (remove ** formatting)
                    version_raw = parts[0].strip()
                    version_match = re.search(r'v?\d+\.\d+\.\d+', version_raw)
                    if version_match:
                        version = version_match.group()
                        if not version.startswith('v'):
                            version = 'v' + version
                            
                        # Extract date
                        date_str = parts[1].strip()
                        
                        # Check if it's upcoming (has calendar emoji or "Planned")
                        is_upcoming = '📅' in version_raw or '*Planned*' in parts[2]
                        
                        # Extract blog link if present
                        blog_info = parts[5].strip() if len(parts) > 5 else "–"
                        has_blog_link = blog_info.startswith('[') and '](' in blog_info and 'http' in blog_info
                        
                        releases[version] = {
                            'date': date_str,
                            'is_upcoming': is_upcoming,
                            'has_blog_link': has_blog_link,
                            'blog_info': blog_info,
                            'raw_version': version_raw
                        }
        
        return releases
    
    async def get_github_releases(self, limit: int = 10) -> List[Dict]:
        """Fetch recent releases from GitHub."""
        async with httpx.AsyncClient() as client:
            releases = await self.github_client.get_duckdb_releases(client, limit=limit)
            return releases
    
    def format_date(self, date_str: str) -> str:
        """Format GitHub date to template format (YYYY-MM-DD)."""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d')
        except:
            return date_str
    
    async def validate_releases(self) -> Tuple[List[str], List[str], List[str]]:
        """
        Validate template releases against GitHub releases.
        
        Returns:
            Tuple of (errors, warnings, info_messages)
        """
        errors = []
        warnings = []
        info = []
        
        try:
            # Get data from both sources
            template_releases = self.parse_template_releases()
            github_releases = await self.get_github_releases(limit=15)
            
            info.append(f"📊 Found {len(template_releases)} releases in template")
            info.append(f"📊 Found {len(github_releases)} releases from GitHub")
            
            # Check each GitHub release against template
            for gh_release in github_releases[:10]:  # Check top 10
                version = gh_release['version']
                gh_date = self.format_date(gh_release['published_at'])
                is_prerelease = gh_release.get('prerelease', False)
                
                if version in template_releases:
                    template_data = template_releases[version]
                    template_date = template_data['date']
                    is_upcoming = template_data['is_upcoming']
                    has_blog_link = template_data['has_blog_link']
                    
                    # Check if release is marked as upcoming but actually released
                    if is_upcoming and not is_prerelease:
                        errors.append(f"❌ {version} is marked as upcoming but is already released ({gh_date})")
                    
                    # Check date accuracy
                    if template_date != gh_date and not is_upcoming:
                        warnings.append(f"⚠️  {version} date mismatch: template={template_date}, GitHub={gh_date}")
                    
                    # Check for blog links on major releases
                    if not has_blog_link and not is_prerelease and version.endswith('.0'):
                        warnings.append(f"⚠️  {version} (major release) missing blog link")
                        
                    info.append(f"✅ {version} found in template")
                    
                else:
                    if not is_prerelease:
                        errors.append(f"❌ {version} (released {gh_date}) missing from template")
                    else:
                        info.append(f"ℹ️  {version} (prerelease) not in template - OK")
            
            # Check for template releases that might not exist on GitHub
            gh_versions = {r['version'] for r in github_releases}
            for version in template_releases:
                if version not in gh_versions and not template_releases[version]['is_upcoming']:
                    warnings.append(f"⚠️  Template has {version} but not found in recent GitHub releases")
                    
        except Exception as e:
            errors.append(f"💥 Validation failed: {e}")
            
        return errors, warnings, info
    
    async def run_validation(self) -> bool:
        """Run the full validation and return success status."""
        logger.info("🔍 Validating Release History table...")
        
        errors, warnings, info = await self.validate_releases()
        
        # Display results
        for message in info:
            logger.info(message)
            
        for message in warnings:
            logger.warning(message)
            
        for message in errors:
            logger.error(message)
        
        # Summary
        if errors:
            logger.error(f"❌ Validation FAILED with {len(errors)} error(s)")
            logger.error("🔧 Action needed: Update templates/components/duckdb_release_info.md.j2")
            return False
        elif warnings:
            logger.warning(f"⚠️  Validation passed with {len(warnings)} warning(s)")
            logger.info("💡 Consider updating release history for accuracy")
            return True
        else:
            logger.success("✅ Release history table is up to date!")
            return True


async def main():
    """Main validation function."""
    validator = ReleaseHistoryValidator()
    success = await validator.run_validation()
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())