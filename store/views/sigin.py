
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,redirect
from store.models.customer import customer
from django.views import View
from django.contrib.auth.hashers import make_password ,check_password


class Signin(View):
    return_url = None 
    
    def get(self,request):
        Signin.return_url = request.GET.get('return_url')
        return render(request,'signin.html')
    def post(self,request):
        self.error = {'state' : False , 'message' : None}
        self.email = request.POST.get('email')
        self.password = request.POST.get('password')
        Customer = customer.customer_by_email(self.email)
       

        if Customer :
            flag=check_password(self.password,Customer.password)
            print(flag)
            if flag:
                request.session['customer'] = Customer.id

                if Signin.return_url:
                    return HttpResponseRedirect(Signin.return_url)
                else :
                    Signin.return_url= None
                    return redirect('home-store')
            else :
                self.error['state'] , self.error['message']=True ,'Password is not valid'

        else:
            self.error['state'] , self.error['message']=True ,'Email Password is not valid'
        return render(request,'signin.html',self.error)


class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect('signin')