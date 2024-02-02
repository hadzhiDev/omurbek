from rest_framework import serializers

from core.models import Photo, Resource, StartEndTime, Group, Lesson


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class ResourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class StartEndTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = StartEndTime
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
