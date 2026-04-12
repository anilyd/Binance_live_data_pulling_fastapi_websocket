import csv
import logging
import time
from app.config import CSV_FILE, DATA_DIR

CURRENT_CSV_FILE = CSV_FILE

def _ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _open_csv_file(mode):
    global CURRENT_CSV_FILE
    try:
        return open(CURRENT_CSV_FILE, mode, newline="")
    except PermissionError:
        if CURRENT_CSV_FILE == CSV_FILE:
            fallback_file = DATA_DIR / f"binance_data_{int(time.time())}.csv"
            logging.warning(
                "CSV file %s is locked; writing to fallback %s",
                CSV_FILE,
                fallback_file,
            )
            CURRENT_CSV_FILE = fallback_file
            return open(CURRENT_CSV_FILE, mode, newline="")
        raise


def init_csv():
    _ensure_data_dir()
    with _open_csv_file("w") as file:
        writer = csv.writer(file)
        writer.writerow([
            "event_time",
            "symbol",
            "price",
            "quantity",
            "trade_time"
        ])


def write_row(row):
    _ensure_data_dir()
    with _open_csv_file("a") as file:
        writer = csv.writer(file)
        writer.writerow(row)