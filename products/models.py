from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, max_length=50)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    description = models.TextField()
    value = models.CharField(max_length=120)
    price = models.FloatField()
    rating = models.FloatField()
    count = models.IntegerField()
    country_of_origin = models.CharField(max_length=50)
    Quality = models.CharField(max_length=50)
    Check = models.CharField(max_length=50)
    Min_weight = models.IntegerField()
    Featured_products = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


