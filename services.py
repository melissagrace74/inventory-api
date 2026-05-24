import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def fetch_product(barcode):
    try:
        url = f"{BASE_URL}/{barcode}.json"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") == 1:
            return data["product"]

        return None

    except Exception as e:
        print("API error:", e)
        return None