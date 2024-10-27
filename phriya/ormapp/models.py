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



