from rest_framework import serializers

from core.models import Photo, Resource


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class ResourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'