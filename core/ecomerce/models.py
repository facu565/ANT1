from django.db import models

# Create your models here.
Product_status = [
    ('S', 'Stock'),
    ('NS', 'No Stock'),
]

Category = [
    ('S', 'vehicles'),
    ('VF', 'Estate'),
    ('SC', 'Technology'),
    ('SC', 'Tools'),
    ('SC', 'Home Appliances'),
    ('SC', 'Construction'),
    ('SC', 'Sports'),
    ('SC', 'Toys'),
    ('SC', 'Fashion'),
    ('SC', 'Services'),


]

class Product (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    status = models.CharField(max_length=2, choices=Product_status, default='Stock')
    #quantity = models.IntegerField(length=200)
    product_category = models.CharField(max_length=2, choices=Category, default='Service')


class Supplier(models.Model):
    name =  models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)

