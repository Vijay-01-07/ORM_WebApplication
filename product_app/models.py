from django.db import models
from django.contrib import admin
# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=20, help_text="Enter Student Name")
    phone_number = models.IntegerField(help_text="Enter Phone Number")
    address = models.CharField(max_length=50, help_text="Enter Address")
    order_no = models.IntegerField(help_text="Enter the Order Number")

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone_number', 'address', 'order_no']
