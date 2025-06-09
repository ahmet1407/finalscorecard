def parse_serpapi_data(data):
    try:
        organic_results = data.get("organic_results", [])
        for result in organic_results:
            if "title" in result and "link" in result:
                title = result.get("title")
                link = result.get("link")
                snippet = result.get("snippet", "")
                rating = result.get("rich_snippet", {}).get("top", {}).get("detected_extensions", {}).get("rating", None)
                reviews = result.get("rich_snippet", {}).get("top", {}).get("detected_extensions", {}).get("reviews", None)

                return {
                    "title": title,
                    "link": link,
                    "description": snippet,
                    "rating": rating,
                    "reviews": reviews,
                }
    except Exception:
        return None

    return None
