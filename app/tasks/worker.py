# app/tasks/worker.py

from app.tasks.celery_app import celery_app

# задача зарегистрируется на старте Celery
import app.tasks.parse