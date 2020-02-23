from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
from django.utils.crypto import random

from .models import Login, Messages, Session


def login(request):
    return render(request, 'entrance.html')


def chatRoom(request):
    date = Messages.objects.all()
    return render(request, 'chatRoom.html', {'date': date})


def entrance(request):
    try:

        m = Login.objects.get(email=request.POST['email'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id + random.randint(0, 1000)
            Session(
                name=m.name,
                session=request.session['member_id']

            ).save()

            return HttpResponseRedirect("/chatRoom/")
        else:
            return HttpResponse("Ваши логин и пароль не соответствуют.")

    except Login.DoesNotExist:

        return HttpResponse("Ваши логин и пароль не соответствуют.")


def add_DB_messages(request):
    dates = Session.objects.all()
    for data in dates:
        if data.session == request.session['member_id']:
            if request.method == "POST":
                if request.POST.get('messages') != '':
                    Messages(
                        name=data.name,
                        messages=request.POST.get('messages'),
                    ).save()

    return HttpResponseRedirect("/chatRoom/")
