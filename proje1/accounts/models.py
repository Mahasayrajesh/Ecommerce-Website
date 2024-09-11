from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonDetail(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=200)
    street=models.CharField(max_length=200)
    landmark=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.BigIntegerField()