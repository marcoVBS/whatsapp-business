from datetime import datetime
from celery import shared_task

from .models import Message
from .whatsapp.api import WhatsAppAPI

@shared_task(name = "send_pending_messages")
def send_pending_messages():
    messages = Message.objects.filter(pending=True, scheduled_date__lt=datetime.now())
    api = WhatsAppAPI()
    for message in messages:
        api.send_message(message.recipient, message.message)

        message.pending = False
        message.save()