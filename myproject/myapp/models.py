from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=15)

class Category(models.Model):
    cat_name=models.CharField(max_length=255, verbose_name='Category')
    cat_desc=models.CharField(max_length=255, verbose_name='Category Description')
    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    brand=models.CharField(max_length=255, null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.name
