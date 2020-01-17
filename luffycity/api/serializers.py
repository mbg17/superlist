from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Course, CourseDetail, Article


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    title = serializers.CharField(source='name')

    class Meta:
        model = Course
        fields = ['id', 'title', 'level', 'course_img']


class CourseDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='course.name')
    course = serializers.CharField(source='course.id')
    level = serializers.CharField(source='course.get_level_display')
    img = serializers.CharField(source='course.course_img')
    # 自定义函数序列化字段
    recommends = serializers.SerializerMethodField('get_recommend_list')
    chapter = serializers.SerializerMethodField('get_course_list')
    teachers = serializers.SerializerMethodField("get_teacher_list")

    class Meta:
        model = CourseDetail
        fields = ['course', 'title', 'img', 'course_slogan', 'level', 'why_study', 'recommends', 'chapter', 'teachers']

    # obj当前表的对象
    def get_recommend_list(self, obj):
        return [{'id': c.id, "title": c.name} for c in obj.recommend_courses.all()]

    def get_course_list(self, obj):
        return [{'id': c.course.id, "name": c.name} for c in obj.course.coursechapters.all()]

    def get_teacher_list(self, obj):
        return [{'id': c.id, "name": c.name, 'role': c.get_role_display()} for c in obj.teachers.all()]


class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    brief = serializers.CharField()
    head_img = serializers.CharField()
    view_num = serializers.IntegerField()
    comment_num = serializers.IntegerField()
    collect_num = serializers.IntegerField()
    article_type_choices = serializers.CharField(source='get_article_type_display')

    class Meta:
        model = Article
        fields = ['id', 'title', 'brief', 'head_img', 'view_num', 'comment_num', 'collect_num', 'article_type_choices']


class ArticleDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField()
    view_num = serializers.IntegerField()
    comment_num = serializers.IntegerField()
    collect_num = serializers.IntegerField()
    article_type_choices = serializers.CharField(source='get_article_type_display')
    comment = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'comment', 'view_num', 'comment_num', 'collect_num', 'article_type_choices']

    def get_comments(self, obj):
        return [{'id': comment.id,
                 'account': comment.account.username,
                 'disagree_number': comment.disagree_number,
                 'agree_number': comment.agree_number,
                 'content': comment.content,
                 'son_comment': [{'id': s.id, 'account': s.account.username, 'content': s.content} for s in
                                 comment.comment_set.all()]
                 } for comment in obj.comment.all() if not comment.p_node]
