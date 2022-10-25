
from django.shortcuts import render ,redirect
from store.models.customer import customer
from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from store.models.orders import Order

class OrderView(View): 

    def post(self,request):
        pass
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer(customer)
        orders = orders.reverse()
        return render(request,'order.html',{'orders' : orders})


