from bots.models import Bot
from bots.serializers import BotSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BotMain(generics.CreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class BotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

