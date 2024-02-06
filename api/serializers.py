from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from core.models import Photo, Resource, StartEndTime, Group, DailyLesson, ScientificWork, Lesson, Topic


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


class DailyLessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyLesson
        fields = '__all__'


class ScientificWorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScientificWork
        fields = '__all__'


class TopicForCreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name', 'pdf',)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    topics = TopicForCreateLessonSerializer(many=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CreateLessonSerializer(WritableNestedModelSerializer):
    topics = TopicForCreateLessonSerializer(many=True)

    class Meta:
        model = Lesson
        fields = '__all__'

    def create(self, validated_data):
        topics = validated_data.pop('topics', [])
        lesson = super().create(validated_data)
        for topic in topics:
            Topic.objects.create(lesson=lesson, **topic)
        return lesson





