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
        pass

    def post(self, request):
        print(request.data)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

