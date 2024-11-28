from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "products.json"

# Helper functions
def load_products():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_products(products):
    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)

# Product schema
class Product(BaseModel):
    name: str
    description: str
    price: float

# POST /products - Create a new product
@app.post("/products", status_code=201)
def create_product(product: Product):
    products = load_products()
    products.append(product.dict())
    save_products(products)
    return {"message": "Product created successfully"}

# GET /products - Retrieve all products
@app.get("/products")
def get_products():
    products = load_products()
    return products
