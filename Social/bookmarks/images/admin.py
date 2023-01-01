from django.contrib import admin
from typing import Sequence, Union, Callable, Any

from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display: Sequence = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
