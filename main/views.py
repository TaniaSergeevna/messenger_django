from django.http import HttpResponseRedirect

from django.shortcuts import render

from .models import User, Messages


def chatRoom(request):
    if request.session.keys():
        date = Messages.objects.all()
        return render(request, 'chatRoom.html', {'date': date})
    else:
        return HttpResponseRedirect("/login/")


def add_DB_messages(request):
    dates = User.objects.all()
    for data in dates:
        if data.get_session_auth_hash() == request.session['_auth_user_hash']:
            if request.method == "POST":
                if request.POST.get('messages') != '':
                    Messages(
                        name=data.first_name,
                        messages=request.POST.get('messages'),

                    ).save()

    return HttpResponseRedirect("/login/chatRoom/")
