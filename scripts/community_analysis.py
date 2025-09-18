from datetime import datetime
import httpx
from loguru import logger
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
import sys
import yaml
import os

logger.remove()
logger.add(
    sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO"
)

GITHUB_API_BASE = "https://api.github.com"
COMMUNITY_REPO = "duckdb/community-extensions"

# Add GitHub token if available for higher rate limits
HEADERS = {"Accept": "application/vnd.github.v3+json"}
if github_token := os.getenv("GITHUB_TOKEN"):
    HEADERS["Authorization"] = f"token {github_token}"


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


async def get_community_extensions(client):
    contents_url = f"{GITHUB_API_BASE}/repos/{COMMUNITY_REPO}/contents/extensions"
    contents = await fetch_github_api(client, contents_url)
    extensions = [item["name"] for item in contents if item["type"] == "dir"]
    logger.info(
        f"Found {len(extensions)} community extensions: {', '.join(extensions)}"
    )
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


async def check_extension_status(client):
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
            last_push_date = (
                datetime.fromisoformat(last_push.rstrip("Z")) if last_push else None
            )
            lag_days = (
                (datetime.now() - last_push_date).days if last_push_date else "Unknown"
            )
            logger.info(
                f"{ext} (Repo: {repo}): {'Discontinued' if archived else 'Ongoing'} | Last push: {last_push_date} ({lag_days} days ago)"
            )
        except Exception as e:
            logger.error(f"Failed to check status for {ext}: {e}")


async def main():
    async with httpx.AsyncClient() as client:
        await check_extension_status(client)


if __name__ == "__main__":
    import asyncio

    logger.info("Starting community extensions status analysis")
    asyncio.run(main())
    logger.info("Analysis complete")
