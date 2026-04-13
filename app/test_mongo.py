from pymongo import MongoClient

try:
    # Connect
    client = MongoClient("mongodb://localhost:27017/")
    
    # Create DB
    db = client["binance"]
    
    # Create collection
    collection = db["trades"]
    
    # Insert test data
    test_data = {
        "symbol": "BTCUSDT",
        "price": 65000,
        "quantity": 0.01
    }
    
    result = collection.insert_one(test_data)
    
    print("Connected to MongoDB")
    print("Inserted ID:", result.inserted_id)

except Exception as e:
    print("Connection failed:", e)