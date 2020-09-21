from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from AppCarnet.models import Nacionalidad, GrupoSanguineo, Direcciones, Carnet, Cedula
from ProyectoCarnet.settings import MEDIA_URL, STATIC_URL

class Usuario(AbstractUser):
    dni = models.IntegerField(blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    donante = models.BooleanField(default=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, null=True)
    grupo_s = models.ForeignKey(GrupoSanguineo, on_delete=models.CASCADE, null=True)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE, null=True)
    carnet = models.ForeignKey(Carnet, on_delete=models.CASCADE, blank=True, null=True)
    cedula = models.ForeignKey(Cedula, on_delete=models.CASCADE, blank=True, null=True)
    

    def getImage(self):
        if(self.image):
            return f'{MEDIA_URL}{self.image}'
        return '{}{}'.format(STATIC_URL, 'img/empty.png')