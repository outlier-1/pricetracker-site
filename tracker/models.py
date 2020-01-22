from django.db import models
from accounts.models import User


# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=120)

    class Meta:
        db_table = 'website'


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    property = models.TextField(max_length=250, blank=True)
    current_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    url = models.URLField(max_length=250)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'


class PriceDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'price_detail'


class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'track'