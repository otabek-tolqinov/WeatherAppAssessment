# Generated by Django 5.0.3 on 2024-03-14 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_weatherinfo_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeatherInfo',
            new_name='WeatherData',
        ),
    ]
