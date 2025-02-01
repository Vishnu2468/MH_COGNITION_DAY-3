from django.db import models

# Create your models here.

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.name}{self.brand}"
