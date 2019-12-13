from rest_framework.views import APIView
from rest_framework.response import Response
from api.authes import auth
from ..models import UserInfo,Token
import uuid
class LoginView(APIView):
    # versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000,  'err':''}
        print(request.data)
        user = UserInfo.objects.filter(**request.data)
        if user:
            token =str(uuid.uuid4())
            Token.objects.update_or_create(user=user.first(),defaults={'token':token})
            ret = {'code': 1000, 'token':token}
        else:
            ret = {'code': 1001,'err':'用户名或密码错误'}
        return Response(ret)


class MicroView(APIView):
    authentication_classes = [auth.MicroAuth]
    def get(self, request, *args, **kwargs):
        ret = {'code': 1000,  'title':'微职位'}
        return Response(ret)