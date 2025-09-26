"""
URL Validator for DuckDB Extensions Analysis.

Provides utilities to validate GitHub repository URLs and documentation URLs.
"""

import asyncio
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse
import re

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
    
    async def validate_url_with_content(self, url: str, extension_name: str) -> Dict[str, any]:
        """
        Validate a URL and also check if the extension name appears in the page content.
        
        Args:
            url: The URL to validate
            extension_name: The extension name to search for in the page content
            
        Returns:
            Dict with validation results including content validation
        """
        result = {
            'url': url,
            'is_valid': False,
            'status_code': None,
            'final_url': None,
            'error_message': None,
            'content_validation': 'not_checked',
            'extension_name_found': False,
            'content_checked': False
        }
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                # First do a HEAD request to check basic accessibility
                head_response = await client.head(url, follow_redirects=True)
                result['status_code'] = head_response.status_code
                result['final_url'] = str(head_response.url)
                
                if not (200 <= head_response.status_code < 400):
                    result['is_valid'] = False
                    result['error_message'] = f"HTTP {head_response.status_code}"
                    result['content_validation'] = 'broken_url'
                    return result
                
                # If HEAD request is successful, do a GET request to fetch content
                try:
                    get_response = await client.get(url, follow_redirects=True)
                    result['content_checked'] = True
                    
                    if 200 <= get_response.status_code < 400:
                        # Check if extension name appears in the content
                        content = get_response.text.lower()
                        extension_name_lower = extension_name.lower()
                        
                        # Look for the extension name in various forms
                        patterns_to_check = [
                            extension_name_lower,  # exact match
                            f"{extension_name_lower} extension",  # with "extension" suffix
                            f"extension {extension_name_lower}",  # with "extension" prefix
                            f"duckdb-{extension_name_lower}",  # with duckdb- prefix
                            f"\\b{re.escape(extension_name_lower)}\\b"  # word boundary match
                        ]
                        
                        extension_found = False
                        for pattern in patterns_to_check:
                            if pattern.startswith('\\b') and pattern.endswith('\\b'):
                                # Use regex for word boundary patterns
                                if re.search(pattern, content):
                                    extension_found = True
                                    break
                            else:
                                # Simple string search
                                if pattern in content:
                                    extension_found = True
                                    break
                        
                        result['extension_name_found'] = extension_found
                        result['is_valid'] = True
                        
                        if extension_found:
                            result['content_validation'] = 'ok'
                        else:
                            result['content_validation'] = 'likely_wrong'
                            result['error_message'] = f"Extension name '{extension_name}' not found in page content"
                    else:
                        result['is_valid'] = False
                        result['error_message'] = f"GET request failed: HTTP {get_response.status_code}"
                        result['content_validation'] = 'broken_url'
                        
                except Exception as content_error:
                    # HEAD succeeded but GET failed - still consider URL structurally valid
                    result['is_valid'] = True
                    result['content_validation'] = 'content_check_failed'
                    result['error_message'] = f"Content check failed: {str(content_error)}"
                    
        except httpx.TimeoutException:
            result['error_message'] = 'Request timeout'
            result['content_validation'] = 'timeout'
        except httpx.RequestError as e:
            result['error_message'] = f'Request error: {str(e)}'
            result['content_validation'] = 'request_error'
        except Exception as e:
            result['error_message'] = f'Unexpected error: {str(e)}'
            result['content_validation'] = 'unexpected_error'
            
        return result
    
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
    
    async def validate_urls_with_content_batch(self, urls_with_extensions: Dict[str, Tuple[str, str]]) -> Dict[str, Dict]:
        """
        Validate multiple URLs with content checking in batch.
        
        Args:
            urls_with_extensions: Dict mapping names to (url, extension_name) tuples
            
        Returns:
            Dict mapping names to validation results with content validation
        """
        results = {}
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            tasks = []
            for name, (url, extension_name) in urls_with_extensions.items():
                task = self._validate_url_with_content_client(client, name, url, extension_name)
                tasks.append(task)
            
            # Process in batches to avoid overwhelming the server
            batch_size = 5  # Smaller batches for content validation since it's more intensive
            for i in range(0, len(tasks), batch_size):
                batch = tasks[i:i + batch_size]
                batch_results = await asyncio.gather(*batch, return_exceptions=True)
                
                for result in batch_results:
                    if isinstance(result, Exception):
                        logger.warning(f"Content validation batch error: {result}")
                    elif result:
                        name, validation_result = result
                        results[name] = validation_result
                
                # Small delay between batches for content validation
                if i + batch_size < len(tasks):
                    await asyncio.sleep(1)
        
        return results
    
    async def _validate_url_with_content_client(self, client: httpx.AsyncClient, name: str, url: str, extension_name: str) -> Optional[Tuple[str, Dict]]:
        """Validate a URL with content checking using a provided client."""
        result = {
            'url': url,
            'is_valid': False,
            'status_code': None,
            'final_url': None,
            'error_message': None,
            'content_validation': 'not_checked',
            'extension_name_found': False,
            'content_checked': False
        }
        
        try:
            # First do a HEAD request to check basic accessibility
            head_response = await client.head(url, follow_redirects=True)
            result['status_code'] = head_response.status_code
            result['final_url'] = str(head_response.url)
            
            if not (200 <= head_response.status_code < 400):
                result['is_valid'] = False
                result['error_message'] = f"HTTP {head_response.status_code}"
                result['content_validation'] = 'broken_url'
                return name, result
            
            # If HEAD request is successful, do a GET request to fetch content
            try:
                get_response = await client.get(url, follow_redirects=True)
                result['content_checked'] = True
                
                if 200 <= get_response.status_code < 400:
                    # Check if extension name appears in the content
                    content = get_response.text.lower()
                    extension_name_lower = extension_name.lower()
                    
                    # Look for the extension name in various forms
                    patterns_to_check = [
                        extension_name_lower,  # exact match
                        f"{extension_name_lower} extension",  # with "extension" suffix
                        f"extension {extension_name_lower}",  # with "extension" prefix
                        f"duckdb-{extension_name_lower}",  # with duckdb- prefix
                        f"\\b{re.escape(extension_name_lower)}\\b"  # word boundary match
                    ]
                    
                    extension_found = False
                    for pattern in patterns_to_check:
                        if pattern.startswith('\\b') and pattern.endswith('\\b'):
                            # Use regex for word boundary patterns
                            if re.search(pattern, content):
                                extension_found = True
                                break
                        else:
                            # Simple string search
                            if pattern in content:
                                extension_found = True
                                break
                    
                    result['extension_name_found'] = extension_found
                    result['is_valid'] = True
                    
                    if extension_found:
                        result['content_validation'] = 'ok'
                    else:
                        result['content_validation'] = 'likely_wrong'
                        result['error_message'] = f"Extension name '{extension_name}' not found in page content"
                else:
                    result['is_valid'] = False
                    result['error_message'] = f"GET request failed: HTTP {get_response.status_code}"
                    result['content_validation'] = 'broken_url'
                    
            except Exception as content_error:
                # HEAD succeeded but GET failed - still consider URL structurally valid
                result['is_valid'] = True
                result['content_validation'] = 'content_check_failed'
                result['error_message'] = f"Content check failed: {str(content_error)}"
                
        except httpx.TimeoutException:
            result['error_message'] = 'Request timeout'
            result['content_validation'] = 'timeout'
        except httpx.RequestError as e:
            result['error_message'] = f'Request error: {str(e)}'
            result['content_validation'] = 'request_error'
        except Exception as e:
            logger.warning(f"Error validating {name} ({url}): {e}")
            result['error_message'] = f'Unexpected error: {str(e)}'
            result['content_validation'] = 'unexpected_error'
            
        return name, result
    
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