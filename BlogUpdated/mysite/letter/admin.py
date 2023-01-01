from django.contrib import admin
from typing import Sequence, Union, Callable, Any, Mapping

from .models import Letter

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    #  = "__all__"
    list_display: Sequence[Union[str, Callable[[], Any]]] = ["title", "subject", "content", "created", "status"]
    prepopulated_fields: Mapping[str, Sequence[str]] = {"slug": ('subject',)}