from django.db import models

# Create your models here.

# 应用数据库
# python manage.py makemigrations
# python manage.py migrate
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=20)

