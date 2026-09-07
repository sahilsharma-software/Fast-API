from fastapi import APIRouter

router = APIRouter(prefix="/products",tags=["products"])


products = [
    {"id": 1, "name": "Mobile", "price": 20000},
    {"id": 2, "name": "Laptop", "price": 50000},
]

from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:int



@router.get("/")
def get_products():
    return products


# get prouct by product id
@router.get("/{product_id}")
def get_product(product_id:int):
    for product in products:
        if product_id == product["id"]:
            return product
        
    return{"message":"product not found"}   

## create product
@router.post("/")
def create_product(product:Product):
    products.append(product.model_dump())
    return product


# update the product

@router.put("/{product_id}")
def update_product(product_id:int , updated_product:Product):
    for index ,product in enumerate(products):
        if product_id == product["id"]:
            products[index] = update_product
            return update_product
    return {"message":"product not found"}

## delete a product

@router.delete("/{product_id}")
def delete_product(product_id:int):
    for index , product in enumerate(products):
        if product_id == product["id"]:
            products.pop(index)
            return {"message":"product deleted successfully"}
        
    return {"message":"product not found"}


 