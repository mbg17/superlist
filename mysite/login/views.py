from django.shortcuts import HttpResponse, render, redirect
from login import models
from functools import wraps
from .forms import loginForm
# Create your views here.
def check_login(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        ret = request.get_signed_cookie('is_login',default='0',salt='test')
        if ret=='1':
            return func(request,*args,**kwargs)
        else:
            # 获取当前路径，不包含参数
            next = request.path_info
            return redirect(f'/login/?next={next}')
    return inner

def login(request):
    error_msg = ''
    form_obj= loginForm()
    if request.method == 'POST':
        form_obj = loginForm(request.POST)
        print(form_obj.errors)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        next = request.GET.get('next')
        if email == 'luyuan@qq.com' and password == '12345678':
            if next:
                ret = redirect(next)
            else:
                ret = redirect('/add_user/')
            ret.set_signed_cookie('is_login','1',salt='test',max_age = 10)
            return ret
        else:
            error_msg = '登录失败'
    return render(request, 'Bootstrap登录页面.html', {'error_msg': error_msg,'form_obj':form_obj})

@check_login
def user_list(request):
    # 每一页数据
    per_page = 10
    # 所有的数据数量
    all_data = models.UserInfo.objects.all().count()
    page_num = request.GET.get('page',1)
    from utils.mypage import Pagination
    # 所有页数
    # 如果前台返回数据类型有误默认为1，如果大于在以后一个，返回最后一页
    # try:
    #     page_num = int(request.GET.get('page'))
    #     if page_num > all_page:
    #         page_num = all_page
    # except Exception:
    #     page_num = 1
    # # 最大分页数量
    # max_page = 11
    # # 一半的页数
    # half_page = max_page // 2
    # # 判断当前页数减去一半页数是否小于0
    # if page_num - half_page < 1:
    #     page_start = 1
    # else:
    #     page_start = page_num - half_page
    # page_end = page_num + half_page + 1
    # # 判断末尾页数是都大于总页数
    # if page_end >= all_page:
    #     page_start = all_page - max_page + 1
    #     page_end = all_page
    # else:
    #     page_end = page_num + half_page
    # list_ = []
    # # 拼接HTML
    # if page_num > 1:
    #     list_.append(f'<li><a href="/user_list/?page={page_num - 1}" aria-label="Previous">&laquo</a></li>')
    # else:
    #     list_.append('<li class="disabled"><a href="#" aria-label="Previous">&laquo</a></li>')
    # for i in range(page_start, page_end + 1):
    #     if i == page_num:
    #         list_.append(f'<li class="active"><a href="/user_list/?page={i}">{i}</a></li>')
    #     else:
    #         list_.append(f'<li><a href="/user_list/?page={i}">{i}</a></li>')
    # if page_num < all_page:
    #     list_.append(f'<li><a href="/user_list/?page={page_num + 1}" aria-label="Next">&raquo;</a></li>')
    # else:
    #     list_.append('<li class="disabled"><a href="#" aria-label="Next">&raquo;</a></li>')
    # page_list = ''.join(list_)
    page = Pagination(page_num,all_data,'/user_list/')
    ret = models.UserInfo.objects.all()[page.start:page.end]
    return render(request, 'user_list.html', {'user_list': ret,
                                              'page_list': page.page_html(),
                                              'all_page':page.all_page})

@check_login
def add_user(request):
    if request.method == 'POST':
        new_name = request.POST.get('username', None)
        models.UserInfo.objects.create(name=new_name)
        return redirect('/user_list/')
    return render(request,'add_user.html')

def check(request):
    user = request.POST.get('user')
    ret = models.UserInfo.objects.filter(name=user)
    print(ret)
    if ret:
        return HttpResponse('用户名已存在')
    else:
        return HttpResponse('通过验证')

def form_test(request):
    form_ = loginForm()
    if request.method == 'POST':
        form_ = loginForm(request.POST)
        print(form_.errors)
    return render(request,'form_test.html',{'form_obj':form_})