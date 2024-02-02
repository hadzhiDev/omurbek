from rest_framework.viewsets import ModelViewSet

from core.models import Photo, Resource, StartEndTime, Group, Lesson
from api.serializers import (PhotoSerializers, ResourceSerializers, StartEndTimeSerializers, GroupSerializers,
                             LessonSerializers)
from api.paginations import SimpleResultPagination


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


class StartEndTimeViewSet(ModelViewSet):
    queryset = StartEndTime.objects.all()
    serializer_class = StartEndTimeSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    pagination_class = SimpleResultPagination
    lookup_field = 'id'