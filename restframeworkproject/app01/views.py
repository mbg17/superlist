from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from . import models
from .serializers import *
# Create your views here.
# 接口展示序列化类
from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination

# 视图方法CBV
class BookView(APIView):
    def get(self, request):
        book_list = models.Book.objects.all()
        bs = BookSerializers(book_list, many=True)
        return Response(bs.data)

    def post(self, request):
        bs = BookModelSerializers(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)


# 基于混合类实现的增删改查
class AuthorView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Author.objects
    serializer_class = AuthorSerializers

    # 获取所有数据
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # 创建一条新的数据
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    queryset = models.Author.objects
    serializer_class = AuthorSerializers

    # 获取单条数据
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # 更新单条数据
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # 删除单条数据
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


from rest_framework import viewsets
from rest_framework import exceptions


# 验证类
class Token():
    def authenticate(self, request):
        status = request.GET.get('token', 0)
        if status:
            return 'luyuan', 'luyuan'
        else:
            raise exceptions.AuthenticationFailed('验证失败')

    def authenticate_header(self, request):
        pass
import datetime
# 每分钟访问不能超过20次
class Time():
    def allow_request(self,request,view):
        time = datetime.datetime.now()
        IP = request.META['REMOTE_ADDR']
        throttle = models.Throttle.objects.get_or_create(IP=IP)[0]
        if throttle.time.strftime('%Y-%m-%d H:%M')==time.strftime('%Y-%m-%d H:%M'):
            throttle.num+=1
        else:
            throttle.time=time
            throttle.num = 1
        throttle.save()
        if throttle.num<=20:
            return True
        else:
            return False

    def wait(self):
        pass
# 基于viewset视图
class AuthorViewSet(viewsets.ModelViewSet):
    # authentication_classes = [Token]
    # throttle_classes = [Time]
    queryset = models.Author.objects
    serializer_class = AuthorSerializers
