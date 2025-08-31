from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def async_generate_summary(text: str):
    return f"Async summary: {text[:50]}..."
