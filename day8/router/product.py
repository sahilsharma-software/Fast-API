from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/product",
    tags=["Products"]
)


class ProductCreate(BaseModel):
    name: str
    price: int


class ResponseProduct(BaseModel):
    id: int
    name: str
    price: int


products = [
    {
        "id": 1,
        "name": "Mobile",
        "price": 20000
    },
    {
        "id": 2,
        "name": "Laptop",
        "price": 50000
    }
]


# Create new product
@router.post("/", response_model=ResponseProduct,status_code=201)
def create_product(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }

    products.append(new_product)

    return new_product


# Get all products
@router.get("/", response_model=list[ResponseProduct])
def get_products():
    return products


# Get product by ID
@router.get("/{product_id}", response_model=ResponseProduct)
def get_product(product_id: int):
    for product in products:
        if product_id == product["id"]:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

### update product
@router.put("/{product_id}", response_model=ResponseProduct)
def update_product(product_id: int, updated_product: ProductCreate):

    for index, product in enumerate(products):

        if product_id == product["id"]:

            new_product = {
                "id": product_id,
                "name": updated_product.name,
                "price": updated_product.price
            }

            products[index] = new_product

            return new_product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

## delete product
@router.delete("/{product_id}",status_code=204)
def delete_product(product_id:int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="product not found"
    )
        