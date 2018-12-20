from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item,List


# Create your views here.
def home_page(request):
    # 处理POST请求
    # if request.method == 'POST':
    # request.POST['item_text'] 获取post中的值
    #     Item.objects.create(text=request.POST['item_text'],list=list_)
    #     # 重定向
    #     return redirect('/lists/the-only-list-in-the-world/')
    # 返回模板数据
    # return render(request,'home.html'）
    # 渲染数据到模板 {{new_item_text}}
    # else:
    #     new_item_text=''
    return render(request, 'home.html')


def view_list(request,list_id):
    # 获取List模型id
    list_ = List.objects.get(id=list_id)
    # filter 函数 通过id 过滤数据
    # items = Item.objects.filter(list=list_)
    # items = Item.objects.all()
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')