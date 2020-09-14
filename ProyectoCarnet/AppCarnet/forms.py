from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Direcciones, Persona

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class cargarDireccion(forms.ModelForm):
    class Meta:
        model = Direcciones
        fields = ('nombre', 'numero', 'piso', 'altura')


class cargarPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'dni', 'nacimiento')