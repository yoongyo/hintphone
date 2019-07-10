from django.db import models
from django.conf import settings

Nation = (
    ('Korea', 'Korea'),
    ('Japan', 'Japan'),
    ('China', 'China'),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nation = models.CharField(max_length=30, choices=Nation, blank=True, null=True)
    escape_room = models.CharField(max_length=30)
    reset = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.escape_room
