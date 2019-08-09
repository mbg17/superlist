from django.shortcuts import HttpResponse,render

def login(request):
    print(request)
    return  render(request,'Bootstrap登录页面.html')