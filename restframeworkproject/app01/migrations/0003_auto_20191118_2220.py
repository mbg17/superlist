# Generated by Django 2.2 on 2019-11-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_throttle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='throttle',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]