import hashlib

from django.contrib import admin
from .models import Login
from .models import Messages, Session

admin.site.register(Login)
admin.site.register(Messages)
admin.site.register(Session)

if len(Login.objects.all()) == 0:
    print('1234',hashlib.sha1(b'1234').hexdigest())
    Login.objects.create(email="Mary@ukr.net",
                         password=hashlib.sha1(b'1234').hexdigest(), name='Mary')
    Login.objects.create(email="Jack@ukr.net",
                         password=hashlib.sha1(b'4321').hexdigest(),
                         name='Jack')
