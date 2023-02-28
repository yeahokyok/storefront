from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=6, decimal_places=2)


class Collection(models.Model):
    title = models.CharField(max_length=255)

    # If you’d prefer Django not to create a backwards relation,
    # set related_name to '+' or end it with '+'
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    inventory = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    promotions = models.ManyToManyField(Promotion, related_name="products")

    def __str__(self):
        return self.title


class Customer(models.Model):

    MEMBERSHIP_CHOICES = (("B", "Bronze"), ("S", "Silver"), ("G", "Gold"))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default="B")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
