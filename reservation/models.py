from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(db_column='firstname' ,max_length=45 ,blank=True, null=True)
    familyname = models.CharField(db_column='familyname' ,max_length=45 ,blank=True, null=True)
    dateofbirth = models.CharField(db_column='dateofbirth' ,max_length=45 ,blank=True, null=True)
    email = models.CharField(db_column='email',max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'register'

