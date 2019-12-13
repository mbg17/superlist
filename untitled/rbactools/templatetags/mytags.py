from django import template

register = template.Library()


@register.filter()
def check_permission(value, action):
    return value in action

@register.inclusion_tag('menu.html')
def get_menu(request):
    permission_menu=request.session['permission_menu']
    return {'permission_menu':permission_menu}