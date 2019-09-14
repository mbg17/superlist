from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
class test(MiddlewareMixin):
    def process_request(self,request):
        r_path = request.path_info
        ret = request.get_signed_cookie('is_login', default='0', salt='test')
        if r_path !='/login/':
            if ret != '1':
                return redirect(f'/login/?next={r_path}')
            else:
                # 获取当前路径，不包含参数
                return
        else:
            return

    def process_response(self,request,response):
        if request.path_info == '/check/':
            return HttpResponse('不能直接访问')
        else:
            return response