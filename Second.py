from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Optional

app = FastAPI()

class Address(BaseModel):
    city:str
    state:str
    pincode:int

class User(BaseModel):
    name:str = Field(min_length=3,max_length=50 ,description="Name of the User" )

    email:str = Field(description="Email address of the user")
    age : int = Field(ge=18,le=100,description="Age of the user")
    address : Address
    phone :int = Field(description="Phone number of the user")
    skills:list[str]

@app.post("/users")
def create_user(user:User):
    return user   