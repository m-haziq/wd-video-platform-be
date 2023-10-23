from django.contrib import admin
from django.utils.safestring import mark_safe
from api.v1.videos.models import Video, Tag


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags_name', 'url']
    list_filter = ('tags', 'title')
    search_fields = ['title', 'tags__name']

    def tags_name(self, obj):
        tag_list = [tag.name for tag in obj.tags.all()]
        tag_names = "<br>".join(tag_list)
        return mark_safe(tag_names)

    tags_name.short_description = 'Tag Names'


admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
