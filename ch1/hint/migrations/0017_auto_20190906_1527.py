# Generated by Django 2.0 on 2019-09-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0016_auto_20190906_1526'),
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
