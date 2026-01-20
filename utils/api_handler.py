import requests

def fetch_all_products():
    try:
        response = requests.get("https://dummyjson.com/products?limit=100")
        data = response.json()
        print("Fetched products from API")
        return data.get('products', [])
    except Exception as e:
        print("API error:", e)
        return []


def create_product_mapping(products):
    mapping = {}
    for p in products:
        mapping[p['id']] = {
            'category': p.get('category'),
            'brand': p.get('brand'),
            'rating': p.get('rating')
        }
    return mapping
