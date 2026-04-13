from app.celery_app import celery
import app.tasks
from app.redis_client import pop
from app.db import save_to_db

import time



@celery.task
def consume():
    """
    Process ONE message from Redis queue
    """
    data = pop()

    if data:
        save_to_db(data)
        print("Saved:", data)
    else:
        print("No data in queue")
            
            
            
