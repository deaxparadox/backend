from django.contrib import admin

from .models import Fruit, Color

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass 

@admin.register(Color)
class FruitAdmin(admin.ModelAdmin):
    pass 