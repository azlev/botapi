from django.urls import include, path
from rest_framework import routers
from bots import views

from django.urls import path
from bots import views

urlpatterns = [
    path('bots', views.BotMain.as_view()),
    path('bots/<uuid:pk>', views.BotDetail.as_view()),
    path('messages', views.MessageMain.as_view()),
    path('messages/<uuid:pk>', views.MessageDetail.as_view()),
]
