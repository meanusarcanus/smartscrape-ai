"""
SmartScrape AI Apify Actor
Wrapper calling Micro-SaaS AI Agent Suite API (POST /scrape-and-extract)
"""

import os
import requests
from apify import Actor

async def main():
    async with Actor:
        # Fetch Apify input
        actor_input = await Actor.get_input() or {}
        url = actor_input.get("url", "https://example.com/product/123")
        extraction_targets = actor_input.get("extraction_targets", ["title", "price", "description"])

        Actor.log.info(f"Extracting URL: {url} with targets: {extraction_targets}")

        # Call live Vercel API
        api_url = "https://microsaas-agent-api.vercel.app/scrape-and-extract"
        payload = {
            "url": url,
            "extraction_targets": extraction_targets
        }

        response = requests.post(api_url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Push result to Apify dataset storage
        await Actor.push_data(data.get("extracted_data", {}))
        Actor.log.info("Successfully pushed extracted data to Apify dataset!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
