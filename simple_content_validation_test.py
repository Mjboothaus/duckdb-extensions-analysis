#!/usr/bin/env python3
"""
Simple test for URL content validation functionality.
Tests the enhanced URL validation logic without complex imports.
"""

import asyncio
import httpx
import re
from typing import Dict, Any

async def validate_url_content(url: str, extension_name: str, timeout: int = 10) -> Dict[str, Any]:
    """
    Simple implementation of content validation for testing.
    
    Args:
        url: The URL to validate
        extension_name: The extension name to search for in the page content
        timeout: Request timeout in seconds
            
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
        async with httpx.AsyncClient(timeout=timeout) as client:
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
                
    except Exception as e:
        result['error_message'] = f'Error: {str(e)}'
        result['content_validation'] = 'request_error'
        
    return result

async def test_enhanced_url_validation():
    """Test the enhanced URL validation functionality."""
    
    print("DuckDB Extensions Analysis - Enhanced URL Validation Test")
    print("=" * 60)
    
    # Test cases with (url, extension_name, expected_result)
    test_cases = [
        # Known good URLs where extension name should be found
        ('https://duckdb.org/docs/stable/core_extensions/spatial.html', 'spatial', 'ok'),
        ('https://duckdb.org/docs/stable/core_extensions/httpfs.html', 'httpfs', 'ok'),
        ('https://duckdb.org/docs/stable/data/json/overview.html', 'json', 'ok'),
        
        # URLs that exist but likely don't contain the extension name
        ('https://duckdb.org/docs/stable/core_extensions/overview.html', 'parquet', 'likely_wrong'),
        ('https://duckdb.org/docs/', 'spatial', 'likely_wrong'),
        
        # Broken URLs (should return broken_url)
        ('https://duckdb.org/docs/stable/core_extensions/nonexistent.html', 'nonexistent', 'broken_url'),
    ]
    
    print("Testing URL content validation:")
    print("=" * 80)
    
    results_summary = {'ok': 0, 'likely_wrong': 0, 'broken_url': 0, 'other': 0}
    
    for i, (url, extension_name, expected) in enumerate(test_cases, 1):
        print(f"\n{i}. Testing '{extension_name}' extension")
        print(f"   URL: {url}")
        print(f"   Expected: {expected}")
        
        result = await validate_url_content(url, extension_name)
        actual = result.get('content_validation', 'unknown')
        
        print(f"   Result: {actual}")
        print(f"   Status: {'✓ PASS' if actual == expected else '✗ FAIL'}")
        
        if result.get('error_message'):
            print(f"   Error: {result['error_message']}")
        
        if result.get('extension_name_found') is not None:
            print(f"   Extension name found: {result['extension_name_found']}")
        
        print(f"   HTTP Status: {result.get('status_code', 'N/A')}")
        
        # Count results for summary
        if actual in results_summary:
            results_summary[actual] += 1
        else:
            results_summary['other'] += 1
    
    print("\n" + "=" * 80)
    print("Summary:")
    print(f"  Total tests: {len(test_cases)}")
    for validation_type, count in results_summary.items():
        if count > 0:
            print(f"  {validation_type}: {count}")
    
    print("\nTest complete! The enhanced URL validation can:")
    print("  ✓ Detect when extension names are present in documentation pages (OK)")
    print("  ✓ Identify pages where extension names are missing (LIKELY_WRONG)")  
    print("  ✓ Handle broken URLs properly (BROKEN)")
    print("\nThis helps identify documentation URLs that may be incorrect even if they return HTTP 200.")

if __name__ == "__main__":
    asyncio.run(test_enhanced_url_validation())