from django.db import models
from django_countries.fields import CountryField
# Create your models here.
from fontawesome_5.fields import IconField

class RoomType(models.Model):
   name  = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self):
      return self.name
   

class Customer(models.Model):
   first_name = models.CharField(max_length=100)
   last_name =  models.CharField(max_length=100)
   email = models.EmailField(blank=True)
   phone  = models.CharField(max_length=12)
   address =  models.CharField(max_length=100)
   nationality  =  CountryField(blank=True)
   date_of_birth  = models.DateField(blank=True)
   
   def __str__(self) -> str:
      return self.first_name + ' '+ self.last_name
   
   
class Room(models.Model):
   room_number = models.CharField(max_length=100)
   room_type = models.ForeignKey("RoomType",on_delete=models.SET_NULL, null=True)
   price = models.FloatField()
   number_of_bed = models.IntegerField()
   service = models.TextField()
   status = models.BooleanField(default=False)
   
   def __str__(self) -> str:
      return self.room_number
   
   
class Book(models.Model):
   customer = models.ForeignKey("Customer", verbose_name=("Customer Name"), on_delete=models.CASCADE)
   room =  models.ForeignKey("Room", on_delete=models.SET_NULL, null=True)
   date = models.DateTimeField(auto_now=True)
   check_in = models.DateField()
   check_out = models.DateField(blank=True)
   status = models.BooleanField(default=True)
   
   def __str__(self) -> str:
      return 'name {0} room {1}'.format(self.customer, self.room)
   

class Service(models.Model):
   name = models.CharField(max_length=100)
   icon = IconField()
   description  = models.CharField(max_length=30)
   def __str__(self) -> str:
      return self.name
   
   
      
      

      
   
      
      

   