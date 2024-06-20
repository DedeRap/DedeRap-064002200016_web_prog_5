from django.db import models
from django import forms
from datetime import date




# Create your models here.
class Pengguna(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_1 = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20, help_text='Enter your city')
    state = models.CharField(max_length=20)  # Typically, a CharField is sufficient for state
    zip_code = models.CharField(max_length=7)
    tanggal_join = models.DateField(auto_now=True)

    
    
class Content(models.Model):
    author = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now = True)
    artikel = models.TextField()
    set_view = models.BooleanField(default=False)