from django.db import models

#https://docs.djangoproject.com/en/2.0/ref/models/fields

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)




