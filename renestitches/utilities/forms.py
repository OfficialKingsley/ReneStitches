from django import forms
from sales.models import CartItem

# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from product.models import Product


class CartItemUpdate(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ["quantity"]

    widgets = {
        "quantity": forms.NumberInput(
            attrs={
                "class": "form-control",
            },
        )
    }


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))


class RegisterForm(UserCreationForm):
    pass
