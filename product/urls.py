from django.urls import path
from .views import AllProductsView

app_name = "products"
urlpatterns = [
    path("", AllProductsView.as_view(), name="all-products"),
]
