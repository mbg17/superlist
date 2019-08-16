from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import Publisher,Book

def publisher_list(request):
    ret = Publisher.objects.all().order_by('id')
    return render(request, 'publisher_list.html', {'publisher_list':ret})

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
    return render(request,'add_publisher.html',{'error':error_msg})
# filter 可以执行删除但不能执行更改
def delete_publisher(request):
    del_id = request.GET.get('id',None)
    ret = Publisher.objects.filter(id=del_id)
    if ret:
        ret.delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('删除对象不存在！')

def edit_publisher(request):
    if request.method=='POST':
        edit_id = request.POST.get('id')
        new_name = request.POST.get('name')
        new_addr = request.POST.get('addr')
        publisher_obj = Publisher.objects.filter(id = edit_id)
        if publisher_obj:
            old_name = Publisher.objects.get(id =edit_id )
            old_name.name=new_name
            old_name.addr=new_addr
            old_name.save()
            return  redirect('/publisher_list/')
        return HttpResponse('编辑的出版社不存在')
    old_id = request.GET.get('id')
    publisher_old = Publisher.objects.filter(id=old_id)
    if publisher_old:
        publisher = Publisher.objects.get(id=old_id)
        return render(request,'edit_publisher.html',{'publisher':publisher})
    return HttpResponse('编辑的出版社不存在')


def book_list(request):
    all_publisher_list = Publisher.objects.all()
    all_book_list = Book.objects.all()
    return render(request,'book_list.html',{'all_book_list':all_book_list,'all_publisher_list':all_publisher_list})

def add_book(request):
    all_publisher = Publisher.objects.all()
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')
        if book_title:
            if Book.objects.filter(title=book_title):
                return HttpResponse('添加的书籍已存在')
            Book.objects.create(title=book_title,publisher_id=new_publisher_id)
        else:
            return render(request,'add_book.html',{'error':'书籍字段不能为空','all_publisher':all_publisher})
        return redirect('/book_list/')
    return render(request,'add_book.html',{'all_publisher':all_publisher})

def delete_book(request):
    if request.method == 'GET':
        delete_id = request.GET.get('id',None)
        ret = Book.objects.filter(id=delete_id)
        if ret:
            ret.delete()
            return redirect('/book_list/')
        else:
            return HttpResponse('删除的书籍不存在')

def edit_book(request):
    if request.method =='POST':
        old_book_id= request.POST.get('id')
        new_publisher_id = request.POST.get('publisher')
        new_title = request.POST.get('title')
        ret = Book.objects.filter(id = old_book_id)
        if ret:
            book = Book.objects.get(id = old_book_id)
            book.title = new_title
            book.publisher_id = new_publisher_id
            book.save()
            return redirect('/book_list/')
        return HttpResponse('编辑的书籍不存在')
    book_id = request.GET.get('id')
    book_obj = Book.objects.get(id=book_id)
    publisher_list = Publisher.objects.all()
    return render(request,'edit_book.html',{'publisher':publisher_list,'book_obj':book_obj})