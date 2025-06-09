
import os
import requests

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_product_on_google(query):
    params = {
        "engine": "google",  # Amazon değil, Google seçildi
        "q": query,
        "api_key": SERP_API_KEY
    }
    response = requests.get("https://serpapi.com/search", params=params, timeout=150)
    response.raise_for_status()
    data = response.json()
    return data


def extract_first_product_info(data):
    try:
        shopping_results = data.get("shopping_results", [])
        if not shopping_results:
            return None
        first = shopping_results[0]
        return {
            "title": first.get("title"),
            "link": first.get("link"),
            "price": first.get("price"),
            "source": first.get("source")
        }
    except Exception as e:
        return {"error": str(e)}
