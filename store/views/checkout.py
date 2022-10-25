
from django.shortcuts import render ,redirect
from store.models.customer import customer as Customer
from django.views import View
from django.contrib.auth.hashers import make_password ,check_password
from store.models.product import Products
from store.models.orders import Order

class Checkout(View):

    def post(self,request):
        address = request.POST.get('address')
        print('address ',address)
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        list_keys=list(cart.keys())
        products = Products.get_product_by_id(list_keys)
        if not customer :
            return redirect('signin')

        for product in products:
            print('id ddd d ',address)
            order = Order(Customer = Customer(id = customer) ,
            product = product,
            price = product.price,
            address = address ,
            quantity = cart.get(str(product.id)))

            order.placeorder()
        request.session['cart'] = {}
        return redirect ('cart')


