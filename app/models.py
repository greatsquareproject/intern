from django.db import models
from datetime import datetime

# Create your models here.
class seller(models.Model):
    Companyname = models.CharField(max_length=250, default="Construct")
    address = models.CharField(max_length=150, default="Madurai")
    phone = models.IntegerField(default='+91 9900809781')
    date = models.DateField(default=datetime.now)

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    purchase_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


class products(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name