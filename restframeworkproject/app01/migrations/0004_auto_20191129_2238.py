# Generated by Django 2.2 on 2019-11-29 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20191118_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]
