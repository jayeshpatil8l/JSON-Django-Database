from django.db import models

# Create your models here.
class Receipt(models.Model):
    receipt_no = models.CharField(max_length=10, primary_key = True)
    date = models.CharField(max_length=15)

class Item(models.Model):
    qty = models.IntegerField(default=1)
    description = models.TextField(null = False, blank = False)
    unit_price = models.DecimalField(max_digits = 11, decimal_places = 2)
    amount = models.DecimalField(max_digits = 11, decimal_places = 2)

class Customer(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    address = models.TextField(null = True, blank = True)
