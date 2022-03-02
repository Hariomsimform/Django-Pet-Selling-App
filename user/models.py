from tkinter import CASCADE
from django.db import models
from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
from datetime import date

from pymysql import NULL
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.

class user_profile(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.address)
    def __unicode__(self):
        return self.user    


class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_age = models.IntegerField()
    pet_type = models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {} {}'.format(self.pet_name, self.pet_name, self.pet_type)

class Cart(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)  
    buyer_id = models.IntegerField()
    def __str__(self):
        return '{} {}'.format(self.pet_id, self.buyer_id)
      


    # def __unicode__(self):
    #     return self.user
    