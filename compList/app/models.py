from django.db import models
# Create your models here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

INDUSTRY_CHOICES = (
    ("Account", "Account"),
    ("IT", "IT"),
    ("Sales", "Sales"),
    ("Health Care", "Health Care"),
)

class companyDetails(models.Model):
    Company_Name = models.CharField(max_length=200)
    Company_Website = models.CharField(max_length=400)
    Company_Phone_Number = models.CharField(max_length=20)
    Company_Address = models.CharField(max_length=200)
    Company_City = models.CharField(max_length=200)
    Company_State = models.CharField(max_length=200)
    Company_Country = models.CharField(max_length=100)
    Industry_List = models.CharField(max_length=30, choices=INDUSTRY_CHOICES, null=False)

    def __str__(self):
        return self.Company_Name

    class Meta:
        ordering = ['Company_Name']    

# Company_Name = name,Company_Website = website,Company_Phone_Number = phone,Company_Address = address,Company_City = city,Company_State = state,Company_Country = country,Industry_List = industry