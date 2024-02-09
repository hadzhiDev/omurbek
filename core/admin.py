from django.contrib import admin
from django import forms

from core.models import Photo, Resource, Group, StartEndTime, DailyLesson, ScientificWork, Lesson, Topic


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )
    search_fields = ('id', )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at',)


class DailyLessonInline(admin.StackedInline):
    model = DailyLesson
    extra = 1


@admin.register(StartEndTime)
class StartEndTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end')
    list_display_links = ('id', 'start', 'end')
    search_fields = ('id', 'start',)
    inlines = [DailyLessonInline]


# @admin.register(DailyLesson)
# class DailyLessonAdmin(admin.ModelAdmin):
#     list_display = ('id', 'science', 'day_of_week', 'group', 'start_end_time')
#     list_display_links = ('id', 'science', 'group')
#     search_fields = ('id', 'science', 'group')
#     list_filter = ('created_at',)
#     readonly_fields = ('created_at', 'updated_at',)


@admin.register(ScientificWork)
class ScientificWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'title', )
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at',)


class TopicStackedInline(admin.TabularInline):
    model = Topic
    extra = 1


class LessonAdminForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at',)
    inlines = [TopicStackedInline]
    form = LessonAdminForm
