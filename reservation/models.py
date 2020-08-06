from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class register(models.Model):
    username = models.CharField(db_column='username' ,max_length=45 ,blank=True, null=True)
    password = models.CharField(db_column='password' ,max_length=45 ,blank=True, null=True)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.username
