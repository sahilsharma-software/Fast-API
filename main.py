from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users")
def get_user():
    return {"message":"user retrieved"}



@app.post("/users")
def create_user():
    return {"message":"user Created"}

@app.delete("/users")
def delete_user():
    return {"message":"user Deleted"}

@app.put("/users")
def update_user():
    return {"message":"user updated"}

### path parameter

@app.get("/users/{user_id}")
def get_user_by_id(user_id:int):
    return {"user_id": user_id}


##  query parameters
@app.get("/products")
def get_products(category:str | None=None):
    return {"category":category}


@app.get("/search")
def search_products(
    keyWords:str,
    category:str,
    limit:int
):
    return {"keyword":keyWords,
            "category":category,
            "limit":limit
            }
