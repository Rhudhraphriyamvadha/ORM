# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![FWAD flowchart](https://github.com/user-attachments/assets/3f61e7f0-13dc-4bf1-83f8-80a2ff246059)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
models.py
 from django.db import models
 from django.contrib import admin
 class Bankloan(models.Model):
   name=models.CharField(max_length=100)
   ifsc=models.CharField(max_length=30)
   accno=models.IntegerField(primary_key='accno')
   loanamt=models.IntegerField()
   mobileno=models.IntegerField()

 class BankloanAdmin(admin.ModelAdmin):
   list_display=('name','ifsc','accno','loanamt','mobileno')

admin.py
 from django.contrib import admin
 from.models import Bankloan,BankloanAdmin
 admin.site.register(Bankloan,BankloanAdmin) 
 

## OUTPUT
![FWAD bankloan](https://github.com/user-attachments/assets/e308a4ab-b46d-4241-a846-957adb3ad545)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
