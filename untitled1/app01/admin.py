from django.contrib import admin
from .models import *
# Register your models here.
class BookConfig(admin.ModelAdmin):
    list_display = ['room','user','date']

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Book,BookConfig)
