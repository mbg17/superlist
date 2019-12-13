from django.shortcuts import render,HttpResponse
from rbactools.utils.permission import add_session
from rbactools.models import *
# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(username=username, pwd=pwd).first()
        print(user)
        if user:
            request.session['user_id']=user.pk
            add_session(user,request)
            return HttpResponse('登录成功')
    return render(request,'login.html')