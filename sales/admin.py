from django.contrib import admin

from sales.models import Cart, CartItem, Order


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    pass


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "total_price", "cart"]
    list_filter = ["cart"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price"]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
