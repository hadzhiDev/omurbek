from django.urls import path, include

from . import views
from .yasg import urlpatterns as url_doc

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('photos', views.PhotoViewSet)
router.register('resources', views.ResourceViewSet)
router.register('startendtime', views.StartEndTimeViewSet)
router.register('groups', views.GroupViewSet)
router.register('daily_lessons', views.DailyLessonViewSet)
router.register('scientific_works', views.ScientificWorkViewSet)
router.register('lessons', views.LessonViewSet)


urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += url_doc
