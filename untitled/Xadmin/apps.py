from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules
from Xadmin.service.Xadmin import site
class XadminConfig(AppConfig):
    name = 'Xadmin'

    # 每次启动扫描每个APP下的Xadmin文件
    def ready(self):
        autodiscover_modules('Xadmin')