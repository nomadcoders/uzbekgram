from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'caption',
        'file',
        'location'
    )

    list_filter = ('location',)

    list_display_links = ('caption', 'location',)

    search_fields = ('location',)


admin.site.register(Image, ImageAdmin)
