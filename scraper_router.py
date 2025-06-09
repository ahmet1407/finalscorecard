from scraper_manager import get_scraper_for_url

def scrape_link(input_text):
    return get_scraper_for_url(input_text)(input_text)