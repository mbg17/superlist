from Xadmin.service.Xadmin import site,ModelAdmin
from rbactools.models import *
site.register(User)
class PerConfig(ModelAdmin):
    list_display=['id','url','title','action','group']
site.register(Permission,PerConfig)
site.register(Role)
site.register(PermissionGroup)