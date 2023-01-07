import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
app = Celery("setup")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
    'send-pending-messages': {
        'task': 'send_pending_messages',
        'schedule': 30.0
    }
}