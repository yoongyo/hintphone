# Generated by Django 2.0 on 2019-08-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0014_auto_20190801_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='enterKey',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
