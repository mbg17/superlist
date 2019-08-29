from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import Book,Author,AuthorDetail

def author_list(request):
    book_list = Book.objects.all()
    all_author = Author.objects.all()
    return render(request, 'author/author_list.html', {'author_list':all_author, 'book_list':book_list})

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
        books = request.POST.getlist('books',None)
        new_author = request.POST.get('author_name',None)
        hobby =request.POST.get('hobby',None)
        addr = request.POST.get('addr',None)
        if new_author:
            filter = Author.objects.filter(name=new_author)
            if filter:
                error = '添加的作者已存在'
            else:
                if hobby and addr:
                    detail = AuthorDetail.objects.create(hobby=hobby,addr=addr)
                    new_author_obj = Author.objects.create(name=new_author,detail=detail)
                # 把书和作者创建对应关系
                    new_author_obj.book.set(books)
                    return redirect('/author_list/')
                else:
                    error = '地址或者爱好不能为空'
        else:
            error = '添加的作者不能为空'
    return render(request, 'author/add_author.html', {'book_list':book_list, 'error':error})

def edit_author(request,id):
    if request.method == 'POST':
        ret = Author.objects.filter(id=id)
        if ret:
            new_author_name =request.POST.get('author_name')
            # 获取多选框所有数据
            new_book_list = request.POST.getlist('books')
            new_hobby = request.POST.get('hobby')
            new_addr = request.POST.get('addr')
            new_author_obj = Author.objects.get(id=id)
            new_detail_obj = new_author_obj.detail
            print(new_detail_obj)
            new_author_obj.name = new_author_name
            new_author_obj.book.set(new_book_list)
            new_detail_obj.hobby = new_hobby
            new_detail_obj.addr = new_addr
            new_detail_obj.save()
            new_author_obj.save()
            return redirect('/author_list/')
    book_list = Book.objects.all()
    author = Author.objects.filter(id = id)
    if author:
        author = Author.objects.get(id = id)
        return render(request, 'author/edit_author.html', {'author': author, 'book_list': book_list})
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