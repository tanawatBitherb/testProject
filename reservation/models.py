from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from .managers import CustomUserManager

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=60)
    datail = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    color = models.CharField(max_length=50)





# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email