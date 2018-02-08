from django.contrib import admin
from .models import Image, Comment, Like


class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'caption',
        'file',
        'location',
        'created_by'
    )

    list_filter = ('location',)

    list_display_links = ('caption', 'location',)

    search_fields = ('location',)


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'comment',
        'created_at',
        'created_for',
        'created_by',
    )


class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'created_for',
        'created_by',
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
