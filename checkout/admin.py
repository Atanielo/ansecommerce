from django.contrib import admin

# Register your models here.
from .models import CartItem, CartItemManager



class CartItemAdmin(admin.ModelAdmin):
    search_fields = ('product', 'quantity','price')
    list_display = ('product', 'quantity','price')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug','created')
    list_display = ('name', 'slug','created')


admin.site.register(CartItem, CartItemAdmin)

