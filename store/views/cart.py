
from django.shortcuts import render ,redirect
from store.models.customer import customer
from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from store.models.product import Products

class Cart(View):
    def get(self,request):
        ids= list(request.session.get('cart').keys())
        product = Products.get_product_by_id(ids)
        print(product)
        return render(request,'cart.html',{'products' : product})


