from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.forms import ModelForm
from credit_app.models import *
import os
import json

class CustomerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Customer
        fields = "__all__"

class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = "__all__"

class CreditForm(forms.ModelForm):
    
    class Meta:
        model = Credit
        fields = "__all__"


        