import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app import state
from app.producer import start_producer
from app.consumer import consume

app = FastAPI()




from app.consumer import consume



async def run_consumer_loop():
    print("Consumer loop started")

    while state.running:   
        consume.delay()
        await asyncio.sleep(1)

    print("Consumer loop stopped")

@app.get("/start")
async def start():
    if not state.running:
        state.running = True
        asyncio.create_task(start_producer())
        asyncio.create_task(run_consumer_loop())   #  important
        return {"message": "Started"}
    return {"message": "Already running"}


@app.get("/stop")
async def stop():
    state.running = False
    print("Pipeline stopped")
    return {"message": "Stopped"}