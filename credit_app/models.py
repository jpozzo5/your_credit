from django.db import models
from django.core.validators import (
    MaxLengthValidator, MaxValueValidator, MinLengthValidator,
    MinValueValidator,
    EmailValidator,
    DecimalValidator
)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal

def value_positive(value):
    if not isinstance(value, int) or (value < 1):
        raise ValidationError(
            _('%(value)s El valor no puede ser negativo y debe ser entero'),
            params={'value': value},
        )

class Bank(models.Model):
    type = [
        ('Priv', 'Privado'),
        ('Public', 'Gobierno'),

    ]
    name = models.CharField('Nombre', max_length=100)
    type_bank= models.CharField(
        max_length=15,
        choices=type,
        default='Priv',
    )
    address = models.CharField('Direcciónd', max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


# Create your models here.
class Customer(models.Model):
    Type = [
        ('N-', 'Natural'),
        ('J-', 'Júridico'),

    ]
    birthday = models.DateField()
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)])
    nation = models.CharField('Nacionalidad', max_length=50)
    address = models.CharField('Dirección de Habitación', max_length=200)
    name = models.CharField('Nombre y Apellido', max_length=100)
    email = models.EmailField('Correo electrónico', max_length=255, unique=True,validators=[EmailValidator()])
    phone_number = models.CharField('Número telefónico', max_length=20, )
    type_person= models.CharField(
        max_length=15,
        choices=Type,
        default='N-',
    )
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE ,null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.name)




class Credit(models.Model):
    tipo = [
        ('1', 'Automotriz'),
        ('2', 'Hipotecarios'),
        ('3', 'Comerciales'),

    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    description = models.CharField('descripción', max_length=300)
    pay_min = models.DecimalField('Pago Mínimo', decimal_places=2, max_digits=8, default=Decimal('0.00'))
    pay_max = models.DecimalField('Pago Maximo',decimal_places=2, max_digits=8, default=Decimal('0.00'))
    plazo = models.IntegerField(validators=[value_positive])
    birthday = models.DateField(null=True, blank=True)
    type_credit = models.CharField(
        max_length=15,
        choices=tipo,
        default='1',
    )
    address = models.CharField('Dirección', max_length=200)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE ,null=True, blank=True, default=None)


    def __str__(self):
        return '{}'.format(self.customer.name)

