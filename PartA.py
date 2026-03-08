from collections import defaultdict

catalog = {
    'SKU001': {'name': 'Laptop', 'price': 65000, 'category': 'electronics',
               'stock': 15, 'rating': 4.5, 'tags': ['computer', 'work']},

    'SKU002': {'name': 'Smartphone', 'price': 30000, 'category': 'electronics',
               'stock': 25, 'rating': 4.3, 'tags': ['mobile', 'android']},

    'SKU003': {'name': 'Headphones', 'price': 2500, 'category': 'electronics',
               'stock': 0, 'rating': 4.0, 'tags': ['music', 'audio']},

    'SKU004': {'name': 'Smartwatch', 'price': 8000, 'category': 'electronics',
               'stock': 12, 'rating': 4.1, 'tags': ['fitness', 'wearable']},

    'SKU005': {'name': 'Tablet', 'price': 20000, 'category': 'electronics',
               'stock': 10, 'rating': 4.2, 'tags': ['computer', 'portable']},

    'SKU006': {'name': 'T-Shirt', 'price': 800, 'category': 'clothing',
               'stock': 50, 'rating': 3.9, 'tags': ['casual', 'cotton']},

    'SKU007': {'name': 'Jeans', 'price': 2000, 'category': 'clothing',
               'stock': 30, 'rating': 4.0, 'tags': ['denim', 'casual']},

    'SKU008': {'name': 'Jacket', 'price': 3500, 'category': 'clothing',
               'stock': 8, 'rating': 4.2, 'tags': ['winter', 'fashion']},

    'SKU009': {'name': 'Sneakers', 'price': 4000, 'category': 'clothing',
               'stock': 0, 'rating': 4.1, 'tags': ['shoes', 'sports']},

    'SKU010': {'name': 'Python Programming', 'price': 900, 'category': 'books',
               'stock': 20, 'rating': 4.7, 'tags': ['education', 'coding']},

    'SKU011': {'name': 'Data Science Handbook', 'price': 1200, 'category': 'books',
               'stock': 18, 'rating': 4.6, 'tags': ['education', 'data']},

    'SKU012': {'name': 'Fantasy Novel', 'price': 500, 'category': 'books',
               'stock': 0, 'rating': 4.2, 'tags': ['story', 'fiction']},

    'SKU013': {'name': 'Organic Honey', 'price': 350, 'category': 'food',
               'stock': 40, 'rating': 4.4, 'tags': ['healthy', 'sweet']},

    'SKU014': {'name': 'Green Tea', 'price': 250, 'category': 'food',
               'stock': 35, 'rating': 4.3, 'tags': ['healthy', 'drink']},

    'SKU015': {'name': 'Dark Chocolate', 'price': 200, 'category': 'food',
               'stock': 60, 'rating': 4.5, 'tags': ['sweet', 'snack']}
}

def search_by_tag(tag):
    tag_map = defaultdict(list)

    for sku, product in catalog.items():
        for t in product.get('tags', []):
            tag_map[t].append(product.get('name'))

    return tag_map.get(tag, [])

def out_of_stock():
    return {
        sku: product
        for sku, product in catalog.items()
        if product.get('stock', 0) == 0
    }
    
def price_range(min_price, max_price):
    return {
        sku: product
        for sku, product in catalog.items()
        if min_price <= product.get('price', 0) <= max_price
    }
    
def category_summary():
    data = defaultdict(list)

    for product in catalog.values():
        category = product.get('category')
        data[category].append(product)

    summary = {}

    for cat, items in data.items():
        count = len(items)
        avg_price = sum(p.get('price', 0) for p in items) / count
        avg_rating = sum(p.get('rating', 0) for p in items) / count

        summary[cat] = {
            "count": count,
            "avg_price": round(avg_price, 2),
            "avg_rating": round(avg_rating, 2)
        }

    return summary

def apply_discount(category, percent):
    discount_factor = 1 - percent / 100

    return {
        sku: {
            **product,
            "price": round(product.get('price', 0) * discount_factor, 2)
        }
        if product.get('category') == category else product
        for sku, product in catalog.items()
    }
    
def merge_catalogs(catalog1, catalog2):
    merged = catalog1 | catalog2
    return merged



print(search_by_tag("sweet"))
print(out_of_stock())
print(price_range(1000, 5000))
print(category_summary())

new_catalog = {
    'SKU016': {'name': 'Bluetooth Speaker', 'price': 3500,
               'category': 'electronics', 'stock': 15,
               'rating': 4.3, 'tags': ['music', 'audio']}
}

merged = merge_catalogs(catalog, new_catalog)