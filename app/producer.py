import asyncio
import websockets
import json
from app.redis_client import push

WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

async def start_producer():
    async with websockets.connect(WS_URL) as ws:
        print("✅ Connected Binance")

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            trade = {
                "symbol": data["s"],
                "price": float(data["p"]),
                "quantity": float(data["q"])
            }

            push(trade)