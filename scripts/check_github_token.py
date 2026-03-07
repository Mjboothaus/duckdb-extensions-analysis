#!/usr/bin/env python3
"""
Check GitHub Token Status and API Rate Limits

This script verifies that the GitHub token is properly configured and working.
"""

import sys
import httpx
from pathlib import Path

# Add conf directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "conf"))
from config import Config


def main():
    print("🔑 GitHub Token Status Check")
    print()

    config = Config()
    has_token, msg = config.get_github_token_info()

    # Token status
    print("Token Status:")
    print(f"  Found: {has_token}")
    if has_token:
        print("  Source: .env file or gh CLI")
        auth_header = config.headers.get("Authorization", "")
        print(f"  Prefix: {auth_header[:15]}...")
    else:
        print("  Source: None")
        print("  Note: Run 'just setup-auth' or 'gh auth login' to configure")

    print()

    # Check API rate limits
    print("GitHub API Rate Limits:")
    try:
        response = httpx.get(
            "https://api.github.com/rate_limit", headers=config.headers, timeout=5
        )
        data = response.json()
        core = data["resources"]["core"]

        print(f"  Limit: {core['limit']} requests/hour")
        print(f"  Remaining: {core['remaining']}")
        print(f"  Used: {core['limit'] - core['remaining']}")
        print()

        if core["limit"] == 5000:
            print("✅ Token is WORKING - authenticated rate limit (5000/hr)")
            return 0
        elif core["limit"] == 60:
            print("❌ Token NOT working - unauthenticated rate limit (60/hr)")
            print()
            print("To fix this:")
            print("  1. Run: gh auth login")
            print("  2. Or run: just setup-auth")
            print("  3. Or set GITHUB_TOKEN environment variable")
            return 1
        else:
            print(f"⚠️  Unexpected rate limit: {core['limit']}/hr")
            return 2

    except Exception as e:
        print(f"  ❌ Error checking rate limits: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
