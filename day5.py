from fastapi import FastAPI,Depends,Query,HTTPException, Header

app = FastAPI()

products = [
    {"id": 1, "name": "Mobile", "price": 20000, "category": "Electronics"},
    {"id": 2, "name": "Laptop", "price": 50000, "category": "Electronics"},
    {"id": 3, "name": "Shoes", "price": 3000, "category": "Fashion"},
    {"id": 4, "name": "Watch", "price": 5000, "category": "Fashion"},
    {"id": 5, "name": "Phone", "price": 30000, "category": "Electronics"}
]

def common_parameters(skip:int =Query(default=0,ge=0,le=100),
                      limit:int = Query(default=2,ge=1,le=100)):
    return {
            "skip":skip,
            "limit":limit
            }

@app.get("/products")
def get_products(data = Depends(common_parameters)):
    return products[data["skip"]:data["skip"]+data["limit"]]



def verify_api_key(x_api_key :str =Header()):
    if x_api_key != "12345":
        raise HTTPException(
            status_code=401,
            detail="invalid api  - key"
        )
    return x_api_key

def get_user(api_key = Depends(verify_api_key)):
    return {
        "id":1,
        "name":"Tiya",
        "api_key":api_key
    }

@app.get("/profile")
def get_profile(user = Depends(get_user)):
    return {
        "message":"welcome to profile",
        "user":user
    }
