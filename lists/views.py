from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    # 处理POST请求
    if request.method=='POST':
        new_item_text=request.POST['item_text']
        Item.objects.create(text=new_item_text)
        # 重定向
        return redirect('/')
    # 返回模板数据
    # return render(request,'home.html'）
    # 渲染数据到模板 {{new_item_text}}
    # else:
    #     new_item_text=''
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})