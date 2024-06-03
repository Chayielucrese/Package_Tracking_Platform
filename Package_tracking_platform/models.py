from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    

class Warehouse(models.Model):
    country = models.CharField(max_length=100) 
    town = models.CharField(max_length=100)

    def __str__(self):
        return self.country
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Package(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=100, unique=True)
    weight = models.FloatField()
    destination = models.CharField(max_length=100)
    warehousearrival = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            self.tracking_id = uuid.uuid4().hex[:10] #Generating a unique tracking_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tracking_id
    

class PackageMovement(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)


class PackageScan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    