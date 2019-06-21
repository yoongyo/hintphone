from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    escape_room = models.CharField(max_length=30)
    reset = models.CharField(max_length=20)
    admin = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.escape_room
