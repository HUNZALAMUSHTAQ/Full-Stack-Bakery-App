from django.contrib import admin
from .models.product import Products
from .models.Category import Category
from .models.customer import customer
from .models.orders import Order
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','category','price']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display= ['first_name','email']



admin.site.register(customer,AdminCustomer)
admin.site.register(Products, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order)

