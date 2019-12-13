from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
import re
class rbac(MiddlewareMixin):
    def process_request(self, request):
        white_url = ['/login/','/admin/.*']
        current_path = request.path_info
        for white in white_url:
            if re.match(white,current_path):
                return None
        user = request.session.get('user_id')
        if not user:
            return redirect('/login/')
        # flag=False
        # permission_list = request.session.get('permissions_list')
        # for permission in permission_list:
        #     ret = re.match(f'^{permission}$',current_path)
        #     if ret:
        #         flag= True
        #         break
        # if flag:
        #     return None
        permission_dict = request.session.get('permission_dict')
        for item in permission_dict.values():
            urls = item['urls']
            for url in urls:
                ret = re.match(f'^{url}$',current_path)
                if ret:
                    request.action=item['actions']
                    return None
        return HttpResponse('无权访问')
