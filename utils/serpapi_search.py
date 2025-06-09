import os
import requests

def search_product_on_google(query):
    serpapi_key = os.getenv("SERPAPI_KEY")
    
    if not serpapi_key:
        print("❌ SERPAPI_KEY environment variable not set")
        return "❌ Hata oluştu: SERPAPI_KEY environment variable not set"

    print("🔑 SERPAPI_KEY bulundu:", serpapi_key[:5] + "..." + serpapi_key[-5:])  # güvenli debug

    params = {
        "engine": "google",
        "q": query,
        "api_key": serpapi_key,
        "num": 5,
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        # Basit örnek dönüş
        if "organic_results" in data and len(data["organic_results"]) > 0:
            return data["organic_results"][0]["link"]
        else:
            return "🔍 Ürün bulunamadı."

    except Exception as e:
        print("🚨 SerpAPI hatası:", e)
        return f"⚠️ API çağrısı başarısız: {e}"
