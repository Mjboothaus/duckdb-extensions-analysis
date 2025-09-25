#!/usr/bin/env python3
"""Simple test to verify URL validation fix is working."""
import asyncio
import httpx

async def test_urls():
    """Test URLs directly with httpx to verify our logic."""
    test_urls = [
        'https://github.com/duckdb/duckdb/extensions/parquet',  # Should be 404
        'https://duckdb.org/docs/core_extensions/overview.html',  # Should be 404
        'https://github.com/duckdb/duckdb',  # Should be 200
        'https://duckdb.org/docs/stable/core_extensions/tpch.html',  # Should be 200
    ]
    
    async with httpx.AsyncClient(timeout=10) as client:
        for url in test_urls:
            try:
                response = await client.head(url, follow_redirects=True)
                is_valid = 200 <= response.status_code < 400
                status = "✓ VALID" if is_valid else "✗ BROKEN"
                print(f"{status:<8} | Status: {response.status_code} | URL: {url}")
            except Exception as e:
                print(f"✗ ERROR   | Error: {e} | URL: {url}")

if __name__ == "__main__":
    asyncio.run(test_urls())