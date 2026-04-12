from app.celery_app import celery
import app.tasks
from app.redis_client import pop
from app.db import save_to_db

import time

@celery.task
def consume():
    while True:
        data = pop()
        if data:
            save_to_db(data)
            print("Saved:", data)
        else:
            time.sleep(1)
            
            
            
# from app.celery_app import celery
# from app.redis_client import pop
# from app.db import save
# from app import state
# import time

# @celery.task
# def consume():
#     print("✅ Consumer started")

#     while state.running:   # 👈 control loop
#         data = pop()
#         if data:
#             save(data)
#             print("Saved:", data)
#         else:
#             time.sleep(1)