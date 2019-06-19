from django.db import models


class RoomEscape(models.Model):
    name = models.CharField(max_length=20)
    admin = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Theme(models.Model):
    roomEscape = models.ForeignKey(RoomEscape, on_delete=models.CASCADE)
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
