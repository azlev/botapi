from bots.models import Bot
from bots.serializers import BotSerializer
from rest_framework import generics


class BotMain(generics.ListCreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class BotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

