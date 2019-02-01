from rest_framework import serializers

from bots.models import Bot
from messages.models import Message


class MessageSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    conversationId = serializers.UUIDField(required=True)
    timestamp = serializers.DateTimeField(required=True)
    # 1/2 dealing with reserved word "from"
    frm = serializers.UUIDField(source='from_')
    to = serializers.UUIDField()
    text = serializers.CharField(required=True)

    def create(self, validated_data):
        print(validated_data)
        m = Message()
        m.conversationId = validated_data['conversationId']
        m.timestamp = validated_data['timestamp']
        m.from_ = validated_data['from_']
        m.to = validated_data['to']
        m.text = validated_data['text']
        m.save()

        return m
# 2/2 dealing with reserved word "from"
MessageSerializer._declared_fields['from'] = MessageSerializer._declared_fields['frm']
del MessageSerializer._declared_fields['frm']
