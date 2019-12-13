from rest_framework.views import APIView,Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from api.serializers import CourseSerializer,CourseDetailSerializer
from rest_framework import serializers
from api.models import Course,CourseDetail

# Create your views here.
class CourseView(ModelViewSet):
    # versioning_class = URLPathVersioning
    # queryset = Course.objects
    # serializer_class = CourseSerializer
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000,  'data':''}
        try:
            queryset = Course.objects.all()
            serializer = CourseSerializer(queryset, many=True)
            ret['data']=serializer.data
        except Exception as e:
            ret = {'code': 1001, 'data': '数据不正确'}
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': {}}
        try:
            queryset = CourseDetail.objects.all().filter(course_id=kwargs['pk']).first()
            data=CourseDetailSerializer(queryset, many=False)
            ret['data']=data.data
        except Exception as e:
            ret = {'code': 1001, 'data': '数据不正确'}
        return Response(ret)




