import redis

try:
    r = redis.Redis(host="localhost", port=6379)
    print(r.ping())
    print("✅ Redis Connected Successfully")
except Exception as e:
    print("❌ Error:", e)