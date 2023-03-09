from django.contrib import admin
import typing 

from .models import Image 

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display: typing.Sequence[str] = ["title", "slug", "image", "created"]
    list_fitler = ['created']