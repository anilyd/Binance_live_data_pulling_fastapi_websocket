import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.producer import start_producer
from app.websocket_api import ws_endpoint
from app.consumer import consume

app = FastAPI()


@app.get("/")
def dashboard():
    return HTMLResponse(Path("templates/index.html").read_text())


@app.get("/start")
async def start():
    asyncio.create_task(start_producer())
    consume.delay()  # start celery task
    return {"message": "Started pipeline"}


app.websocket("/ws")(ws_endpoint)



from app.consumer import consume

@app.get("/start")
async def start():
    asyncio.create_task(start_producer())
    consume.delay()   # 👈 THIS IS CRITICAL
    return {"message": "Started"}