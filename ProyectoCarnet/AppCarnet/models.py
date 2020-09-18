from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GrupoSanguineo(models.Model):
    grupo = models.CharField(max_length=3)
    
    def __str__(self):
        return self.grupo

class Direcciones(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    piso = models.CharField(max_length=25)
    altura = models.CharField(blank=True, null=True, max_length=20)
    def __str__(self):
        return f'{self.nombre} {self.altura} {self.numero} piso: {self.piso}'

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=25, null=False)
    def __str__(self):
        return self.nacionalidad


class TipoCarnet(models.Model):
    tipo = models.CharField(max_length=5)
    def __str__(self):
        return self.tipo

class Carnet(models.Model):
    n_carnet = models.IntegerField(primary_key=True)
    foto = models.ImageField(upload_to='fotos_persona', null=True,blank=True)
    otorgamiento = models.DateField()
    vencimiento = models.DateField()
    tipo_carnet = models.ForeignKey(TipoCarnet, on_delete=models.PROTECT, null=True)
    donante = models.BooleanField(default=False)
    grupo_s = models.ForeignKey(GrupoSanguineo, on_delete=models.PROTECT, null=True)
    validado = models.BooleanField(default=False, blank=True)
    

class Marca(models.Model):
    nombre = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

class TipoUso(models.Model):
    uso = models.CharField(max_length=20)


class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=45)
    anio = models.DateField()
    tipo_v = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, default=True)
    def __str__(self):
        return f'marca: {self.marca}, modelo: {self.modelo}, año: {self.anio}, tipo: {self.tipo_v}'


class Seguro(models.Model):
    nombre = models.CharField(max_length=50)
    num_poliza = models.IntegerField()
    tel = models.IntegerField()
    tel_emergencia = models.IntegerField()
       


class Cedula(models.Model):
    num_cedula = models.CharField(max_length= 45)
    patente = models.CharField(max_length= 15)
    #nombre_registro = models.CharField(max_length= 45) Habria que normalizar
    num_motor = models.IntegerField()
    vehiculo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    num_chasis = models.IntegerField()
    emision = models.DateField()
    vencimiento = models.DateField()
    seguro = models.ForeignKey(Seguro, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)






