from pydantic import BaseModel

class createProduct(BaseModel):
    name:str
    price:int

class productResponse(BaseModel):
    id:int
    name:str
    price:int

