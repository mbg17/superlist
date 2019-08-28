from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse # 反向解析函数
from app01.models import Book,Publisher
# Create your views here.
def book_list(request):
    all_publisher_list = Publisher.objects.all()
    all_book_list = Book.objects.all()
    return render(request, 'book/book_list.html', {'all_book_list':all_book_list, 'all_publisher_list':all_publisher_list})

def add_book(request):
    all_publisher = Publisher.objects.all()
    error =''
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')
        if book_title:
            if Book.objects.filter(title=book_title):
                error = '添加的书籍已存在'
            else:
                Book.objects.create(title=book_title,publisher_id=new_publisher_id)
                return redirect(reverse('book_list'))
        else:
            error = '字段不能为空'
        return render(request, 'book/add_book.html', {'error':error, 'all_publisher':all_publisher})
    return render(request, 'book/add_book.html', {'all_publisher':all_publisher})

def delete_book(request,id):
    if request.method == 'GET':
        ret = Book.objects.filter(id=id)
        if ret:
            ret.delete()
            return redirect(reverse('book_list'))
        else:
            return HttpResponse('删除的书籍不存在')

def edit_book(request,id):
    """
    :param request: 请求对象
    :param id: 修改书籍的主键id
    :return:
    """
    if request.method =='POST':
        new_publisher_id = request.POST.get('publisher')
        new_title = request.POST.get('title')
        ret = Book.objects.filter(id = id)
        if ret:
            book = Book.objects.get(id = id)
            book.title = new_title
            book.publisher_id = new_publisher_id
            book.save()
            return redirect('/book_list/')
        return HttpResponse('编辑的书籍不存在')
    book_obj = Book.objects.get(id=id)
    publisher_list = Publisher.objects.all()
    return render(request, 'book/edit_book.html', {'publisher':publisher_list, 'book_obj':book_obj})