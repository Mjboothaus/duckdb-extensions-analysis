from datetime import datetime
import httpx
import requests
from bs4 import BeautifulSoup
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import sys
import yaml
import os

logger.remove()
logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

GITHUB_API_BASE = "https://api.github.com"
COMMUNITY_REPO = "duckdb/community-extensions"
DUCKDB_REPO = "duckdb/duckdb"

# Add GitHub token if available for higher rate limits
HEADERS = {"Accept": "application/vnd.github.v3+json"}
if github_token := os.getenv("GITHUB_TOKEN"):
    HEADERS["Authorization"] = f"token {github_token}"

# DuckDB release info (v1.4.0 as current)
DUCKDB_VERSION = "v1.4.0"
DUCKDB_RELEASE_DATE = datetime(2025, 9, 16)  # From official announcement
CURRENT_DATE = datetime.now()
DUCKDB_LAG_DAYS = (CURRENT_DATE - DUCKDB_RELEASE_DATE).days

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((httpx.RequestError,)),
    before=lambda _: logger.debug("Retrying request..."),
)
async def fetch_github_api(client, url):
    logger.debug(f"Fetching {url}")
    response = await client.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((requests.RequestException,)),
    before=lambda _: logger.debug("Retrying request..."),
)
def fetch_duckdb_docs(url):
    logger.debug(f"Fetching {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def get_core_extensions():
    url = "https://duckdb.org/docs/stable/core_extensions/overview.html"
    html = fetch_duckdb_docs(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    # Parse the table for extensions and stages
    table = soup.find('table')
    if not table:
        logger.warning("Could not find core extensions table")
        return []
    
    rows = table.find_all('tr')[1:]  # Skip header
    extensions = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 2:
            name = cols[0].get_text(strip=True)
            stage = cols[1].get_text(strip=True)
            extensions.append({"name": name, "stage": stage})
    
    logger.info(f"Found {len(extensions)} core extensions from DuckDB {DUCKDB_VERSION}")
    return extensions

def check_core_status():
    extensions = get_core_extensions()
    for ext in extensions:
        status = "Ongoing"  # All core are ongoing unless deprecated (none currently)
        last_push = DUCKDB_RELEASE_DATE
        lag_days = DUCKDB_LAG_DAYS
        logger.info(f"{ext['name']} (Core, Stage: {ext['stage']}): {status} | Last updated: {last_push} ({lag_days} days ago in {DUCKDB_VERSION})")

async def get_community_extensions(client):
    contents_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions"
    contents = await fetch_github_api(client, contents_url)
    extensions = [item["name"] for item in contents if item["type"] == "dir"]
    logger.info(f"Found {len(extensions)} community extensions: {', '.join(extensions)}")
    return extensions

async def get_extension_metadata(client, ext_name):
    metadata_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions/{ext_name}/description.yml"
    try:
        metadata_raw = await fetch_github_api(client, metadata_url)
        import base64
        metadata_content = base64.b64decode(metadata_raw["content"]).decode("utf-8")
        metadata = yaml.safe_load(metadata_content)
        return metadata
    except httpx.HTTPStatusError as e:
        logger.warning(f"Description not found for {ext_name}: {e}")
        return None

async def check_community_status(client):
    extensions = await get_community_extensions(client)
    for ext in extensions:
        logger.info(f"Processing {ext}")
        metadata = await get_extension_metadata(client, ext)
        if not metadata or "repo" not in metadata or "github" not in metadata["repo"]:
            logger.warning(f"No repository found for {ext}. Skipping.")
            continue
        repo = metadata["repo"]["github"]
        repo_url = f"{GITHUB_API_BASE}/repos/{repo}"
        try:
            repo_data = await fetch_github_api(client, repo_url)
            archived = repo_data.get("archived", False)
            last_push = repo_data.get("pushed_at")
            last_push_date = datetime.fromisoformat(last_push.rstrip("Z")) if last_push else None
            lag_days = (CURRENT_DATE - last_push_date).days if last_push_date else "Unknown"
            status = "Discontinued" if archived else "Ongoing"
            logger.info(f"{ext} (Repo: {repo}): {status} | Last push: {last_push_date} ({lag_days} days ago)")
        except Exception as e:
            logger.error(f"Failed to check status for {ext}: {e}")

async def main():
    # Check core extensions (sync, as it uses requests)
    logger.info("Starting core extensions status analysis")
    check_core_status()
    
    # Check community extensions (async)
    async with httpx.AsyncClient() as client:
        logger.info("Starting community extensions status analysis")
        await check_community_status(client)

if __name__ == "__main__":
    import asyncio
    logger.info("Starting full DuckDB extensions status analysis")
    asyncio.run(main())
    logger.info("Analysis complete")