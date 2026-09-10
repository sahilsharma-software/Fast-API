from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import (
    get_all_products,
    create_product as create_product_db,
    get_product_by_id,
    update_product as update_product_db,
    delete_product as delete_product_db
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# Request model
class ProductCreate(BaseModel):
    name: str
    price: int


# Response model
class ProductResponse(BaseModel):
    id: int
    name: str
    price: int


# CREATE product
@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):

    return create_product_db(
        product.name,
        product.price
    )


# READ all products
@router.get("/", response_model=list[ProductResponse])
def get_products():

    return get_all_products()


# READ product by ID
@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):

    product = get_product_by_id(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# UPDATE product
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    updated_product: ProductCreate
):

    product = update_product_db(
        product_id,
        updated_product.name,
        updated_product.price
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# DELETE product
@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int):

    deleted = delete_product_db(product_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return