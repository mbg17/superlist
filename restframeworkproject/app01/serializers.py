from rest_framework import serializers
from rest_framework.response import Response
from . import models
class BookSerializers(serializers.Serializer):
    title = serializers.CharField()
    publisher = serializers.CharField(source='publisher.name')

# 接口保存数据序列化类
class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Book
        fields='__all__'
    def create(self, validated_data):
        obj = models.Book.objects.create(title=validated_data['title'],publisher=validated_data['publisher'])
        return obj


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Publisher
        fields='__all__'


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields='__all__'