from bots.models import Bot, Message
from rest_framework import serializers

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id', 'name')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'conversationId', 'timestamp', 'bot', 'direction', 'client', 'text')
