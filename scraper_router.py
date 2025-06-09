from utils.detect_platform import detect_platform
from utils.scrape_amazon import scrape_amazon_product
from utils.scrape_hepsiburada import scrape_hepsiburada_product
from utils.scrape_trendyol import scrape_trendyol_product
from utils.serpapi_search import search_product_on_google

def scrape_link(link_or_query):
    platform = detect_platform(link_or_query)

    if platform == "amazon":
        return scrape_amazon_product(link_or_query)
    elif platform == "hepsiburada":
        return scrape_hepsiburada_product(link_or_query)
    elif platform == "trendyol":
        return scrape_trendyol_product(link_or_query)
    else:
        print("🔄 SerpAPI ile sorgulanıyor...")
        return search_product_on_google(link_or_query)
