# Generated by Django 2.0 on 2019-11-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hint', '0022_auto_20191119_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='hintCount',
            field=models.PositiveIntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
