from django.test import TestCase

from rest_framework.test import APIRequestFactory

from .models import Message
from .views import MessageMain, MessageDetail
from bots.views import BotMain

class MessageTests(TestCase):

    def test_messagedetail_get_only(self):
        factory = APIRequestFactory()
        request = factory.post('/bots', {'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Aureo'})
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 201)

        message = {
            "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
            "timestamp": "2018-11-16T23:30:52.6917722Z",
            "from": "36b9f842-ee97-11e8-9443-0242ac120002",
            "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
            "text": "Oi! Como posso te ajudar?"
        }
        request = factory.post("/messages", message)
        response = MessageMain.as_view()(request)
        self.assertEqual(response.status_code, 201)


        request = factory.post("/messages/7665ada8-3448-4acd-a1b7-d688e68fe9a1", message)
        response = MessageDetail.as_view()(request)
        self.assertEqual(response.status_code, 405)

