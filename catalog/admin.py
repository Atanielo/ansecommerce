from django.contrib import admin

# Register your models here.

from .models import Category, Product



class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category', 'description', 'price', 'created', 'modified')
    list_display = ('name', 'category', 'description', 'price', 'created', 'modified')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug','created')
    list_display = ('name', 'slug','created')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
