from rest_framework.viewsets import ModelViewSet

from core.models import Photo, Resource
from api.serializers import PhotoSerializers, ResourceSerializers
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