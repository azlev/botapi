from django.urls import path
from bots import views


urlpatterns = [
    path('', views.BotMain.as_view()),
    path('/<uuid:pk>', views.BotDetail.as_view()),
]
