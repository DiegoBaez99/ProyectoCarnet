from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GrupoSanguineo(models.Model):
    grupo = models.CharField(max_length=3)


class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=30)

class Direcciones(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    altura = models.IntegerField()

class TipoCarnet(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)

class Carnet(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(primary_key=True)
    n_carnet = models.IntegerField()
    foto = models.ImageField()
    otorgamiento = models.DateField()
    vencimiento = models.DateField()
    nacimiento = models.DateField()
    donacion = models.BooleanField(default=True)
    validado = models.BooleanField(default=False)
    tipo_carnet = models.ForeignKey(TipoCarnet, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    grupo_sanguineo = models.ForeignKey(GrupoSanguineo, on_delete=models.CASCADE)

class Marca(models.Model):
    nombre = models.CharField(max_length=45)

class Modelo(models.Model):
    modelo = models.CharField(max_length=45)
    anio = models.DateField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

class TipoSeguro(models.Model):
    nombre = models.CharField(max_length=30)

class Seguro(models.Model):
    nombre = models.CharField(max_length=50)
    num_poliza = models.IntegerField()
    tel = models.IntegerField()
    tel_emergencia = models.IntegerField()
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


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carnet = models.OneToOneField(Carnet, on_delete=models.CASCADE)
    #cedula = models.ForeignKey(Cedula, on_delete=models.CASCADE)






   







