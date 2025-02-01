from django.db import models

# Create your models here.

class mobile(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=10000)
    stock = models.CharField(max_length=100)
    manufacture_date = models.DateField()
    def __str__(self):
        return f"{self.name}{self.brand}"