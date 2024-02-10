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


class DailyLessonReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyLesson
        exclude = ('start_end_time',)


class DailyLessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyLesson
        fields = ['science', 'day_of_week', 'group']


class StartEndTimeSerializers(WritableNestedModelSerializer):
    lessons = DailyLessonReadSerializers(many=True)

    class Meta:
        model = StartEndTime
        fields = '__all__'


class CreateStartEndTimeSerializers(WritableNestedModelSerializer):
    lessons = DailyLessonSerializers(many=True)

    class Meta:
        model = StartEndTime
        fields = '__all__'

    def validate(self, attrs):
        for i in range(len(attrs['lessons'])):
            for j in range(len(attrs['lessons'])):
                if i != j and attrs['lessons'][i]['day_of_week'] == attrs['lessons'][j]['day_of_week']:
                    raise Exception(
                        'вы не можете добавить один урок в один и тот же день и в одно и то же время'
                    )

        return attrs


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
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





