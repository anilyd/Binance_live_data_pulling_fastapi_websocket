# Binance Real-Time Data Streamer (FastAPI + WebSocket)

This project streams real-time cryptocurrency trade data from Binance using WebSockets and stores it into a CSV file using FastAPI.

---

##  Features

* Real-time data streaming from Binance
* Async WebSocket handling
* CSV storage for persistence
* FastAPI endpoints to control streaming (Start/Stop)
* Auto-reconnect on failure
* Clean modular architecture

---

## Project Structure

```
binance_streamer/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point
│   ├── websocket_client.py # Binance WebSocket logic
│   ├── csv_writer.py       # CSV handling logic
│   ├── config.py           # Config/constants
│   └── state.py            # Global state flag
│
├── data/
│   └── binance_data.csv    # Output CSV file
│
├── requirements.txt
└── README.md
```

---

##  Installation

### 1️ Clone the repository

```
git clone <your-repo-url>
cd binance_streamer
```

### 2 Create virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3 Install dependencies

```
pip install -r requirements.txt
```

---

##  Running the Application

Start FastAPI server:

```
uvicorn app.main:app --reload
```

---

##  API Endpoints

###  Start Streaming

```
GET /start
```

Starts Binance WebSocket streaming and begins writing data to CSV.

---

###  Stop Streaming

```
GET /stop
```

Stops the streaming process.

---

###  Health Check

```
GET /
```

Returns API status.

---

##  Sample Output (CSV)

```
event_time,symbol,price,quantity,trade_time
2026-04-11 12:01:01,BTCUSDT,65000.5,0.002,2026-04-11 12:01:01
```

---

##  Configuration

Edit `app/config.py`:

```
WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
CSV_FILE = "data/binance_data.csv"
```

You can change:

* Trading pair (BTCUSDT → ETHUSDT etc.)
* Output file path

---

##  Future Improvements

*  Support multiple trading pairs
*  Add Redis queue for buffering
*  Store data in MongoDB / PostgreSQL
*  Build real-time dashboard (WebSocket broadcast)
*  Add data aggregation (candlesticks, OHLC)

---

##  Architecture Overview

```
Binance WebSocket
        ↓
Async Listener (websocket_client.py)
        ↓
CSV Writer (csv_writer.py)
        ↓
Storage (data/binance_data.csv)
```

FastAPI acts as a control layer to start/stop streaming.

---

##  Notes

* CSV writing is synchronous (can be optimized using queue)
* Ensure stable internet for uninterrupted streaming
* Binance WebSocket may disconnect → auto-reconnect handled

---

##  Author

**Anil Yadav**
Python Developer | Backend Engineer

---



