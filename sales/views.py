import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from product.models import Product
from django.contrib.auth.decorators import login_required
from renestitches.utilities.forms import CartItemUpdate
from sales.models import Cart, CartItem, Order


# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login")
def add_to_cart(request, id):
    user = request.user
    cart = Cart.objects.get(user=user)
    product = Product.objects.get(id=id)
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        cart_item = CartItem.objects.create(
            product=product,
            quantity=quantity,
            cart=cart,
        )
        cart_item.save()
        return redirect("products:all-products")
    else:
        context = {
            "cart": cart,
            "product": product,
        }
        return render(request, "sales/add-to-cart.html", context)


@login_required(login_url="/users/login")
def cart(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    cart_length = CartItem.objects.filter(cart=cart).count()
    context = {
        "cart_items": cart_items,
        "cart_length": cart_length,
    }
    return render(request, "sales/cart.html", context)


@login_required(login_url="/users/login")
def update_cart(request, id):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_item = CartItem.objects.get(id=id)
    cart_length = CartItem.objects.filter(cart=cart).count()
    if request.method == "POST":
        form = CartItemUpdate(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect("sales:cart")
    else:
        form = CartItemUpdate(None, instance=cart_item)
        context = {
            "cart_item": cart_item,
            "form": form,
            "cart_length": cart_length,
        }
        return render(request, "sales/update-cart.html", context)


@login_required(login_url="/users/login")
def delete_cart_item(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect("sales:cart")


@login_required(login_url="/users/login")
def orders(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == "POST":
        price = 0
        details = []
        encoder = json.JSONEncoder()
        if cart_items.count() >= 1:
            for cart_item in cart_items:
                price += cart_item.total_price
                details.append(
                    {
                        "Product": f"{cart_item.product.name}",
                        "Quantity": cart_item.quantity,
                        "Price Paid": cart_item.total_price,
                    }
                )
                cart_item.delete()
        else:
            return redirect("sales:cart")
        details = encoder.encode(details)
        order = Order(user=user, price=price, details=details)
        order.save()
        return redirect("sales:orders")
    else:
        orders = Order.objects.filter(user=user)
        context = {"orders": orders}
        return render(request, "sales/orders.html", context)


@login_required(login_url="/users/login")
def specific_order(request, id):
    order = Order.objects.get(id=id)
    # context = {"order": order}
    decoder = json.JSONDecoder()
    data = {
        "id": order.id,
        "user": order.user.username,
        "price": order.price,
        "state": order.state,
        "details": decoder.decode(order.details),
    }

    return JsonResponse(data)
