

import redis
import json

#r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(
    host="localhost",   # YOUR WSL IP
    port=6379,
    decode_responses=True
)


def push(data):
    r.rpush("binance_queue", json.dumps(data))

def pop():
    data = r.lpop("binance_queue")
    return json.loads(data) if data else None