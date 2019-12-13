from django.shortcuts import HttpResponse


def add_session(user, request):
    request.session['user_id']=user.pk
    # permissions = user.roles.all().values('permissions__url')
    # permissions_list = []
    # for i in permissions:
    #     permissions_list.append(i['permissions__url'])
    # request.session['permissions_list']=permissions_list
    permissions = user.roles.all().values('permissions__url', 'permissions__group_id', 'permissions__action','permissions__title').distinct()
    permission_dict = {}
    for permission in permissions:
        id=permission['permissions__group_id']
        url=permission['permissions__url']
        action = permission['permissions__action']
        print(permission_dict.get(id))
        if permission_dict.get(id):
            permission_dict[id]['urls'].append(url)
            permission_dict[id]['actions'].append(action)
        else:
            permission_dict[id]={
                'urls':[url],
                'actions':[action]
            }
    request.session['permission_dict']=permission_dict
    permission_menu = []
    for menu in permissions:
        print(menu)
    request.session['permission_menu']=permission_menu

