from tkinter import CASCADE
from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    product_name =  models.CharField(max_length=50)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to ='media')

    def __str__(self):
        return self.product_name
    
