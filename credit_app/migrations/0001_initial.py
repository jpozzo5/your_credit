# Generated by Django 3.0.10 on 2021-08-04 16:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('type_bank', models.CharField(choices=[('Priv', 'Privado'), ('Public', 'Gobierno')], default='Priv', max_length=15)),
                ('address', models.CharField(max_length=200, verbose_name='Direcciónd')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('age', models.IntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(99)])),
                ('nation', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección de Habitación')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre y Apellido')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electrónico')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Número telefónico')),
                ('type_person', models.CharField(choices=[('N-', 'Natural'), ('J-', 'Júridico')], default='N-', max_length=15)),
                ('bank', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='credit_app.Bank')),
            ],
        ),
    ]
