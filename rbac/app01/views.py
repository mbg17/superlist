from django.shortcuts import render,HttpResponse
from rbactools import models
from rbactools.utils.permission import add_session
# Create your views here.


def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = models.User.objects.filter(username=username, pwd=pwd).first()
        print(user)
        if user:
            add_session(user,request)
            return HttpResponse('登录成功')
    return render(request,'login.html')

def user(request):
    user_list = models.User.objects.all()
    user = models.User.objects.get(id=request.session.get('user_id'))
    return render(request,'user_list.html',{'user_list':user_list,'user':user})

def user_add(request):
    return HttpResponse('user_add')

def user_edit(request,id):
    return HttpResponse('user_edit')

def user_del(request):
    return HttpResponse('user_del')

def role(request):
    role_list = models.Role.objects.all()
    user = models.User.objects.get(id=request.session.get('user_id'))
    return render(request, 'role.html', {'role_list': role_list, 'user': user})