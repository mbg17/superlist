from django.shortcuts import HttpResponse,render,redirect
from login import  models
# Create your views here.

def login(request):
    error_msg=''
    if request.method=='POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password', None)
        if email=='luyuan@qq.com' and password=='12345678':
            return redirect('http://www.baidu.com')
        else:
            error_msg='登录失败'
    return  render(request,'Bootstrap登录页面.html',{'error_msg':error_msg})

def user_list(request):
    ret = models.UserInfo.objects.all()
    return render(request,'user_list.html',{'user_list':ret})


def add_user(request):
    if request.method=='POST':
        new_name = request.POST.get('username',None)
        models.UserInfo.objects.create(name=new_name)
        return redirect('/user_list/')
    return render(request,'add_user.html')