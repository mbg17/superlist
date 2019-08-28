from django.shortcuts import render,redirect,HttpResponse
from app01.models import Publisher
# Create your views here.
def publisher_list(request):
    ret = Publisher.objects.all().order_by('id')
    return render(request, 'publisher/publisher_list.html', {'publisher_list':ret})

def add_publisher(request):
    error_msg = ''
    if request.method=='POST':
        new_publisher = request.POST.get('publisher',None)
        new_addr = request.POST.get('addr', None)
        if new_publisher:
            Publisher.objects.create(name=new_publisher,addr=new_addr)
            return redirect('/publisher_list/')
        else:
            error_msg = '提交内容不能为空'
    return render(request, 'publisher/add_publisher.html', {'error':error_msg})
# filter 可以执行删除但不能执行更改
def delete_publisher(request,id):
    ret = Publisher.objects.filter(id=id)
    if ret:
        ret.delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('删除的出版社不存在！')

def edit_publisher(request,id):
    if request.method=='POST':
        new_name = request.POST.get('name')
        new_addr = request.POST.get('addr')
        publisher_obj = Publisher.objects.filter(id = id)
        if publisher_obj:
            old_name = Publisher.objects.get(id =id )
            old_name.name=new_name
            old_name.addr=new_addr
            old_name.save()
            return  redirect('/publisher_list/')
        return HttpResponse('编辑的出版社不存在')
    publisher_old = Publisher.objects.filter(id=id)
    if publisher_old:
        publisher = Publisher.objects.get(id=id)
        return render(request, 'publisher/edit_publisher.html', {'publisher':publisher})
    return HttpResponse('编辑的出版社不存在')