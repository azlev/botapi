from bots.models import Bot
from messages.models import Message
from messages.serializers import MessageSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MessageMain(APIView):
    """
    This logic is not just crud, hence APIView is better suitable
    """
    def get(self, request):
        conversationId = request.query_params.get("conversationId", None)
        messages = Message.objects.filter(conversationId=conversationId).order_by("timestamp")
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

