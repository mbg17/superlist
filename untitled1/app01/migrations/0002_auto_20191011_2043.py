# Generated by Django 2.2 on 2019-10-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
