from fastapi import FastAPI,HTTPException , Query
from pydantic import BaseModel

app = FastAPI()

products = []

class Product(BaseModel):
    id:int
    name:str
    price:int
    category:str

@app.get("/")
def get():
    return {"message":"Product api is running"}


@app.post("/products")
def create_products(product:Product):
    products.append(product)
    return products


@app.get("/products")
def get_products(
    category:str | None= None,
    min_price:int | None = None,
    search:str | None = None,
    skip:int = Query(default=0,ge=1,le=10,description="maximum number of products to skip"),
    limit:int = Query(default=2,ge=1,le=100,description="maximum number of products to skip")
):
    filtered_product = []
    for product in products:
        if((category is None or product.category ==category)\
           and (min_price is None or product.price >= min_price)\
           and (search is None or search.lower() in product.name.lower())):
            filtered_product.append(product)
    return filtered_product[skip:skip+limit]
   

@app.get("/products/{product_id}")
def get_product(product_id:int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    for index,product in enumerate(products):
        if product.id == product_id:
            products.pop(index)
            return {"message":"Product deleted Successfully"}

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
