from fastapi import APIRouter
from pydantic import BaseModel

user_router = APIRouter(prefix="/user",tags=["Users"])

users =[
    {
        "id":1,
        "name":"sahil",
        "email":"sahil@gmail.com"
    },
    {
        "id":2,
        "name":"aman",
        "email":"aman@gmail.com"
    }
]

class User(BaseModel):
    id:int
    name:str
    email:str



@user_router.get("/")
def get_user():
    return users

@user_router.get("/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user_id == user["id"]:
            return user
    return{"message":"user not found"}


@user_router.post("/")
def create_user(user:User):
    users.append(user.model_dump())
    return user

## update the user
@user_router.put("/{user_id}")
def update_user(user_id:int,updated_user:User):
    for index , user in enumerate(users):
        if user_id == user["id"]:
            users[index] = updated_user
            return update_user
    return {"message":"user not found"}

## delete the user

@user_router.delete("/{user_id}")
def delete_user(user_id:int):
    for index,user in enumerate(users):
        if user_id == user["id"]:
            users.pop(index)
            return{"message":"user deleted successfully"}
        
    return {"message":"user not found"}


