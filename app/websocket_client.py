import asyncio
import websockets
import json
from datetime import datetime

from app.config import WS_URL
from app.csv_writer import write_row
from app import state


async def listen_binance():
    while state.running:
        try:
            async with websockets.connect(WS_URL) as websocket:
                print("✅ Connected to Binance")

                while state.running:
                    message = await websocket.recv()
                    data = json.loads(message)
                    print("📈 Received:", data)

                    row = [
                        datetime.fromtimestamp(data["E"] / 1000),
                        data["s"],
                        float(data["p"]),
                        float(data["q"]),
                        datetime.fromtimestamp(data["T"] / 1000)
                    ]

                    write_row(row)

        except Exception as e:
            print("❌ Error:", e)
            await asyncio.sleep(5)  # retry