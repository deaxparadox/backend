from django.contrib import admin
from .models import Category, Ingredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass 

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass 