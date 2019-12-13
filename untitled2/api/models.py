from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=32,unique=True)
    course_img= models.CharField(max_length=32,null=True)
    level_list=(
        (1,'初级'),
        (2, '中级'),
        (3, '高级')
    )
    level = models.IntegerField(choices=level_list)

    def __str__(self):
        return self.title
import json
class CourseDetail(models.Model):
    course = models.OneToOneField(Course,on_delete=models.CASCADE)
    slogan = models.CharField(max_length=32,null=True)
    why = models.CharField(max_length=32)
    recommend = models.ManyToManyField(Course,related_name='rc')

    def __str__(self):
        return self.course.title

class CourseList(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.IntegerField(null=True)
    name = models.CharField(max_length=32)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title+self.name

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Token(models.Model):
    user = models.OneToOneField(UserInfo,on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
