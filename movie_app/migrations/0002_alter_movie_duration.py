# Generated by Django 4.2.9 on 2024-01-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.FloatField(),
        ),
    ]
