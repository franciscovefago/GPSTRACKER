# Generated by Django 3.1.4 on 2023-05-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps_app', '0002_auto_20230510_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpsdevice',
            name='is_connected',
            field=models.BooleanField(default=False),
        ),
    ]
