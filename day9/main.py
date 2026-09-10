from fastapi import FastAPI
from database import get_db_connection, create_tables,insert_sample_product
from routers.product import router

app = FastAPI()

create_tables()

app.include_router(router)

insert_sample_product()


@app.get("/")
def home():
    connection = get_db_connection()
    connection.close()

    return {
        "message": "Database connection successful"
    }