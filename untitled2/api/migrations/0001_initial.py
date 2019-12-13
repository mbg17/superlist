# Generated by Django 2.2 on 2019-12-04 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why', models.CharField(max_length=32)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='api.Course')),
                ('recommend', models.ManyToManyField(related_name='recommend_course_id', to='api.Course')),
            ],
        ),
    ]
