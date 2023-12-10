from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)

class Patient(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient')
    profile_Picture=models.ImageField(upload_to="dp/" ,null=True,blank=True)
    address=models.TextField(help_text="line1,city,state,pincode")
class Doctor(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor')
    profile_Picture=models.ImageField(upload_to="dp/" ,null=True,blank=True)
    address=models.TextField(help_text="line1,city,state,pincode")