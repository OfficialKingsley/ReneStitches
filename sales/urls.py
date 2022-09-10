from django.urls import path
from . import views

app_name = "sales"
urlpatterns = [
    path("add-to-cart/<str:id>", views.add_to_cart, name="add-to-cart"),
    path("update-cart/<str:id>", views.update_cart, name="update-cart"),
    path(
        "delete-cart-item/<str:id>",
        views.delete_cart_item,
        name="delete-cart-item",
    ),
    path("cart", views.cart, name="cart"),
    path("orders", views.orders, name="orders"),
    path("orders/<str:id>/", views.specific_order),
]
