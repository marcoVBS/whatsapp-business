from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
import re

from .models import Message
from .serializers import MessageSerializer
from .whatsapp.api import WhatsAppAPI

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows messages management
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if (user.is_superuser):
            query_set = Message.objects.all()
        else:
            query_set = Message.objects.filter(user=user)
        return query_set.order_by('-created_at')

    def create(self, request):

        scheduled_date = request.POST.get('scheduled_date', datetime.now())
        if isinstance(scheduled_date, str):
            scheduled_date = datetime.strptime(scheduled_date, '%Y-%m-%d %H:%M:%S')

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = Message.objects.create(
                recipient=re.sub("[^0-9]", "", serializer.data['recipient']),
                message=serializer.data['message'],
                scheduled_date=scheduled_date,
                pending=True,
                user_id=request.user.id
            )
        else:
            return Response({"errors": serializer.errors})

        if scheduled_date <= datetime.now():
            api = WhatsAppAPI()
            api.send_message(request.data['recipient'], request.data['message'])

            message.pending = False
            message.save()

        return Response(MessageSerializer(message).data)