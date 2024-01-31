from django.urls import path, include

from . import views
from .yasg import urlpatterns as url_doc

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('photos', views.PhotoViewSet)
router.register('resources', views.ResourceViewSet)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += url_doc
