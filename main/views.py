from django.http import HttpResponseRedirect

from django.shortcuts import render

from .models import User, Messages

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'chatRoom.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def base(request):
    return render(request, 'registration/menu.html')


def chatRoom(request):
    if request.session.keys():
        date = Messages.objects.all()
        return render(request, 'chatRoom.html', {'date': date})
    else:
        return HttpResponseRedirect("/login/")


def add_DB_messages(request):
    if request.session.keys():
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
    else:
        return HttpResponseRedirect("/login/")
