from fastapi import APIRouter
from pydantic import BaseModel

order_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


class Order(BaseModel):
    id: int
    product_id: int
    quantity: int


orders = [
    {
        "id": 1,
        "product_id": 2,
        "quantity": 1
    },
    {
        "id": 2,
        "product_id": 1,
        "quantity": 3
    }
]


@order_router.get("/")
def get_orders():
    return orders


@order_router.get("/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order

    return {"message": "Order not found"}


@order_router.post("/")
def create_order(order: Order):
    orders.append(order.model_dump())
    return order