# Generated by Django 2.0 on 2019-10-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0017_auto_20190906_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='hintCount',
            field=models.PositiveIntegerField(default=3),
        ),
    ]