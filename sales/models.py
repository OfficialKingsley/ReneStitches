# from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from product.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} - Cart"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    @property
    def total_price(self):
        if self.product.discount > 0:
            return (
                float(self.product.price)
                * float(1 - self.product.discount)
                * float(self.quantity)
            )
        else:
            return self.product.price * self.quantity

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    price = models.FloatField()
    details = models.TextField()
    CHOICES = [
        ("pending", "Pending"),
        ("failed", "Failed"),
        ("success", "Success"),
    ]
    state = models.CharField(
        choices=CHOICES,
        default=CHOICES[0][0],
        max_length=100,
    )
