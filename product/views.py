from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.contrib.auth.mixins import LoginRequiredMixin
from sales.models import Cart, CartItem
from .models import Product


# Create your views here.
class AllProductsView(View):
    def get(self, request):
        product_list = Product.objects.all()
        paginator = Paginator(product_list, 8)
        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {
            "products": products,
        }
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_length = CartItem.objects.filter(cart=cart).count()
            context["cart_length"] = cart_length
        return render(request, "products/all-products.html", context)
