from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('entrance/', views.entrance, name='entrance/'),
    path('chatRoom/', views.chatRoom, name='chatRoom'),
    path('chatRoom/add_DB_messages/db', views.add_DB_messages, name="chatRoom/add_DB_messages/db"),
]
