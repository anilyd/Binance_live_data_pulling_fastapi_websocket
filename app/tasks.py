from app.celery_app import celery
from app.db import save_to_db

@celery.task
def process_data(data):
    print("✅ process_data received:", data)
    save_to_db(data)