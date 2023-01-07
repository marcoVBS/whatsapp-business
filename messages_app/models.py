from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(to=User, null=False, verbose_name='Message owner', on_delete=models.CASCADE)
    recipient = models.CharField(max_length=15, null=False, verbose_name='Recipient Whatsapp number')
    message = models.TextField(null=False, verbose_name='Text message to send')
    pending = models.BooleanField(default=False, verbose_name='Defines whether the message is pending delivery')
    scheduled_date = models.DateTimeField(null=True, verbose_name='Message sending schedule date')
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Creation date')
