# Generated by Django 2.0 on 2019-07-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0012_auto_20190709_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='interPhone_ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='interPhone_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='interPhone_secret',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
