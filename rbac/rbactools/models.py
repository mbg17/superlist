from django.db import models

# Create your models here.


class Permission(models.Model):
    url = models.CharField(max_length=64)
    title = models.CharField(max_length=32)
    action = models.CharField(max_length=32)
    group = models.ForeignKey('PermissionGroup',on_delete=models.DO_NOTHING,null=True)
    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField(Permission)
    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    roles = models.ManyToManyField(Role)
    def __str__(self):
        return self.username
        
class PermissionGroup(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title
