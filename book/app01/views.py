from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import Publisher,Book,Author

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
        return HttpResponse('删除的出版社不存在！')

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

def author_list(request):
    book_list = Book.objects.all()
    all_author = Author.objects.all()
    return render(request,'author_list.html',{'author_list':all_author,'book_list':book_list})

def delete_author(request,delete_id):
    if delete_id and delete_id is not None:
        ret = Author.objects.filter(id=delete_id)
        if ret:
            Author.objects.get(id=delete_id).delete()
            return redirect('/author_list/')
        else:
            return HttpResponse('删除的用户不存在')
    return HttpResponse('删除的对象不能为空')

def add_author(request):
    error = ''
    book_list = Book.objects.all()
    if request.method == 'POST':
        books = request.POST.getlist('books')
        new_author = request.POST.get('author_name')
        if new_author:
            filter = Author.objects.filter(name=new_author)
            if filter:
                error = '添加的作者已存在'
            else:
                new_author_obj = Author.objects.create(name=new_author)
                # 把书和作者创建对应关系
                new_author_obj.book.set(books)
                return redirect('/author_list/')
        else:
            error = '添加的作者不能为空'
    return render(request,'add_author.html',{'book_list':book_list,'error':error})

def edit_author(request):
    if request.method == 'POST':
        new_author_id = request.POST.get('id')
        ret = Author.objects.filter(id=new_author_id)
        if ret:
            new_author_name =request.POST.get('author_name')
            # 获取多选框所有数据
            new_book_list = request.POST.getlist('books')
            new_author_obj = Author.objects.get(id=new_author_id)
            new_author_obj.name = new_author_name
            new_author_obj.book.set(new_book_list)
            new_author_obj.save()
            return redirect('/author_list/')
    book_list = Book.objects.all()
    get_id = request.GET.get('id')
    author = Author.objects.filter(id = get_id)
    if author:
        author = Author.objects.get(id = get_id)
        return render(request, 'edit_author.html', {'author': author, 'book_list': book_list})
    return redirect('/author_list/')

def upload(request):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request:
    :return:
    """
    if request.method == "POST":
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["file"].name
        # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for chunk in request.FILES["file"].chunks():
                # 写入本地文件
                f.write(chunk)
        return HttpResponse("上传OK")
    return render(request,'upload.html')