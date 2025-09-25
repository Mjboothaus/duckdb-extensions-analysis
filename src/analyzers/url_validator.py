"""
URL Validator for DuckDB Extensions Analysis.

Provides utilities to validate GitHub repository URLs and documentation URLs.
"""

import asyncio
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

import httpx
from loguru import logger


class URLValidator:
    """Validates URLs for GitHub repositories and documentation."""
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
    
    async def validate_url(self, url: str) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        Validate a single URL.
        
        Returns:
            (is_valid, status_code, error_message)
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.head(url, follow_redirects=True)
                is_valid = 200 <= response.status_code < 400
                error_message = None if is_valid else f"HTTP {response.status_code}"
                return is_valid, response.status_code, error_message
        except httpx.TimeoutException:
            return False, None, "Request timeout"
        except httpx.RequestError as e:
            return False, None, f"Request error: {str(e)}"
        except Exception as e:
            return False, None, f"Unexpected error: {str(e)}"
    
    async def validate_urls_batch(self, urls: Dict[str, str]) -> Dict[str, Dict]:
        """
        Validate multiple URLs in batch.
        
        Args:
            urls: Dict mapping names to URLs
            
        Returns:
            Dict mapping names to validation results
        """
        results = {}
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            tasks = []
            for name, url in urls.items():
                task = self._validate_url_with_client(client, name, url)
                tasks.append(task)
            
            # Process in batches to avoid overwhelming the server
            batch_size = 10
            for i in range(0, len(tasks), batch_size):
                batch = tasks[i:i + batch_size]
                batch_results = await asyncio.gather(*batch, return_exceptions=True)
                
                for result in batch_results:
                    if isinstance(result, Exception):
                        logger.warning(f"Batch validation error: {result}")
                    elif result:
                        name, validation_result = result
                        results[name] = validation_result
                
                # Small delay between batches
                if i + batch_size < len(tasks):
                    await asyncio.sleep(0.5)
        
        return results
    
    async def _validate_url_with_client(self, client: httpx.AsyncClient, name: str, url: str) -> Optional[Tuple[str, Dict]]:
        """Validate a URL with a provided client."""
        try:
            response = await client.head(url, follow_redirects=True)
            is_valid = 200 <= response.status_code < 400
            error_message = None if is_valid else f"HTTP {response.status_code}"
            
            result = {
                'url': url,
                'is_valid': is_valid,
                'status_code': response.status_code,
                'final_url': str(response.url),
                'error_message': error_message
            }
            return name, result
        except httpx.TimeoutException:
            result = {
                'url': url,
                'is_valid': False,
                'status_code': None,
                'final_url': None,
                'error_message': 'Request timeout'
            }
            return name, result
        except httpx.RequestError as e:
            result = {
                'url': url,
                'is_valid': False,
                'status_code': None,
                'final_url': None,
                'error_message': f'Request error: {str(e)}'
            }
            return name, result
        except Exception as e:
            logger.warning(f"Error validating {name} ({url}): {e}")
            result = {
                'url': url,
                'is_valid': False,
                'status_code': None,
                'final_url': None,
                'error_message': f'Unexpected error: {str(e)}'
            }
            return name, result
    
    def is_github_url(self, url: str) -> bool:
        """Check if a URL is a GitHub URL."""
        try:
            parsed = urlparse(url)
            return parsed.netloc.lower() in ['github.com', 'www.github.com']
        except Exception:
            return False
    
    def extract_github_repo(self, url: str) -> Optional[str]:
        """Extract repository path from GitHub URL (e.g., 'duckdb/duckdb-excel')."""
        if not self.is_github_url(url):
            return None
        
        try:
            parsed = urlparse(url)
            path_parts = parsed.path.strip('/').split('/')
            if len(path_parts) >= 2:
                return f"{path_parts[0]}/{path_parts[1]}"
        except Exception:
            pass
        
        return None
    
    async def validate_extension_urls(self, extensions_metadata: Dict) -> Dict[str, Dict]:
        """
        Validate URLs for all extensions based on metadata.
        
        Args:
            extensions_metadata: Extension metadata containing URL information
            
        Returns:
            Dict mapping extension names to URL validation results
        """
        urls_to_validate = {}
        
        # Extract URLs from metadata
        for ext_name, metadata in extensions_metadata.items():
            if isinstance(metadata, dict):
                # Check for repository URL
                if 'repository' in metadata:
                    repo_url = f"https://github.com/{metadata['repository']}"
                    urls_to_validate[f"{ext_name}_repo"] = repo_url
                
                # Check for documentation URL
                if 'documentation_url' in metadata:
                    urls_to_validate[f"{ext_name}_docs"] = metadata['documentation_url']
        
        # Validate all URLs
        validation_results = await self.validate_urls_batch(urls_to_validate)
        
        # Organize results by extension
        extension_results = {}
        for key, result in validation_results.items():
            if '_repo' in key:
                ext_name = key.replace('_repo', '')
                if ext_name not in extension_results:
                    extension_results[ext_name] = {}
                extension_results[ext_name]['repository'] = result
            elif '_docs' in key:
                ext_name = key.replace('_docs', '')
                if ext_name not in extension_results:
                    extension_results[ext_name] = {}
                extension_results[ext_name]['documentation'] = result
        
        return extension_results
    
    def get_validation_summary(self, validation_results: Dict[str, Dict]) -> Dict:
        """Generate a summary of validation results."""
        total_urls = 0
        valid_urls = 0
        invalid_urls = 0
        error_types = {}
        
        for ext_name, results in validation_results.items():
            for url_type, result in results.items():
                total_urls += 1
                if result['is_valid']:
                    valid_urls += 1
                else:
                    invalid_urls += 1
                    error_msg = result.get('error_message', 'Unknown error')
                    error_types[error_msg] = error_types.get(error_msg, 0) + 1
        
        return {
            'total_urls': total_urls,
            'valid_urls': valid_urls,
            'invalid_urls': invalid_urls,
            'success_rate': (valid_urls / total_urls * 100) if total_urls > 0 else 0,
            'error_types': error_types
        }