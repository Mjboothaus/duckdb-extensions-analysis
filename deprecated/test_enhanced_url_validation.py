#!/usr/bin/env python3
"""
Test script for enhanced URL validation with content checking.

This script tests the new URL validation functionality that checks if extension 
names appear in the content of documentation pages, not just HTTP status codes.
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path to ensure proper imports
parent_path = Path(__file__).parent
sys.path.insert(0, str(parent_path))
sys.path.insert(0, str(parent_path / 'src'))

# Direct import to avoid relative import issues
from src.analyzers.url_validator import URLValidator
from loguru import logger

async def test_content_validation():
    """Test the enhanced URL validation with content checking."""
    
    logger.info("Testing enhanced URL validation with content checking...")
    
    validator = URLValidator()
    
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
        ('https://duckdb.org/docs/stable/core_extensions/badext.html', 'badext', 'broken_url'),
    ]
    
    print("Testing individual URL content validation:")
    print("=" * 80)
    
    for url, extension_name, expected in test_cases:
        print(f"\nTesting: {extension_name} at {url}")
        print(f"Expected: {expected}")
        
        result = await validator.validate_url_with_content(url, extension_name)
        actual = result.get('content_validation', 'unknown')
        
        print(f"Actual:   {actual}")
        print(f"Status:   {'✓ PASS' if actual == expected else '✗ FAIL'}")
        
        if result.get('error_message'):
            print(f"Error:    {result['error_message']}")
        
        if result.get('extension_name_found') is not None:
            print(f"Name found: {result['extension_name_found']}")
    
    print("\n" + "=" * 80)
    print("Testing batch content validation:")
    
    # Test batch validation
    batch_urls = {
        'spatial_good': ('https://duckdb.org/docs/stable/core_extensions/spatial.html', 'spatial'),
        'json_good': ('https://duckdb.org/docs/stable/data/json/overview.html', 'json'),
        'wrong_page': ('https://duckdb.org/docs/stable/core_extensions/overview.html', 'parquet'),
        'broken_url': ('https://duckdb.org/docs/stable/core_extensions/nonexistent.html', 'nonexistent')
    }
    
    batch_results = await validator.validate_urls_with_content_batch(batch_urls)
    
    for name, result in batch_results.items():
        url = result['url']
        content_validation = result.get('content_validation', 'unknown')
        extension_found = result.get('extension_name_found', False)
        
        print(f"\n{name}:")
        print(f"  URL: {url}")
        print(f"  Content validation: {content_validation}")
        print(f"  Extension name found: {extension_found}")
        print(f"  HTTP status: {result.get('status_code', 'N/A')}")
        
        if result.get('error_message'):
            print(f"  Error: {result['error_message']}")
    
    print("\n" + "=" * 80)
    print("Summary:")
    
    # Count results by type
    summary_counts = {}
    for result in batch_results.values():
        content_validation = result.get('content_validation', 'unknown')
        summary_counts[content_validation] = summary_counts.get(content_validation, 0) + 1
    
    for validation_type, count in summary_counts.items():
        print(f"  {validation_type}: {count}")
    
    print("\nTest complete!")

async def main():
    """Main test function."""
    print("DuckDB Extensions Analysis - Enhanced URL Validation Test")
    print("=" * 60)
    
    await test_content_validation()

if __name__ == "__main__":
    asyncio.run(main())