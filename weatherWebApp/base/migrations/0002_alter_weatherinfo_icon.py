# Generated by Django 5.0.3 on 2024-03-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherinfo',
            name='icon',
            field=models.CharField(max_length=10),
        ),
    ]
