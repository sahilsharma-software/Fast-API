from fastapi import FastAPI
import asyncio
import time
import httpx

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    return {
        "message":"This is synchronous"
    }

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(2)
    return {
        "message":"This is asynchronus"
    }

@app.get("/blocking")
def blocking():
        time.sleep(5)
        return{
             "message":"blocking finished"
        }
@app.get("/non-blocking")
async def non_blocking_endpoint():
    await asyncio.sleep(5)
    return {
        "message": "Non-blocking finished"
    }

@app.get("/bad-async")
async def bad_async():
     time.sleep(5)
     return {"message","bad response"}

@app.get("/good-async")
async def good_async():
     await asyncio.sleep(5)
     return {"message":"good respone"}

@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")

    return {
         "status code":response.status_code,
         "header":dict(response.headers),
         "data":response.json()
            }

@app.get("/sequential")
async def sequential():
    async with httpx.AsyncClient() as client:

        response1 = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        response2 = await client.get(
            "https://jsonplaceholder.typicode.com/posts/2"
        )

    return {
        "post1": response1.json(),
        "post2": response2.json()
    }

@app.get("/parallel")
async def parallel():
    async with httpx.AsyncClient() as client:

        response1, response2 = await asyncio.gather(
            client.get("https://jsonplaceholder.typicode.com/posts/1"),
            client.get("https://jsonplaceholder.typicode.com/posts/2")
        )

    return {
        "post1": response1.json(),
        "post2": response2.json()
    }
    