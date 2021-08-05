from django.contrib import admin

from .models import *

@admin.register(Customer)
class ProfileAdmin(admin.ModelAdmin):
    list_display= ['name','email']

@admin.register(Bank)
class Bankdmin(admin.ModelAdmin):
    list_display= ['name']


@admin.register(Credit)
class Creditdmin(admin.ModelAdmin):
    list_display= ['customer','bank','description']