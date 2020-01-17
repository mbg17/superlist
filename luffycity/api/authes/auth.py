from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

class MicroAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserAuthToken.objects.get(id=2)
        if not obj:
            raise AuthenticationFailed({'code':1004,'error':'验证失败'})
        return (obj.user,obj.token)