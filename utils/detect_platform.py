def detect_platform(url):
    if "amazon" in url:
        return "amazon"
    elif "hepsiburada" in url:
        return "hepsiburada"
    elif "trendyol" in url:
        return "trendyol"
    return "unknown"
