from django.contrib import admin

# Register your models here.

from .models import Grocery

@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'description', 'price', 'stock', 'expiry_date')