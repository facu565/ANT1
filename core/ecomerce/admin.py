from django.contrib import admin
from.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'product_category']



admin.site.register(Product, ProductAdmin)