from django.db import models


# Create your models here.

# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    addr = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.id}:{self.name}>'


# 书籍表
class Book(models.Model):
    # 自增ID
    id = models.AutoField(primary_key=True)
    # varchar类型字段
    title = models.CharField(max_length=64, null=False, unique=True)
    # 外键 当主表删除后当前表一块删除 同时删除中间表所有数据
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.id}:{self.title}>'

# 作者信息
class Author(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=16,null=False,unique=True)
    # 多对多关系 创建第三张中间表 存的是具体书的对象
    book = models.ManyToManyField(Book)
    detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.name}>'

class AuthorDetail(models.Model):
    hobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=12)