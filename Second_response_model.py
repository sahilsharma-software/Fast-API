from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

@app.post("/users",response_model=UserResponse)
def create_user(user:UserRequest):
    return user

@app.post("/new_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully"}

@app.get("/user/{user_id}")
def get_user(user_id:int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {"user_id":user_id,"name":"Tiya"}


@app.get("/get_age/{user_age}")
def get_age(user_age:int):
    if user_age < 18:
        raise HTTPException(
            status_code=400,
            detail="age must be 18 or above"
        )
    return {"VALId AGe"}

@app.get("/admin")
def access_admin(is_admin = False):
    if not is_admin:
        raise HTTPException(
            status_code=403,
            detail="you don;t have permisison"
        )
    return {"message ":"welcome to admin portal"}
    