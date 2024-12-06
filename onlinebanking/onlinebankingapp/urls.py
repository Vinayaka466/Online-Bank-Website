from django.contrib import admin
from django.urls import path
from.views import Home,Cantact_User,succuess
from .views import register, login_view, account_view,logout,registration_success,deposit,withdraw,bill_payment,payment_success,payment_failed,transfer,edit_account

urlpatterns = [
    path('', Home, name='home'),
    path('cantact', Cantact_User, name='cantact'),
    path('succuess',succuess,name ='succuess'),
    path('register/', register, name='register'),
    path('registration_success',registration_success,name='registration_success'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
    path('logout',logout,name = 'logout'),
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
    path('bill_payment',bill_payment,name='bill_payment'),
    path('payment_success',payment_success,name='payment_success'),
    path('payment_failed',payment_failed,name='payment_failed'),
    path('transfer',transfer,name='transfer'),
    path('edit_account',edit_account,name='edit_account'),
    
    
  
         # Example view for the homepage
]