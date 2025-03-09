import os
from celery import Celery

# Set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

# Load config from settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks from installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
