"""
DuckDB Release Manager for tracking DuckDB versions and releases.

Fetches release data from official DuckDB CSV and provides version information.
"""

from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path
from typing import List, Optional, Dict
import csv

import httpx
import diskcache as dc
from loguru import logger


@dataclass
class DuckDBRelease:
    """Represents a DuckDB release with all metadata."""
    
    version: str
    release_date: date
    lts: bool
    codename: Optional[str] = None
    duck_species_primary: Optional[str] = None
    duck_species_secondary: Optional[str] = None
    duck_wikipage: Optional[str] = None
    blog_post: Optional[str] = None
    end_of_life: Optional[date] = None
    
    @property
    def is_future(self) -> bool:
        """Check if this is a planned future release."""
        return self.release_date > date.today()
    
    @property
    def is_active(self) -> bool:
        """Check if this release is currently active (not EOL)."""
        if self.end_of_life is None:
            return True
        return date.today() <= self.end_of_life
    
    @property
    def version_tuple(self) -> tuple:
        """Return version as tuple for comparison (1, 4, 0) from 'v1.4.0' or '1.4.0'."""
        version_str = self.version.lstrip('v')
        parts = version_str.split('.')
        return tuple(int(p) for p in parts if p.isdigit())


class DuckDBReleaseManager:
    """Manages DuckDB release information from official CSV source."""
    
    RELEASES_CSV_URL = "https://duckdb.org/data/duckdb-releases.csv"
    CACHE_KEY = "duckdb_releases_csv"
    CACHE_DURATION_HOURS = 24
    
    def __init__(self, config, cache_hours: int = 24):
        """Initialize release manager with configuration and caching."""
        self.config = config
        self.cache_hours = cache_hours
        self.cache = dc.Cache(str(config.cache_dir))
        self._releases: Optional[List[DuckDBRelease]] = None
    
    def _parse_date(self, date_str: str) -> Optional[date]:
        """Parse date string in YYYY-MM-DD format."""
        if not date_str or date_str.strip() == '':
            return None
        try:
            return datetime.strptime(date_str.strip(), '%Y-%m-%d').date()
        except ValueError:
            logger.warning(f"Failed to parse date: {date_str}")
            return None
    
    def _parse_bool(self, bool_str: str) -> bool:
        """Parse boolean string."""
        if not bool_str or bool_str.strip() == '':
            return False
        return bool_str.strip().lower() in ('true', '1', 'yes')
    
    def _fetch_releases_csv(self) -> str:
        """Fetch releases CSV from DuckDB website with caching."""
        # Check cache first
        cached_data = self.cache.get(self.CACHE_KEY)
        if cached_data:
            cached_time, csv_content = cached_data
            age_hours = (datetime.now() - cached_time).total_seconds() / 3600
            if age_hours < self.cache_hours:
                logger.debug(f"Using cached DuckDB releases CSV (age: {age_hours:.1f}h)")
                return csv_content
        
        # Fetch from URL
        logger.info(f"Fetching DuckDB releases from {self.RELEASES_CSV_URL}")
        try:
            response = httpx.get(
                self.RELEASES_CSV_URL,
                timeout=self.config.http_timeout,
                follow_redirects=True
            )
            response.raise_for_status()
            csv_content = response.text
            
            # Cache the result
            self.cache.set(self.CACHE_KEY, (datetime.now(), csv_content))
            logger.info("Successfully fetched and cached DuckDB releases CSV")
            
            return csv_content
            
        except Exception as e:
            logger.error(f"Failed to fetch DuckDB releases CSV: {e}")
            # Try to return stale cache if available
            if cached_data:
                logger.warning("Using stale cached data due to fetch failure")
                return cached_data[1]
            raise
    
    def _parse_releases_csv(self, csv_content: str) -> List[DuckDBRelease]:
        """Parse CSV content into DuckDBRelease objects."""
        releases = []
        
        csv_reader = csv.DictReader(csv_content.splitlines())
        for row in csv_reader:
            try:
                release_date = self._parse_date(row.get('release_date', ''))
                if not release_date:
                    logger.warning(f"Skipping release with invalid date: {row}")
                    continue
                
                # Parse end of life date if present
                eol_date = self._parse_date(row.get('end_of_life', ''))
                
                # Create release object
                release = DuckDBRelease(
                    version=row.get('version_number', '').strip(),
                    release_date=release_date,
                    lts=self._parse_bool(row.get('lts', '')),
                    codename=row.get('codename', '').strip() or None,
                    duck_species_primary=row.get('duck_species_primary', '').strip() or None,
                    duck_species_secondary=row.get('duck_species_secondary', '').strip() or None,
                    duck_wikipage=row.get('duck_wikipage', '').strip() or None,
                    blog_post=row.get('blog_post', '').strip() or None,
                    end_of_life=eol_date
                )
                
                releases.append(release)
                logger.debug(f"Parsed release: {release.version} ({release.release_date})")
                
            except Exception as e:
                logger.warning(f"Failed to parse release row: {row} - {e}")
                continue
        
        # Sort by release date (newest first)
        releases.sort(key=lambda r: r.release_date, reverse=True)
        
        logger.info(f"Parsed {len(releases)} releases from CSV")
        return releases
    
    def load_releases(self) -> List[DuckDBRelease]:
        """Load all DuckDB releases from CSV."""
        if self._releases is not None:
            return self._releases
        
        csv_content = self._fetch_releases_csv()
        self._releases = self._parse_releases_csv(csv_content)
        return self._releases
    
    def get_all_releases(self) -> List[DuckDBRelease]:
        """Get all releases including future planned releases."""
        return self.load_releases()
    
    def get_past_releases(self) -> List[DuckDBRelease]:
        """Get only released versions (exclude future planned releases)."""
        all_releases = self.load_releases()
        return [r for r in all_releases if not r.is_future]
    
    def get_latest_release(self) -> Optional[DuckDBRelease]:
        """Get the most recent stable release (exclude future releases)."""
        past_releases = self.get_past_releases()
        if not past_releases:
            logger.warning("No past releases found")
            return None
        
        # Return the most recent (first in sorted list)
        latest = past_releases[0]
        logger.info(f"Latest DuckDB release: {latest.version} ({latest.release_date})")
        return latest
    
    def get_latest_lts_release(self) -> Optional[DuckDBRelease]:
        """Get the most recent LTS release."""
        past_releases = self.get_past_releases()
        lts_releases = [r for r in past_releases if r.lts]
        
        if not lts_releases:
            logger.warning("No LTS releases found")
            return None
        
        latest_lts = lts_releases[0]
        logger.info(f"Latest LTS release: {latest_lts.version} ({latest_lts.release_date})")
        return latest_lts
    
    def get_release_by_version(self, version: str) -> Optional[DuckDBRelease]:
        """Find a specific release by version number."""
        # Normalize version (handle both 'v1.4.0' and '1.4.0')
        normalized_version = version.lstrip('v')
        
        all_releases = self.load_releases()
        for release in all_releases:
            if release.version.lstrip('v') == normalized_version:
                return release
        
        logger.warning(f"Release not found for version: {version}")
        return None
    
    def get_active_releases(self) -> List[DuckDBRelease]:
        """Get all active releases (not EOL, not future)."""
        past_releases = self.get_past_releases()
        return [r for r in past_releases if r.is_active]
    
    def get_releases_for_report(self) -> List[Dict]:
        """Get release data formatted for report generation."""
        all_releases = self.load_releases()
        
        report_data = []
        for release in all_releases:
            report_data.append({
                'version': release.version,
                'release_date': release.release_date.strftime('%Y-%m-%d'),
                'codename': release.codename or '–',
                'duck_species': release.duck_species_secondary or release.duck_species_primary or '–',
                'lts': '✓' if release.lts else '',
                'blog_post': release.blog_post or '',
                'end_of_life': release.end_of_life.strftime('%Y-%m-%d') if release.end_of_life else '',
                'is_future': release.is_future,
                'status': 'Planned' if release.is_future else ('Active' if release.is_active else 'EOL')
            })
        
        return report_data
    
    def get_fallback_version(self) -> str:
        """Get fallback version from config or latest known release."""
        try:
            latest = self.get_latest_release()
            if latest:
                return latest.version
        except Exception as e:
            logger.warning(f"Failed to get latest release: {e}")
        
        # Fall back to config
        fallback = self.config.fallback_duckdb_version
        logger.info(f"Using fallback version from config: {fallback}")
        return fallback
