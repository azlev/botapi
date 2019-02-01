from django.test import TestCase

from rest_framework.test import APIRequestFactory

from .models import Bot
from .views import BotMain, BotDetail

class BotTests(TestCase):

    def test_botmain_should_accept_only_post(self):
        factory = APIRequestFactory()
        request = factory.post('/bots', {'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Aureo'})
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 201)

        request = factory.get('/bots')
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 405)

        request = factory.put('/bots', {'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Aureo'})
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 405)

        request = factory.delete('/bots')
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_botmain_do_not_duplicate(self):
        factory = APIRequestFactory()
        request = factory.post('/bots', {'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Aureo'})
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 201)

        request = factory.post('/bots', {'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Aureo'})
        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_botdetail_do_not_update_id(self):
        factory = APIRequestFactory()
        request = factory.post('/bots', {'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Aureo'})
        response = BotMain.as_view()(request)
        request = factory.put('/bots/36b9f842-ee97-11e8-9443-0242ac120002', {'id': '36b9f842-ee97-11e8-9443-0242ac120003', 'name': 'Aureo'})

        response = BotMain.as_view()(request)
        self.assertEqual(response.status_code, 405)
