# Generated by Django 2.1 on 2019-10-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_hintcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hintCode',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interPhone',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
