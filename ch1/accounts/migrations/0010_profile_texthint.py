# Generated by Django 2.1 on 2019-10-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191007_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='textHint',
            field=models.BooleanField(default=False),
        ),
    ]
