from django.shortcuts import render
from django.views import View
from product.models import Product

from sales.models import Cart, CartItem


# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {}
        products = Product.objects.all()[:8]
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_length = CartItem.objects.filter(cart=cart).count()
            context = {
                "products": products,
                "cart_length": cart_length,
            }
        else:
            context = {
                "products": products,
            }
        return render(request, "home/index.html", context)


class AboutView(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_length = CartItem.objects.filter(cart=cart).count()
            context = {
                "cart_length": cart_length,
            }

        return render(request, "home/about.html", context)


class ContactUsView(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_length = CartItem.objects.filter(cart=cart).count()
            context = {
                "cart_length": cart_length,
            }
        return render(request, "home/contact.html", context)
