from django.contrib import admin

# Register your models here.

from .models import cloths;
@admin.register(cloths)
class clothsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'description','size','price', 'stock')