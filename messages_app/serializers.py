from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Message

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    recipient = PhoneNumberField(region="BR")

    class Meta:
        model = Message
        fields = ['id', 'user', 'recipient', 'message', 'pending', 'scheduled_date', 'created_at']