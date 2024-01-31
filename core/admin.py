from django.contrib import admin

from core.models import Photo, Resource


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