from utils.scrape_amazon import scrape_amazon_product
from utils.scrape_hepsiburada import scrape_hepsiburada_product
from utils.scrape_trendyol import scrape_trendyol_product
from utils.detect_platform import detect_platform

def get_scraper_for_url(input_text):
    platform = detect_platform(input_text)
    if platform == "amazon":
        return scrape_amazon_product
    elif platform == "hepsiburada":
        return scrape_hepsiburada_product
    elif platform == "trendyol":
        return scrape_trendyol_product
    else:
        raise Exception("Desteklenmeyen platform")