# Generated by Django 2.0 on 2019-12-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0029_remove_theme_theme_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='manyHint',
            field=models.BooleanField(default=False),
        ),
    ]
