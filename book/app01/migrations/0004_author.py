# Generated by Django 2.2 on 2019-08-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_publisher_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('book', models.ManyToManyField(to='book_list.Book')),
            ],
        ),
    ]
