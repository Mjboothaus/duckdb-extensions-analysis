#!/usr/bin/env python3

import asyncio
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from analyzers.url_validator import URLValidator

async def test_urls():
    """Test the fixed URL validation on known broken and working URLs."""
    
    validator = URLValidator()
    
    # Test URLs - including some known broken ones from the independent test
    test_urls = {
        'working_github': 'https://github.com/duckdb/duckdb',
        'working_duckdb_docs': 'https://duckdb.org/docs/stable/core_extensions/tpch.html',
        'broken_extension_path': 'https://github.com/duckdb/duckdb/extensions/parquet',
        'broken_docs_path': 'https://duckdb.org/docs/core_extensions/overview.html',
        'another_broken': 'https://github.com/duckdb/duckdb/extensions/sqlite',
        'working_community': 'https://duckdb.org/docs/extensions/community_extensions.html',
    }
    
    print("Testing URL validation with fixed logic...")
    print("=" * 50)
    
    results = await validator.validate_urls_batch(test_urls)
    
    for name, result in results.items():
        status = "✓ VALID" if result['is_valid'] else "✗ BROKEN"
        status_code = result['status_code'] if result['status_code'] else 'N/A'
        error_msg = result['error_message'] if result['error_message'] else 'None'
        
        print(f"{status:<8} | {name:<20} | Status: {status_code} | Error: {error_msg}")
        print(f"         | URL: {result['url']}")
        print()

if __name__ == "__main__":
    asyncio.run(test_urls())