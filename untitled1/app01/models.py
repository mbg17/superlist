from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    tel =models.CharField(max_length=32)
    def __str__(self):
        return self.username

class Room(models.Model):
    caption = models.CharField(max_length=32)
    num = models.IntegerField()
    def __str__(self):
        return self.caption

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time_list = (
        (1,'08:00'),
        (2,'09:00'),
        (3,'10:00'),
        (4,'11:00'),
        (5,'12:00'),
        (6,'13:00'),
        (7,'14:00'),
        (8,'15:00'),
        (9,'16:00'),
        (10,'17:00'),
        (11,'18:00'),
        (12,'19:00'),
        (13,'20:00'),
    )
    time = models.IntegerField(choices=time_list)
    class Meta:
        unique_together = (('room','date','time'),)

    def __str__(self):
        return f'{self.user.username}预定了{self.room.caption}'