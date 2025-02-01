from django.db import models

# Create your models here.

class cloths(models.Model):
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    size = models.CharField(max_length=10)
    price = models.CharField(max_length=10000)
    stock = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.brand}{self.category}"