from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item,List


# Create your views here.
def home_page(request):
    # 处理POST请求
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'],list=list_)
    #     # 重定向
    #     return redirect('/lists/the-only-list-in-the-world/')
    # 返回模板数据
    # return render(request,'home.html'）
    # 渲染数据到模板 {{new_item_text}}
    # else:
    #     new_item_text=''
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/the-only-list-in-the-world/')