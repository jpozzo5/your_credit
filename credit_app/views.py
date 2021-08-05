from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db import *
from .models import *
from django.views.generic import TemplateView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.views.generic import ListView, View




"""
    Clase permite mostrar el listado de creditos.
"""
class CreditView(TemplateView):
    template_name = 'credit.html'
    success_url = '../'

    def get(self, request, *args, **kwargs):
        credit_list = Credit.objects.filter()
        return render(request, 'credit.html', {'credit_list': credit_list})

"""
    Clase Que permite Realizar la creacion de un nuevo credito.
"""
class RegisterCreditView(TemplateView):
    template_name = 'form_credit.html'
    success_url = '../'

    def get(self, request, *args, **kwargs):
        form = CreditForm() 
        return render(request, 'form_credit.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = CreditForm(request.POST) # Bound form
        error = None
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
        else:
            error = 'Ha ocurrido un error'
        print(error)
        return HttpResponseRedirect('/credit')


"""
    Esta clase lo que realiza es despachar una informacion confirmado si el credito fue 
    eliminado.
    Ojo :Mediante ajax se realizan Peticiones a este metodo POST.
"""

class DeleteCreditAjax(View):
    def post(self, request, *args, **kwargs):
        credit_id = request.POST['credit_id']
        msj = None
        if credit_id:
            for id in credit_id:
                Credit.objects.filter(id=id).delete()
            msj ="Operacion Exitosa"
        else:
            msj ="Ha ocurrido un error!"
        data = {'msj':msj}

        return JsonResponse(data)

#---------------------------------------------------------



"""
    Clase permite mostrar el listado de Bancos.
"""
class BankView(TemplateView):
    template_name = 'bank.html'
    success_url = '../'

    def get(self, request, *args, **kwargs):
        bank_list = Bank.objects.filter()
        return render(request, 'bank.html', {'bank_list': bank_list})

"""
    Clase Que permite Realizar la creacion de un nuevo Banco.
"""
class RegisterBankView(TemplateView):
    template_name = 'form_bank.html'
    success_url = '../'

    def get(self, request, *args, **kwargs):
        form = BankForm() 
        return render(request, 'form_bank.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = BankForm(request.POST) # Bound form
        error = None
        if form.is_valid():
            new_customer = form.save() # Guardar los datos en la base de datos
        else:
            error = 'Ha ocurrido un error'

        return HttpResponseRedirect('/bank')



"""
    Esta clase lo que realiza es despachar una informacion confirmado si el banco fue 
    eliminado.
    Ojo :Mediante ajax se realizan Peticiones a este metodo POST.
"""

class DeleteBankAjax(View):
    def post(self, request, *args, **kwargs):
        bank_id = request.POST['bank_id']
        msj = None
        if bank_id:
            for id in bank_id:
                Bank.objects.filter(id=id).delete()
            msj ="Operacion Exitosa"
        else:
            msj ="Ha ocurrido un error!"
        data = {'msj':msj}

        return JsonResponse(data)




#----------------------------------------------------


class HomeView(TemplateView):
    template_name = 'home.html'
    success_url = '../'

    def get(self, request, *args, **kwargs):
        customer_list = Customer.objects.filter()
        return render(request, 'home.html', {'customer_list': customer_list})

class RegisterView(TemplateView):
    template_name = 'form_customer.html'
    success_url = '../'

    def get(self, request, *args, **kwargs):
        form = CustomerForm() 
        return render(request, 'form_customer.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST) # Bound form
        error = None
        if form.is_valid():
            new_customer = form.save() # Guardar los datos en la base de datos
        else:
            error = 'Ha ocurrido un error'

        return HttpResponseRedirect('/home')


class DeleteCustomerAjax(View):
    def post(self, request, *args, **kwargs):
        customer_id = request.POST['customer_id']
        msj = None
        if customer_id:
            for id in customer_id:
                Customer.objects.filter(id=id).delete()
            msj ="Operacion Exitosa"
        else:
            msj ="Ha ocurrido un error!"
        data = {'msj':msj}

        return JsonResponse(data)

      
class HomeUpdateView(UpdateView):
    model = Customer
    template_name = 'update_customer.html'
    form_class = CustomerForm
    success_url = '/home'


class BankUpdateView(UpdateView):
    model = Bank
    template_name = 'update_bank.html'
    form_class = BankForm
    success_url = '/bank'

class CreditUpdateView(UpdateView):
    model = Credit
    template_name = 'update_credit.html'
    form_class = CreditForm
    success_url = '/home'
  