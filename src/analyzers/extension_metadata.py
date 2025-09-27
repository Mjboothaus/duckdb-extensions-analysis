"""
Extension metadata manager for DuckDB Extensions Analysis.

This module manages extension metadata and special cases through configuration files
instead of hardcoded logic, making the system more maintainable and extensible.
"""

import toml
from pathlib import Path
from typing import Dict, List, Optional, Set
from loguru import logger


class ExtensionMetadata:
    """Manages extension metadata and special handling rules."""
    
    def __init__(self, config_dir: Path):
        self.config_dir = config_dir
        self.metadata_file = config_dir / "extensions_metadata.toml"
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict:
        """Load extension metadata from TOML configuration file."""
        if not self.metadata_file.exists():
            logger.warning(f"Extension metadata file not found: {self.metadata_file}")
            return {}
        
        try:
            metadata = toml.load(self.metadata_file)
            logger.debug(f"Loaded extension metadata from {self.metadata_file}")
            return metadata
        except Exception as e:
            logger.warning(f"Failed to load extension metadata: {e}")
            return {}
    
    def get_core_extension_path(self, extension_name: str) -> Optional[str]:
        """Get the repository path for a core extension."""
        # Check if it has a dedicated source directory
        with_source = self.metadata.get("core_extensions", {}).get("with_source_directories", {})
        if extension_name in with_source:
            return with_source[extension_name]["path"]
        
        # Check if it's an external repository
        external = self.metadata.get("core_extensions", {}).get("external_repositories", {})
        if extension_name in external:
            return f"external:{external[extension_name]['repository']}"
        
        # Check if it's integrated into core
        integrated = self.metadata.get("core_extensions", {}).get("integrated_core", {})
        if extension_name in integrated:
            return "integrated_core"
        
        # Unknown extension
        return None
    
    def get_external_repository(self, extension_name: str) -> Optional[str]:
        """Get external repository for an extension."""
        external = self.metadata.get("core_extensions", {}).get("external_repositories", {})
        if extension_name in external:
            return external[extension_name]["repository"]
        return None
    
    def is_integrated_core_extension(self, extension_name: str) -> bool:
        """Check if an extension is integrated into core DuckDB."""
        integrated = self.metadata.get("core_extensions", {}).get("integrated_core", {})
        return extension_name in integrated
    
    def has_dedicated_source_directory(self, extension_name: str) -> bool:
        """Check if an extension has a dedicated source directory."""
        with_source = self.metadata.get("core_extensions", {}).get("with_source_directories", {})
        return extension_name in with_source
    
    def get_special_url(self, extension_name: str) -> Optional[str]:
        """Get special URL for an extension if it exists."""
        special_urls = self.metadata.get("core_extensions", {}).get("special_urls", {})
        return special_urls.get(extension_name)
    
    def get_documentation_url(self, extension_name: str) -> Optional[str]:
        """Generate documentation URL for an extension."""
        # First check for special URLs
        special_url = self.get_special_url(extension_name)
        if special_url:
            return special_url
        
        # Check if it uses overview pattern
        overview_extensions = set(self.metadata.get("url_patterns", {}).get("overview_extensions", []))
        url_patterns = self.metadata.get("url_patterns", {})
        
        if extension_name in overview_extensions:
            pattern = url_patterns.get("overview_pattern", "https://duckdb.org/docs/stable/core_extensions/{name}/overview.html")
            return pattern.format(name=extension_name)
        else:
            pattern = url_patterns.get("standard", "https://duckdb.org/docs/stable/core_extensions/{name}.html")
            return pattern.format(name=extension_name)
    
    def get_all_core_extensions(self) -> Set[str]:
        """Get all known core extension names."""
        extensions = set()
        
        # Add extensions with source directories
        with_source = self.metadata.get("core_extensions", {}).get("with_source_directories", {})
        extensions.update(with_source.keys())
        
        # Add external repository extensions
        external = self.metadata.get("core_extensions", {}).get("external_repositories", {})
        extensions.update(external.keys())
        
        # Add integrated core extensions
        integrated = self.metadata.get("core_extensions", {}).get("integrated_core", {})
        extensions.update(integrated.keys())
        
        return extensions
    
    def get_extension_description(self, extension_name: str) -> Optional[str]:
        """Get description for an extension."""
        # Check external repositories
        external = self.metadata.get("core_extensions", {}).get("external_repositories", {})
        if extension_name in external:
            return external[extension_name].get("description")
        
        # Check integrated core
        integrated = self.metadata.get("core_extensions", {}).get("integrated_core", {})
        if extension_name in integrated:
            return integrated[extension_name].get("description")
        
        return None
    
    def is_deprecated_extension(self, extension_name: str) -> bool:
        """Check if a community extension is deprecated."""
        deprecated = self.metadata.get("community_extensions", {}).get("deprecated", {})
        return extension_name in deprecated
    
    def get_deprecated_extension_info(self, extension_name: str) -> Optional[Dict]:
        """Get deprecation information for an extension."""
        deprecated = self.metadata.get("community_extensions", {}).get("deprecated", {})
        return deprecated.get(extension_name)
    
    def is_review_required_extension(self, extension_name: str) -> bool:
        """Check if a community extension requires review for deprecation."""
        review_required = self.metadata.get("community_extensions", {}).get("review_required", {})
        return extension_name in review_required
    
    def get_review_required_extension_info(self, extension_name: str) -> Optional[Dict]:
        """Get review information for an extension."""
        review_required = self.metadata.get("community_extensions", {}).get("review_required", {})
        return review_required.get(extension_name)
    
    def is_template_extension(self, extension_name: str) -> bool:
        """Check if a community extension is a template extension."""
        templates = self.metadata.get("community_extensions", {}).get("templates", {})
        return extension_name in templates
    
    def get_template_extension_info(self, extension_name: str) -> Optional[Dict]:
        """Get template information for an extension."""
        templates = self.metadata.get("community_extensions", {}).get("templates", {})
        return templates.get(extension_name)
    
    def reload_metadata(self) -> None:
        """Reload metadata from file."""
        self.metadata = self._load_metadata()
        logger.info("Extension metadata reloaded")


# Convenience functions for backward compatibility
def get_extension_metadata(config_dir: Path) -> ExtensionMetadata:
    """Get extension metadata manager instance."""
    return ExtensionMetadata(config_dir)