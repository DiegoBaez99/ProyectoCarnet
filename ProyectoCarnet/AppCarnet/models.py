from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GrupoSanguineo(models.Model):
    grupo = models.CharField(max_length=3)

class Direcciones(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    piso = models.CharField(max_length=25)
    altura = models.CharField(blank=True, null=True, max_length=20)

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=25, null=False)


class Persona(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(primary_key=True)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=70)
    grupo_s = models.ForeignKey(GrupoSanguineo, on_delete=models.PROTECT)
    donante = models.BooleanField()
    nacimiento = models.DateField()
    """nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT, null=True)"""
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE, blank=True, null=True)

    
    

class TipoCarnet(models.Model):
    tipo = models.CharField(max_length=4)

class Carnet(models.Model):
    n_carnet = models.IntegerField()
    foto = models.ImageField()
    otorgamiento = models.DateField()
    vencimiento = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_carnet = models.ForeignKey(TipoCarnet, on_delete=models.PROTECT)
    donante = models.BooleanField(default=False)
    grupo_s = models.ForeignKey(GrupoSanguineo, on_delete=models.PROTECT, null=True)


class Usuario(User):
    user = models.OneToOneField(User, parent_link= True, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona, on_delete = models.CASCADE)
    n_carnet = models.OneToOneField(Carnet, on_delete=models.CASCADE)


class Marca(models.Model):
    nombre = models.CharField(max_length=45)

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=45)
    año = models.DateField()

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

class TipoSeguro(models.Model):
    nombre = models.CharField(max_length=30)

class Seguro(models.Model):
    nombre = models.CharField(max_length=50)
    num_poliza = models.IntegerField(max_length=30)
    tel = models.IntegerField(max_length=15)
    tel_emergencia = models.IntegerField(max_length=15)
    tipo = models.ForeignKey(TipoSeguro, on_delete=models.PROTECT)    

class Cedula(models.Model):
    num_cedula = models.CharField(max_length= 45)
    patente = models.CharField(max_length= 15)
    nombre_registro = models.CharField(max_length= 45)
    num_motor = models.IntegerField()
    vehiculo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    num_chasis = models.IntegerField()
    emision = models.DateField()
    vencimiento = models.DateField()
    seguro = models.ForeignKey(Seguro, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)






