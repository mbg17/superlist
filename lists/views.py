from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    # 处理POST请求
    # if request.method=='POST':
    #     return HttpResponse(request.POST['item_text'])
    # 返回模板数据
    # return render(request,'home.html'）
    # 渲染数据到模板 {{new_item_text}}
    return render(request,'home.html',{
        'new_item_text':request.POST.get('item_text','')
        })