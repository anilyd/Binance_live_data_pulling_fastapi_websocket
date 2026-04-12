import asyncio
from fastapi import FastAPI

from app import state
from app.csv_writer import init_csv
from app.websocket_client import listen_binance

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Binance Stream API Running"}


@app.get("/start")
async def start_stream():
    if not state.running:
        state.running = True
        init_csv()
        asyncio.create_task(listen_binance())
        return {"message": "Streaming started"}
    return {"message": "Already running"}


@app.get("/stop")
async def stop_stream():
    state.running = False
    return {"message": "Streaming stopped"}