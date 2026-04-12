from fastapi import WebSocket
from app.redis_client import r
import json

clients = []

async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            data = r.lrange("binance_queue", -1, -1)
            if data:
                msg = json.loads(data[0])
                for c in clients:
                    await c.send_json(msg)
    except:
        clients.remove(websocket)