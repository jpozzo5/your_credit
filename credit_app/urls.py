from django.urls import path
from django.conf.urls import url, include
from credit_app.views import *



urlpatterns = [

    url(r'^home/$', HomeView.as_view(),name ="cliene_view"),
    url(r'^home/register-customer/$', RegisterView.as_view(),name ="customer_reg_view"),
    url(r'^home/DeleteCustomerAjax/$', DeleteCustomerAjax.as_view(),name ="delete_customer"),
    url('home/update/(?P<pk>\d+)/$', HomeUpdateView.as_view(),name='location-update'),

    url(r'^bank/$', BankView.as_view(),name ="bank_view"),
    url(r'^bank/register-bank/$', RegisterBankView.as_view(),name ="bank_reg_view"),
    url(r'^bank/DeleteBankAjax/$', DeleteBankAjax.as_view(),name ="delete_bank"),
    url('bank/update/(?P<pk>\d+)/$', BankUpdateView.as_view(),name='bank-update'),

    url(r'^credit/$', CreditView.as_view(),name ="credit_view"),
    url(r'^credit/register-credit/$', RegisterCreditView.as_view(),name ="credit_reg_view"),
    url(r'^credit/DeleteCreditAjax/$', DeleteCreditAjax.as_view(),name ="delete_bank"),
    

 
]