# Generated by Django 2.2 on 2019-11-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('addr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('book', models.ManyToManyField(to='app01.Book')),
                ('detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail')),
            ],
        ),
    ]
