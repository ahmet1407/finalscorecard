import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/113.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=150)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("span", {"id": "productTitle"})
        price_tag = soup.find("span", {"class": "a-price-whole"})

        title = title_tag.get_text(strip=True) if title_tag else "Amazon Ürünü"
        price = price_tag.get_text(strip=True).replace(".", "") + " TL" if price_tag else "999 TL"

        return {
            "name": title,
            "price": price,
            "satisfaction": 88,
            "flaw": 12,
            "aura": 85,
            "expert": 90,
        }

    except Exception as e:
        raise ValueError(f"Amazon sayfasına ulaşılamadı: {str(e)}")
