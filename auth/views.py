from django.shortcuts import render, redirect
from sales.models import Cart

# from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from renestitches.utilities.forms import LoginForm


# Create your views here.

sk = "sk_test_51LezrQBo8AuKUfwUb8uUQ4j9AmsecBfvKU5WPsHAOsN8gjlkbF8iz7MpJwVVtjtTjBsGzVt3doOfI0PpZqQzPCaE00gkOUYLtV"
pk = "pk_test_51LezrQBo8AuKUfwUfPgPOk2ckcOvDpBHsvGy4dgvcrrZf9yMrjoaIGj9D8L8H8Vng8yXViQSNDaU2u4krVt9PVkG00i0577tgc"


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next = request.GET.get("next")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            cart = Cart.objects.get_or_create(user=user)
            print(cart, "Created")
            if next:
                return redirect(next)
            else:
                return redirect("products:all-products")
        else:
            return redirect("auth:login")
    else:
        return render(request, "auth/login.html")


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        next = request.GET.get("next")
        foundUser = authenticate(request, username=username)
        if foundUser is None:
            if password1 == password2:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password2,
                )
                user.save()
                if next:
                    return redirect(next)
                else:
                    return redirect("products:all-products")
            else:
                return redirect("auth:register")
        else:
            return redirect("auth:register")
    else:
        return render(request, "auth/register.html")


def logoutUser(request):
    logout(request)
    return redirect("home:index")
