# utils/serpapi_search.py

import os
import requests

def search_product_on_google(url: str):
    serpapi_key = os.getenv("SERPAPI_KEY")
    if not serpapi_key:
        raise ValueError("SERPAPI_KEY environment variable not set")

    params = {
        "engine": "google",
        "q": url,
        "api_key": serpapi_key,
        "num": "10",
        "device": "desktop"
    }

    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code != 200:
        raise RuntimeError(f"SerpAPI failed: {response.text}")

    return response.json()
