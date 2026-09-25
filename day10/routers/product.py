from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import productResponse,createProduct

from database import get_db
from models import Product

router = APIRouter(prefix="/products",tags=["Products"])
@router.get("/",response_model=list[productResponse])
def get_products(db:Session=Depends(get_db)):
    result = db.execute(
        select(Product)
    )
    products = result.scalars().all()

    return products

@router.post("/",response_model=productResponse,status_code=201)
def create_product(product:createProduct,db:Session=Depends(get_db)):
    new_product = Product(
        name = product.name,
        price = product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.put("/{product_id}",response_model = productResponse)
def update_product(
    product_id:int,
    updated_product :createProduct,
    db:Session=Depends(get_db)
):
    product = db.get(Product,product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="product not found"
        )
    product.name = updated_product.name
    product.price = updated_product.price

    db.commit()
    db.refresh(product)

    return product

@router.delete("/{product_id}", status_code=204)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return


    
    