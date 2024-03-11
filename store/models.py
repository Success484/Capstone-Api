from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=False)
    
    def __str__(self):
        return self.name
    

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name