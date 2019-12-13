from rest_framework import serializers
from .models import Course, CourseDetail


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    class Meta:
        model = Course
        fields = ['id','title','level','course_img']

class CourseDetailSerializer(serializers.ModelSerializer):
    title= serializers.CharField(source='course.title')
    course = serializers.CharField(source='course.id')
    level = serializers.CharField(source='course.get_level_display')
    img = serializers.CharField(source='course.course_img')
    # 自定义函数序列化字段
    recommends = serializers.SerializerMethodField('get_recommend_list')
    chapter = serializers.SerializerMethodField('get_course_list')
    class Meta:
        model = CourseDetail
        fields = ['course','title','img','slogan','level','why','recommends','chapter']
    # obj当前表的对象
    def get_recommend_list(self,obj):
        return [{'id':c.id,"title":c.title} for c in obj.recommend.all()]

    def get_course_list(self,obj):
        return [{'id':c.course.id,"name":c.name} for c in obj.course.courselist_set.all()]