from django.contrib.admin import ModelAdmin, register

from djangoprojectjfobatista.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('title',)}
