# Generated by Django 2.2 on 2019-12-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191204_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='slogan',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='courselist',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
