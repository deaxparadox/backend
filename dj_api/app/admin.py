from django.contrib import admin

from .models import (
    Musician,
    Album,
    Person,
)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass 

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass 

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    raw_id_fields = ["artist"]
