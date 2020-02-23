from django.contrib import admin
from .models import Login
from .models import Messages, Session

admin.site.register(Login)
admin.site.register(Messages)
admin.site.register(Session)

if len(Login.objects.all()) == 0:
    Login.objects.create(email="Mary@ukr.net", password="1234", name='Mary')
    Login.objects.create(email="Jack@ukr.net", password="4321", name='Jack')
