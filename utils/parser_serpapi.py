def parse_serpapi_response(data):
    result = {
        "name": None,
        "price": None,
        "rating": None,
        "review_count": None,
        "link": None,
        "image": None
    }

    # Öncelikle ürün adı ve resim inline_images'tan alınabilir
    if "inline_images" in data and len(data["inline_images"]) > 0:
        result["name"] = data["inline_images"][0].get("title")
        result["image"] = data["inline_images"][0].get("original")

    # Sonra organic_results'tan daha detaylı veriler alınabilir
    organic = data.get("shopping_results", []) or data.get("organic_results", [])

    if len(organic) > 0:
        first = organic[0]
        result["name"] = first.get("title", result["name"])
        result["link"] = first.get("link")
        result["price"] = (
            first.get("price")
            or first.get("extracted_price")
            or (first.get("rich_snippet", {}).get("top", {}).get("detected_extensions", {}).get("price"))
        )
        result["rating"] = (
            first.get("rating")
            or first.get("rich_snippet", {}).get("top", {}).get("detected_extensions", {}).get("rating")
        )
        result["review_count"] = (
            first.get("reviews")
            or first.get("rich_snippet", {}).get("top", {}).get("detected_extensions", {}).get("reviews")
        )

    return result
