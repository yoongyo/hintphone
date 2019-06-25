# Generated by Django 2.0 on 2019-06-21 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0006_roomescape_reset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='roomEscape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RoomEscape',
        ),
    ]