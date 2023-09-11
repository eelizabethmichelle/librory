from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    rented = models.IntegerField()
    available = amount - rented
    category = models.TextField()
    description = models.TextField()