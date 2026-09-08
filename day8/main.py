from fastapi import FastAPI 
from router.product import router

app = FastAPI()

app.include_router(router)