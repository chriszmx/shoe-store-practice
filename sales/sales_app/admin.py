from django.contrib import admin
from .models import ShoeInventory, ShoppingCart, CartItem


@admin.register(ShoeInventory)
class ShoeInventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'quantity')
    list_filter = ('brand', 'color')
    search_fields = ('name', 'brand', 'color')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
