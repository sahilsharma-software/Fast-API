from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from database import engine
from models import Base

from routers.auth import router

app = FastAPI()

import time

@app.middleware("http")
async def log_request_time(request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    print(
        f"{request.method} {request.url.path} - {process_time:.4f}s"
    )

    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)


Base.metadata.create_all(bind=engine)
app.include_router(router)