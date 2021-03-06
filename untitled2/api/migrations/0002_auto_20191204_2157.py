# Generated by Django 2.2 on 2019-12-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.IntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1),
            preserve_default=False,
        ),
    ]
