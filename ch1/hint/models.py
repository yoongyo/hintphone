from django.db import models
from django.conf import settings


class Theme(models.Model):
    roomEscape = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme_number = models.PositiveIntegerField(null=True, blank=True)
    hintCount = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    hint1 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint2 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint3 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint4 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint5 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint6 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint7 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint8 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint9 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint10 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint11 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint12 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint13 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint14 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint15 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint16 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint17 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint18 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint19 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)
    hint20 = models.FileField(upload_to='{0}/{1}/'.format(roomEscape, name), blank=True, null=True)

    def __str__(self):
        return self.name
