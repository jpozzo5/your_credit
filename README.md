Proyecto Pokemon V0.1 DjangoRest
Autor:Jesus pozzo
# ![Django DRF Example App](django_pokemon.png)

## Instalación

1. En el proyecto existe un archivo requirements.txt el cual contiene todas las dependencias necesarias para este proyecto para instalarlas en un entorno virtual pordemos utilziar el comando 
`pip install -r requirements.txt`.

2. La arquitectura de Bases de datos de este proyecto fue armada mediante Posgresql utilizando la libreria psycopg2 la configuracion de la BD : 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_credit',
        'USER': 'jesus',
        'PASSWORD':'pozzo*',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Ahora podemos realizar la migracion de nuestro proyecto para cargar lo modelos y luego poder cargar los recursos `python manage.py migrate`.



## Servicios
1. `home/` muestra un listado de los Clientes `[GET]`.
2. `home/register-customer/`En la vista de cliente existe un formulario el cual nos permitira crear nuevos clientes`[POST]`.
3. `home/DeleteCustomerAjax/` este router realiza una peticion mediante ajax cuando se elimine un cliente `[POST]`. 


4. `bank` Muestra un listado de los Bancos `[GET]`.
5. `bank/register-bank/` En la vista de Bancos existe un formulario el cual nos permitira crear nuevos Bancos`[POST]`
6. `bank/DeleteBankAjax/` Elimina Los bancos`[DELETE]`.

7. `credit/` Este Servicio Muestra el listado de Creditos`[Get]`.
8. `credit/register-credit/` Permite Crear Nuevos Creditos para los clientes`[POST].
9. `credit/DeleteCreditAjax/` Elimina los creditos de los clientes de forma asincrona. `[GET]`.


