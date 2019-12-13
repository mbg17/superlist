from Xadmin.service.Xadmin import site,ModelAdmin
from app02 import models
from app01.models import Book
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
# Register your models here.
class OrderConfig(ModelAdmin):
    # head_list=['目录']
    pass
site.register(models.Order,OrderConfig)
site.register(models.Food)
