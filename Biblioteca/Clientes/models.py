from django.db import models

# Create your models here.

class Clientes(models.Model):

    name = models.CharField(max_length=50, help_text='Escriba su nombre')
    telephone = models.CharField(max_length=10, help_text='Ingrese su numero de teléfono')
    sexo= models.CharField(max_length=1, help_text= 'Ingrese cual es su sexo (F)(M)')
    fechanacimiento = models.DateField()
