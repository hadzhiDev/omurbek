from django.contrib import admin

from core.models import Photo, Resource, Group, StartEndTime, Lesson


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


@admin.register(StartEndTime)
class StartEndTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end')
    list_display_links = ('id', 'start', 'end')
    search_fields = ('id', 'start',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'science', 'day_of_week', 'group', 'start_end_time')
    list_display_links = ('id', 'science', 'group')
    search_fields = ('id', 'science', 'group')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at',)