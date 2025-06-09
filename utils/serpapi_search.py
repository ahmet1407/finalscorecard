from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

def query_serpapi(product_input: str):
    is_url = product_input.startswith("http")

    search_params = {
        "engine": "google",
        "q": product_input,
        "google_domain": "google.com",
        "gl": "tr",
        "hl": "tr",
        "api_key": SERPAPI_KEY,
        "device": "desktop"
    }

    if not is_url:
        search_params["tbm"] = "shop"

    search = GoogleSearch(search_params)
    results = search.get_dict()

    return results
