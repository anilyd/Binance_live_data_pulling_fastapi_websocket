import asyncio
import json
import websockets
from datetime import datetime

from app.config import WS_URL
from app.csv_writer import write_row
from app.redis_client import push_to_queue
from app.tasks import process_data
from app import state


def _build_trade(data):
    return {
        "event_time": datetime.fromtimestamp(data["E"] / 1000).isoformat(),
        "symbol": data["s"],
        "price": float(data["p"]),
        "quantity": float(data["q"]),
        "trade_time": datetime.fromtimestamp(data["T"] / 1000).isoformat(),
        "trade_id": data["t"],
        "maker_side": data["m"],
        "is_best_match": data.get("M", True),
    }


async def listen_binance():
    while state.running:
        try:
            async with websockets.connect(WS_URL) as websocket:
                print("✅ Connected to Binance")

                while state.running:
                    message = await websocket.recv()
                    data = json.loads(message)
                    trade = _build_trade(data)

                    print("📥 Trade received:", trade)

                    write_row([
                        trade["event_time"],
                        trade["symbol"],
                        trade["price"],
                        trade["quantity"],
                        trade["trade_time"],
                    ])

                    push_to_queue(trade)
                    process_data.delay(trade)

        except Exception as e:
            print("❌ Error:", e)
            await asyncio.sleep(5)  # retry