from django.contrib.auth.hashers import make_password
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from store.models.customer import customer
from django.views import View



class Signup(View):
    def get(self, request) :
        return render(request,'signup.html')
    def post(self, request) : 

        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
       
        Customer =customer(first_name=firstname,last_name=lastname,email=email,password=password1)

        self.warn = {'state' : False, "message" : None }

        if password1 != password2 : 
            self.warn['state'] , self.warn['message']= True ,"Password Doesn't Match"  
            return render(request,'signup.html',self.warn)

        
        elif Customer.customer_exist() :
            self.warn['state'] , self.warn['message']=  Customer.customer_exist()  ,"User Already Exists  " 
            return render(request,'signup.html',self.warn)

        else :
            Customer.password = make_password(password1)
            Customer.register()
            return redirect('home-store')

