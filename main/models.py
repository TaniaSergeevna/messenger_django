from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Messages(models.Model):
    name = models.CharField(max_length=40)
    messages = models.TextField(default='')
    date_time = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date_time = timezone.now()
        self.save()

    def __str__(self):
        return self.name
