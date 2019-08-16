from django.db import models

# Create your models here.

# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False,unique=True)
    addr = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.id}:{self.name}>'

# 书籍表
class Book(models.Model):
    id = models.AutoField(primary_key=True) # 自增ID
    title = models.CharField(max_length=64,null=False,unique=True) # varchar类型字段
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)# 外键

    def __str__(self):
        return f'<{self.id}:{self.title}>'