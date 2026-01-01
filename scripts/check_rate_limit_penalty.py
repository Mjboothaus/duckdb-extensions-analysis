#!/usr/bin/env python3
"""
Check for GitHub Secondary Rate Limit Penalties

This script tests if you're currently under a secondary rate limit penalty
by making a test API request and analyzing the response.
"""

import sys
import httpx
import time
from pathlib import Path
from datetime import datetime

# Add conf directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "conf"))
from config import Config


def check_for_penalty():
    print("🔍 Checking for GitHub Secondary Rate Limit Penalties")
    print()
    
    config = Config()
    
    # First check primary rate limits
    print("Step 1: Checking primary rate limits...")
    try:
        response = httpx.get(
            "https://api.github.com/rate_limit",
            headers=config.headers,
            timeout=10
        )
        data = response.json()
        core = data["resources"]["core"]
        
        print(f"  Primary limit: {core['limit']}/hour")
        print(f"  Remaining: {core['remaining']}")
        print(f"  Resets at: {datetime.fromtimestamp(core['reset']).strftime('%Y-%m-%d %H:%M:%S')}")
        
        if core['remaining'] < 100:
            print("\n⚠️  WARNING: Low on primary rate limit!")
            print(f"  You have {core['remaining']} requests left.")
            return
            
        print("  ✅ Primary rate limit OK\n")
        
    except Exception as e:
        print(f"  ❌ Error checking rate limits: {e}\n")
        return
    
    # Test with actual API calls to detect secondary limits
    print("Step 2: Testing for secondary rate limit penalties...")
    print("  Making 3 test API requests to common repos...")
    
    test_repos = [
        "duckdb/duckdb",
        "duckdb/community-extensions", 
        "query-farm/a5"
    ]
    
    penalties_detected = 0
    success_count = 0
    
    for i, repo in enumerate(test_repos, 1):
        try:
            start_time = time.time()
            response = httpx.get(
                f"https://api.github.com/repos/{repo}",
                headers=config.headers,
                timeout=10
            )
            elapsed = time.time() - start_time
            
            if response.status_code == 200:
                print(f"  {i}. ✅ {repo} - OK ({elapsed:.2f}s)")
                success_count += 1
            elif response.status_code == 403:
                print(f"  {i}. ❌ {repo} - HTTP 403 (PENALTY DETECTED)")
                penalties_detected += 1
                
                # Check response headers for clues
                retry_after = response.headers.get('Retry-After')
                if retry_after:
                    print(f"      Retry-After header: {retry_after}s")
                    
                # Check for abuse detection message
                try:
                    error_data = response.json()
                    if 'message' in error_data:
                        print(f"      Message: {error_data['message'][:100]}")
                except:
                    pass
                    
            elif response.status_code == 429:
                print(f"  {i}. ⚠️ {repo} - HTTP 429 (Rate Limited)")
                penalties_detected += 1
            else:
                print(f"  {i}. ⚠️ {repo} - HTTP {response.status_code}")
                
            # Small delay between requests
            if i < len(test_repos):
                time.sleep(1)
                
        except Exception as e:
            print(f"  {i}. ❌ {repo} - Error: {e}")
    
    print()
    print("=" * 60)
    print("DIAGNOSIS:")
    print("=" * 60)
    
    if penalties_detected == 0:
        print("✅ NO PENALTIES DETECTED")
        print("\nYou can proceed with analysis safely.")
        print("Recommended: Use default cache (12 hours)")
        print("  Command: just workflow")
        return 0
        
    elif penalties_detected >= 2:
        print("❌ SECONDARY RATE LIMIT PENALTY ACTIVE")
        print("\nYou are currently flagged by GitHub's abuse detection.")
        print("\nWhy this happens:")
        print("  - Too many rapid sequential requests")
        print("  - Pattern detected as 'scraping' behavior")
        print("  - Using --cache-hours 0 triggers this")
        print("\nHow to fix:")
        print("  1. ⏰ Wait 30-60 minutes for penalty to expire")
        print("  2. ✅ Use cached data: just workflow")
        print("  3. ❌ DO NOT use --cache-hours 0")
        print("  4. 💡 For fresh data: just cache-clear && just workflow")
        print("\nCurrent time:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return 1
        
    else:
        print("⚠️  POSSIBLE PENALTY (mixed results)")
        print("\nSome requests succeeded, others failed.")
        print("You may be on the edge of a penalty.")
        print("\nRecommendation:")
        print("  - Wait 15-30 minutes before running analysis")
        print("  - Use default cache when you resume")
        return 2


if __name__ == "__main__":
    sys.exit(check_for_penalty())
