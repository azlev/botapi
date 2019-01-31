from bots.models import Bot
from rest_framework import serializers

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id', 'name')

