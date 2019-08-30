from django.shortcuts import HttpResponse, render, redirect
from login import models


# Create your views here.

def login(request):
    error_msg = ''
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email == 'luyuan@qq.com' and password == '12345678':
            return redirect('http://www.baidu.com')
        else:
            error_msg = '登录失败'
    return render(request, 'Bootstrap登录页面.html', {'error_msg': error_msg})


def user_list(request):
    # 每一页数据
    per_page = 10
    all_data = models.UserInfo.objects.all().count()
    # 所有页数
    all_page = divmod(all_data, per_page)
    all_page = all_page[0] + 1 if all_page[1] else all_page[0]
    # 如果前台返回数据类型有误默认为1，如果大于在以后一个，返回最后一页
    try:
        page_num = int(request.GET.get('page'))
        if page_num > all_page:
            page_num = all_page
    except Exception:
        page_num = 1
    # 所有的数据数量
    max_page = 11
    half_page = max_page // 2
    if page_num - half_page < 1:
        page_start = 1
    else:
        page_start = page_num - half_page
    page_end = page_num + half_page + 1
    if page_end >= all_page:
        page_start = all_page - max_page + 1
        page_end = all_page
    else:
        page_end = page_num + half_page
    list_ = []
    if page_num > 1:
        list_.append(f'<li><a href="/user_list/?page={page_num - 1}" aria-label="Previous">&laquo</a></li>')
    else:
        list_.append('<li class="disabled"><a href="#" aria-label="Previous">&laquo</a></li>')
    for i in range(page_start, page_end + 1):
        if i == page_num:
            list_.append(f'<li class="active"><a href="/user_list/?page={i}">{i}</a></li>')
        else:
            list_.append(f'<li><a href="/user_list/?page={i}">{i}</a></li>')
    if page_num < all_page:
        list_.append(f'<li><a href="/user_list/?page={page_num + 1}" aria-label="Next">&raquo;</a></li>')
    else:
        list_.append('<li class="disabled"><a href="#" aria-label="Next">&raquo;</a></li>')
    page_list = ''.join(list_)
    ret = models.UserInfo.objects.all()[(page_num - 1) * 10:page_num * 10]
    return render(request, 'user_list.html', {'user_list': ret,
                                              'page_list': page_list,
                                              'page_num': page_num,
                                              'page_start': page_start,
                                              'page_end': page_end})


def add_user(request):
    if request.method == 'POST':
        new_name = request.POST.get('username', None)
        models.UserInfo.objects.create(name=new_name)
        return redirect('/user_list/')
    return render(request, 'add_user.html')
