from django.db import models

# Create your models here.


"""class GrupoSanguineo(models.Model):
    grupo = models.CharField(max_length=3)


class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=25)

class Persona(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(max_length=10)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=70)
    grupo_s = models.ForeignKey(GrupoSanguineo, on_delete=models.PROTECT)
    donante = models.BooleanField()
    nacimiento = models.DateField()


class TipoCarnet(models.Model):
    tipo = models.CharField(max_length=4)

class Carnet(models.Model):
    n_carnet = models.IntegerField()
    foto = models.ImageField()
    otorgamiento = models.DateField()
    vencimiento = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_carnet = models.ForeignKey(TipoCarnet, on_delete=models.PROTECT)


class Usuario(models.Model):
    nickname = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    n_carnet = models.ForeignKey(Carnet, on_delete=models.CASCADE)


class Marca(models.Model):
    nombre = models.CharField(max_length=45)

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=45)
    año = models.DateField()

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

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
    tipo = models.ForeignKey(TipoVehiculo)


class TipoSeguro(models.Model):
    nombre = models.CharField(max_length=30)

class Seguro(models.Model):
    nombre = models.CharField(max_length=50)
    num_poliza = models.IntegerField(max_length=30)
    tel = models.IntegerField(max_length=15)
    tel_emergencia = models.IntegerField(max_length=15)
    tipo = models.ForeignKey(TipoSeguro, on_delete=models.PROTECT)
"""
