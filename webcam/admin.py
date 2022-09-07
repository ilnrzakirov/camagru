from django.contrib import admin

# Register your models here.
from webcam.models import ImageFilter, Post, Picture

admin.site.register(ImageFilter)
admin.site.register(Post)
admin.site.register(Picture)