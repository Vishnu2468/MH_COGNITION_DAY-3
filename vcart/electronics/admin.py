from django.contrib import admin

# Register your models here.

from .models import mobile;
@admin.register(mobile)
class mobileAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'description','price', 'stock', 'manufacture_date')