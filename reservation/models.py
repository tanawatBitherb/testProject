from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    product_name = models.CharField(max_length=60)
    datail = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

