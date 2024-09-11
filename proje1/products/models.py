from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    prod_img=models.ImageField(upload_to='userimg/',blank=True,null=True)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='liked',blank=True,null=True)
    carts=models.ManyToManyField(User,related_name='carted',blank=True,null=True)

    def __str__(self):
        return self.product_name
