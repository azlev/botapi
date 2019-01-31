from bots.models import Bot, Message
from bots.serializers import BotSerializer, MessageSerializer
from rest_framework import generics


class BotMain(generics.ListCreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class BotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class MessageMain(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

