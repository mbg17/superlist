from django.contrib import admin
from rbactools.models import *
# Register your models here.
class PermissionConfig(admin.ModelAdmin):
    list_display = ['title','url','group','action']
admin.site.register(User)
admin.site.register(Permission,PermissionConfig)
admin.site.register(Role)
admin.site.register(PermissionGroup)
