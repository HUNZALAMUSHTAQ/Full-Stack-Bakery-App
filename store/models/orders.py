from django.db import  models
from .product import Products
from .customer import customer
import datetime
class Order(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    Customer= models.ForeignKey(customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    address = models.CharField(max_length=50, default='', blank=True)
    date =  models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False)
    
    def placeorder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(Customer= customer_id).order_by('-date')