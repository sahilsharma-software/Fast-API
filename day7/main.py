from fastapi import FastAPI

from routers.products import router

from routers.user import user_router

from routers.order import order_router

app = FastAPI()

app.include_router(router)
app.include_router(user_router)
app.include_router(order_router)
