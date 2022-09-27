from django.contrib import admin

from webcam.models import ImageFilter, Post, Picture


class PostAdmin(admin.ModelAdmin):
    fields = ["user", "pub_date", "comment", "image"]
    search_fields = ["user"]
    list_display = ["user", "image"]
    filter_horizontal = ["comment"]


class PictureAdmin(admin.ModelAdmin):
    fields = ["title", "img"]
    search_fields = ["title"]
    list_display = ["title"]


admin.site.register(ImageFilter)
admin.site.register(Post, PostAdmin)
admin.site.register(Picture, PictureAdmin)
