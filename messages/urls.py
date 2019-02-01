from django.urls import include, path
from messages import views


urlpatterns = [
    path('', views.MessageMain.as_view()),
    path('/<uuid:pk>', views.MessageDetail.as_view()),
]
