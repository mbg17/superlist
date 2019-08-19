# 自定义filter
from django import template
register = template.Library()

# 注册名字为cut的自定义filter
# {% load myfilter %} 加载py文件
# {值:cut:""] 使用
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

# 不指定name 使用函数名
@register.filter
def lower(value):
    return value.lower()