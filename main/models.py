from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    type = models.TextField()
    description = models.TextField()