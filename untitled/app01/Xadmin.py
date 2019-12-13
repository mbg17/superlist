from Xadmin.service.Xadmin import site
from Xadmin.service.Xadmin import ModelAdmin
from django.forms import ModelForm
from app01.models import *
from django.utils.safestring import mark_safe
from django.shortcuts import reverse,redirect

class BookModelClass(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        labels={
            'title':'书籍名称',
            'publisher':'出本社名称',
        }
class BookConfig(ModelAdmin):
    def play(self,request,queryset):
        queryset.update(price=100)
    play.desc='测试'
    list_display = ['title','publisher','price']
    list_display_links = ['title']
    moderlform_class = BookModelClass
    search_field = ['title']
    actions=[play]
    list_filter = ['publisher','author','title']

class AuthorConfig(ModelAdmin):
    list_display = ['book']

site.register(Book,BookConfig)
site.register(Publisher)
site.register(Author,AuthorConfig)