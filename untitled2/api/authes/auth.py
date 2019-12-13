from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

class MicroAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.Token.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code':1004,'error':'验证失败'})
        return (obj.user.username,obj.token)