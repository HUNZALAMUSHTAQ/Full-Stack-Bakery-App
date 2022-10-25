from django.contrib import admin
from django.urls import path
from  .views.store_home import Home
from .views.signup import Signup
from .views.sigin import Signin , Logout
from .views.cart import Cart
from .views.order import OrderView
from .views.checkout import Checkout
from store.middleware.auth import auth_middleware
admin.autodiscover()


urlpatterns = [
    path('',Home.as_view(),name='home-store'),
    path('signup',Signup.as_view(),name='signup'),
    path('signin',Signin.as_view(),name='signin'),
    path('logout',Logout.as_view(),name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('order/',auth_middleware(OrderView.as_view()),name='order'),
    path('checkout',Checkout.as_view(),name='checkout')


]