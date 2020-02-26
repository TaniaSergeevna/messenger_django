from django.contrib.auth import views
from django.urls import path
from . import views as vs

# login Mary@ukr.net
# pass1234word
# login Jack@ukr.net
# pass4321word
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('chatRoom/', vs.chatRoom, name='chatRoom'),
    path('chatRoom/add_DB_messages/db', vs.add_DB_messages, name="chatRoom/add_DB_messages/db"),
]
