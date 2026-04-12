from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
CSV_FILE = DATA_DIR / "binance_data.csv"