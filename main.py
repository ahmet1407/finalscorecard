from flask import Flask, request, jsonify
from utils.serpapi_scraper import serpapi_search
from services.parser import parse_serpapi_data

app = Flask(__name__)

@app.route("/api/parse", methods=["POST"])
def parse_product():
    data = request.json
    product_url = data.get("url")
    if not product_url:
        return jsonify({"error": "No URL provided"}), 400

    raw_data = serpapi_search(product_url)
    if not raw_data:
        return jsonify({"error": "Failed to fetch data from SerpAPI"}), 500

    parsed = parse_serpapi_data(raw_data)
    if not parsed:
        return jsonify({"error": "Could not parse product data"}), 500

    return jsonify(parsed)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
