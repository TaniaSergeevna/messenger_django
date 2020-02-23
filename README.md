# messenger_django

Technology :

-Python 3.6
-Django
-SQLite
-HTML
-CSS
-Bootstrap 4

This project can be run on any computer with any OS. To ran we need install Python ( https://www.python.org/downloads/), 
install Django (pip install Django).
First, open one terminal and enter the project folder (cd messenger_dj).
To migrate(python manage.py makemigrations)(python manage.py migrate).
And start a server ( python manage.py runserver).
We get(Starting development server at http://127.0.0.1:8000/).
Open the address in the two browsers http://127.0.0.1:8000/ and we can see login page. 
Enter the datas(email = Mary@ukr.net, password = 1234 or email = Jack@ukr.net, password = 4321 )  the massengers page will open.
We can chat.


First, create a Django project(django-admin startproject messenger_dj) and create app(python manage.py startapp main).
Register the messenger_dj / settings.py application.
Creat DB (use DB Django), creat tree modele Login (use to store user information), Sessions(use to store sessions) and 
Messenger(use to store messenger).
We carry out migrations(python manage.py makemigrations)(python manage.py migrate) and create createsuperuser
(python manage.py createsuperuser), urls, views,templates.



