import requests

BASE_URL = "http://127.0.0.1:8000/products"

def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product added successfully.")
    else:
        print(f"Failed to add product: {response.json()}")

def get_all_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:")
        for product in response.json():
            print(product)
    else:
        print(f"Failed to fetch products: {response.json()}")

if __name__ == "__main__":
    add_product("Laptop", "High-end gaming laptop", 1500.99)
    add_product("Smartphone", "Latest model smartphone", 999.99)
    get_all_products()
