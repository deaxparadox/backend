from django.contrib import admin
from typing import Sequence 

from .models import Profile 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = ('user', 'date_of_birth', 'photo')
    raw_id_fields: Sequence[str] = ['user']