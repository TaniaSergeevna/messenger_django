from django.db import models
from django.utils import timezone


class Login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Messages(models.Model):
    name = models.CharField(max_length=40)
    messages = models.TextField(default='')
    date_time = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date_time = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=40)
    session = models.IntegerField()

    def __str__(self):
        return self.name
