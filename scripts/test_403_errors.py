#!/usr/bin/env python3
"""Test script to see detailed GitHub 403 error messages."""

import asyncio
import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent.parent / "conf"))
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from config import Config
from analyzers.github_api import GitHubAPIClient
import httpx


async def test_repos():
    config = Config()
    print(f"Token found: {config.has_github_token}")
    print()
    
    client_api = GitHubAPIClient(config, cache_hours=0)
    
    # Test repos that have been giving 403s
    test_repos = [
        "query-farm/a5",
        "duckdb/duckdb", 
        "duckdb/community-extensions"
    ]
    
    async with httpx.AsyncClient() as client:
        for repo in test_repos:
            print(f"\n{'='*60}")
            print(f"Testing: {repo}")
            print('='*60)
            
            result = await client_api.get_repository_info(client, repo)
            
            if result:
                print(f"✓ Success: Got {result.get('full_name', 'data')}")
            else:
                print(f"✗ Failed: No data returned")


if __name__ == "__main__":
    asyncio.run(test_repos())
