from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    # 返回模板数据
    return render(request,'home.html')