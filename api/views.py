from rest_framework.viewsets import ModelViewSet

from core.models import Photo, Resource, StartEndTime, Group, DailyLesson, ScientificWork, Lesson, Topic
from api.serializers import (PhotoSerializers, ResourceSerializers, StartEndTimeSerializers, GroupSerializers,
                             DailyLessonSerializers, ScientificWorkSerializers, TopicForCreateLessonSerializer,
                             LessonSerializer, CreateLessonSerializer, TopicSerializer, DailyLessonReadSerializers,
                             CreateStartEndTimeSerializers)
from api.paginations import SimpleResultPagination
from api.mixins import SerializeByActionMixin


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class StartEndTimeViewSet(SerializeByActionMixin, ModelViewSet):
    queryset = StartEndTime.objects.all()
    serializer_classes = {
        'list': StartEndTimeSerializers,
        'update': CreateStartEndTimeSerializers,
        'create': CreateStartEndTimeSerializers,
        'retrieve': StartEndTimeSerializers,
    }
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class DailyLessonViewSet(ModelViewSet):
    queryset = DailyLesson.objects.all()
    serializer_class = DailyLessonSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class ScientificWorkViewSet(ModelViewSet):
    queryset = ScientificWork.objects.all()
    serializer_class = ScientificWorkSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class LessonViewSet(SerializeByActionMixin, ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_classes = {
        'list': LessonSerializer,
        'update': CreateLessonSerializer,
        'create': CreateLessonSerializer,
        'retrieve': LessonSerializer,
    }
    # serializer_class = CreateLessonSerializer
    pagination_class = SimpleResultPagination
    lookup_field = 'id'