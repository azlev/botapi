from bots.models import Bot
from messages.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    conversationId = serializers.UUIDField(required=True)
    timestamp = serializers.DateTimeField(required=True)
    bot = serializers.UUIDField()
    direction = serializers.CharField(max_length=1)
    client = serializers.UUIDField()
    text = serializers.CharField(required=True)

    def _direction(self, data, botkey, clientkey, direction):
        try:
            b = Bot.objects.get(id=data[botkey])
            data['bot'] = b.id
            data['client'] = data[clientkey]
            data['direction'] = direction
        except Bot.DoesNotExist:
            return False
        return True

    def validate(self, data):
        """
        Check and transform from and to in bot, direction and client
        """
        print("mimimi", data)
        if not self._direction(data, 'from', 'to', 'F'):
            if not self.direction(data, 'to', 'from', 'T'):
                raise serializers.ValidationError("Bot not found")
        #del data['from']
        #del data['to']
        return data
