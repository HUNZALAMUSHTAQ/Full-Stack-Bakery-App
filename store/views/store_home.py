from django.core.checks import messages
from django.http.request import HttpHeaders
from store.models.Category import Category
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from store.models.product import Products , Category 
from store.models.customer import customer
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart :
             request.session['cart']={}
        self.products=None
        self.categoryID= request.GET.get('category')
        if self.categoryID : 
            self.products = Products.product_by_id(category_id=self.categoryID)
        else:
            self.products=Products.all_products()
        data={"products":self.products,'categories':Category.all_category}
        return  render(request,'index.html',data)

    def post(self , request):
        product = request.POST.get('product')

        remove = request.POST.get('remove')
        cart = request.session.get('cart')
 
        if cart :
            quantity= cart.get(product)
            if quantity :
                if remove :
                    if quantity <= 1 :
                        cart.pop(product)
                    else :
                        cart[product] = quantity-1 

                else:
                    cart[product] = quantity+1
            else : 
                cart[product] = 1 

         
        else : 
            cart ={}
            cart[product] = 1
        request.session['cart'] = cart

  
        return redirect('home-store')


  

