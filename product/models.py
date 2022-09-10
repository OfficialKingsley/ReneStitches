from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    image = models.ImageField(upload_to="images/products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    @property
    def discounted_price(self):
        if self.discount == 0:
            return self.price
        else:
            return float(1 - self.discount) * self.price

    def __str__(self):
        return self.name
