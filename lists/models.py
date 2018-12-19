from django.db import models

# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
    text=models.TextField(default='')
    #  外间关联
    list=models.ForeignKey(List,default=None,on_delete=models.SET_DEFAULT)
