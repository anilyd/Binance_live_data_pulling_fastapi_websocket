
import asyncio
import websockets
import json
from app.redis_client import push
from app import state

WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


async def start_producer():
    print("Producer started")

    while state.running:   # controlled externally
        try:
            async with websockets.connect(WS_URL) as ws:
                print("✅ Connected Binance")

                while state.running:
                    msg = await ws.recv()
                    data = json.loads(msg)

                    trade = {
                        "symbol": data["s"],
                        "price": float(data["p"]),
                        "quantity": float(data["q"])
                    }

                    print("Pushing:", trade)   # debug
                    push(trade)

        except Exception as e:
            print("Error:", e)
            await asyncio.sleep(1)   # reconnect