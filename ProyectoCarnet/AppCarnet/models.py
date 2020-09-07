from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(max_length=10)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=70)
    grupo_s = models.ForeignKey(GrupoSanguineo, on_delete=models.PROTECT)
    donante = models.BooleanField()
    firma = models.CharField(max_length=50) 

class GrupoSanguineo(models.Model):
    grupo = models.CharField(max_length=3)


class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=25)


class Carnet(models.Model):
    n_carnet = models.IntegerField()
    foto = models.ImageField()
    otorgamiento = models.DateField()
    vencimiento = models.DateField()
    persona = models.OneToOneField()
    tipo_carnet = models.ForeignKey(TipoCarnet, on_delete=models.PROTECT)

class TipoCarnet(models.Model):
    tipo = models.CharField(max_length=4)

class Usuario(models.Model):
    nickname = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    n_carnet = models.ForeignKey(Carnet)
