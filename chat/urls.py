from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.room, name='room'),
    path('messages/write', views.message_write, name='message_write'),
    path('messages/', views.messages, name='messages'),
]
