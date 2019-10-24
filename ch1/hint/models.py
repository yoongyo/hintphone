from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class Theme(models.Model):
    roomEscape = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enterKey = models.CharField(max_length=50)
    theme_number = models.PositiveIntegerField(null=True, blank=True)
    hintCount = models.PositiveIntegerField(default=3)
    name = models.CharField(max_length=30)

    hint1 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint1 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint1 = RichTextUploadingField(blank=True, null=True)
    sub_textHint1 = RichTextUploadingField(blank=True, null=True)

    hint2 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint2 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint2 = RichTextUploadingField(blank=True, null=True)
    sub_textHint2 = RichTextUploadingField(blank=True, null=True)

    hint3 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint3 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint3 = RichTextUploadingField(blank=True, null=True)
    sub_textHint3 = RichTextUploadingField(blank=True, null=True)

    hint4 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint4 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint4 = RichTextUploadingField(blank=True, null=True)
    sub_textHint4 = RichTextUploadingField(blank=True, null=True)

    hint5 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint5 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint5 = RichTextUploadingField(blank=True, null=True)
    sub_textHint5 = RichTextUploadingField(blank=True, null=True)

    hint6 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint6 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint6 = RichTextUploadingField(blank=True, null=True)
    sub_textHint6 = RichTextUploadingField(blank=True, null=True)

    hint7 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint7 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint7 = RichTextUploadingField(blank=True, null=True)
    sub_textHint7 = RichTextUploadingField(blank=True, null=True)

    hint8 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint8 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint8 = RichTextUploadingField(blank=True, null=True)
    sub_textHint8 = RichTextUploadingField(blank=True, null=True)

    hint9 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint9 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint9 = RichTextUploadingField(blank=True, null=True)
    sub_textHint9 = RichTextUploadingField(blank=True, null=True)

    hint10 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint10 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint10 = RichTextUploadingField(blank=True, null=True)
    sub_textHint10 = RichTextUploadingField(blank=True, null=True)

    hint11 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint11 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint11 = RichTextUploadingField(blank=True, null=True)
    sub_textHint11 = RichTextUploadingField(blank=True, null=True)

    hint12 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint12 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint12 = RichTextUploadingField(blank=True, null=True)
    sub_textHint12 = RichTextUploadingField(blank=True, null=True)

    hint13 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint13 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint13 = RichTextUploadingField(blank=True, null=True)
    sub_textHint13 = RichTextUploadingField(blank=True, null=True)

    hint14 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint14 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint14 = RichTextUploadingField(blank=True, null=True)
    sub_textHint14 = RichTextUploadingField(blank=True, null=True)

    hint15 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint15 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint15 = RichTextUploadingField(blank=True, null=True)
    sub_textHint15 = RichTextUploadingField(blank=True, null=True)

    hint16 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint16 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint16 = RichTextUploadingField(blank=True, null=True)
    sub_textHint16 = RichTextUploadingField(blank=True, null=True)

    hint17 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint17 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint17 = RichTextUploadingField(blank=True, null=True)
    sub_textHint17 = RichTextUploadingField(blank=True, null=True)

    hint18 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint18 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint18 = RichTextUploadingField(blank=True, null=True)
    sub_textHint18 = RichTextUploadingField(blank=True, null=True)

    hint19 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint19 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint19 = RichTextUploadingField(blank=True, null=True)
    sub_textHint19 = RichTextUploadingField(blank=True, null=True)

    hint20 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint20 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint20 = RichTextUploadingField(blank=True, null=True)
    sub_textHint20 = RichTextUploadingField(blank=True, null=True)

    hint21 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint21 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint21 = RichTextUploadingField(blank=True, null=True)
    sub_textHint21 = RichTextUploadingField(blank=True, null=True)

    hint22 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint22 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint22 = RichTextUploadingField(blank=True, null=True)
    sub_textHint22 = RichTextUploadingField(blank=True, null=True)

    hint23 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint23 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint23 = RichTextUploadingField(blank=True, null=True)
    sub_textHint23 = RichTextUploadingField(blank=True, null=True)

    hint24 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint24 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint24 = RichTextUploadingField(blank=True, null=True)
    sub_textHint24 = RichTextUploadingField(blank=True, null=True)

    hint25 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint25 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint25 = RichTextUploadingField(blank=True, null=True)
    sub_textHint25 = RichTextUploadingField(blank=True, null=True)

    hint26 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint26 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint26 = RichTextUploadingField(blank=True, null=True)
    sub_textHint26 = RichTextUploadingField(blank=True, null=True)

    hint27 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint27 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint27 = RichTextUploadingField(blank=True, null=True)
    sub_textHint27 = RichTextUploadingField(blank=True, null=True)

    hint28 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint28 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint28 = RichTextUploadingField(blank=True, null=True)
    sub_textHint28 = RichTextUploadingField(blank=True, null=True)

    hint29 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint29 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint29 = RichTextUploadingField(blank=True, null=True)
    sub_textHint29 = RichTextUploadingField(blank=True, null=True)

    hint30 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint30 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint30 = RichTextUploadingField(blank=True, null=True)
    sub_textHint30 = RichTextUploadingField(blank=True, null=True)

    interPhone_key = models.CharField(max_length=100, blank=True, null=True)
    interPhone_secret = models.CharField(max_length=100, blank=True, null=True)
    interPhone_ID = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
