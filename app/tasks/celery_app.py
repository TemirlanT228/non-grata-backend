# app/tasks/celery_app.py

from celery import Celery

celery_app = Celery(
    "non_grata",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

celery_app.conf.task_routes = {
    "app.tasks.parse.parse_entity": {"queue": "parsing"}
}