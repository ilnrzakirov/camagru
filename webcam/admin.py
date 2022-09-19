from django.contrib import admin

# Register your models here.
from webcam.models import ImageFilter, Post, Picture


class PostAdmin(admin.ModelAdmin):
    fields = ["user", "pub_date", "comment", "image"]

admin.site.register(ImageFilter)
admin.site.register(Post)
admin.site.register(Picture)