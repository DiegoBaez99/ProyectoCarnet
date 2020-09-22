from .models import Direcciones, Carnet, GrupoSanguineo,TipoCarnet,Marca,Modelo,TipoUso,Seguro, Cedula
from user.models import Usuario
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class cargarDireccion(forms.ModelForm):
    class Meta:
        model = Direcciones
        fields = ('nombre', 'numero', 'piso', 'altura')


class cargarPersona(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'dni', 'nacimiento')


class CarnetForm(forms.ModelForm):
    otorgamiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Carnet
        fields = ['n_carnet', 'foto', 'donante', 'otorgamiento', 'vencimiento', 'grupo_s', 'tipo_carnet']
        labels = {
            'n_carnet': "Ingrese el numero de carnet",
            'foto': "Ingrese una foto del carnet",
            'donante': "¿Es donante?",
            'otorgamiento': "Ingrese la fecha de otorgamiento",
            'vencimiento': "Ingrese la fecha de vencimiento",
            'grupo_s': "Ingrese seu grupo sanguineo",
            'tipo_carnet': "Ingrese su tipo de carnet",
        }
        
    
class CustomUserCreationForm(forms.Form):     
    

    username = forms.CharField(label='Nombre de Usuario', min_length=4, max_length=35, widget=forms.TextInput)
    email = forms.EmailField(label='Email',widget=forms.TextInput)
    password1 = forms.CharField(label='Ingrese una contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = Usuario.objects.filter(username=username)
        if r.count():
            raise  ValidationError(f"{username} ya existe.Pruebe otro nombre de usuario")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Usuario.objects.filter(email=email)
        if r.count():
            raise  ValidationError(f"{email} ya esta registrado. Pruebe con otro email.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        user = Usuario.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class CedulaForm(forms.ModelForm):
    emision = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Cedula
        fields = ['num_cedula', 'patente', 'marca', 'modelo', 'uso', 'num_motor', 'num_chasis', 'emision', 'vencimiento', 'seguro']

        labels = {
            'num_cedula': "Ingrese el numero de cedula",
            'patente': "Ingrese la patente",
            'marca': "Seleccione la marca",
            'modelo': "Seleccione el modelo",
            'uso': "Seleccione el uso",
            'num_motor': "Ingrese el numero de motor",
            'num_chasis': "Ingrese el numero de chasis",
            'emision': "Ingrese la fecha de emision",
            'vencimiento': "Ingrese el vencimiento",
            'seguro': "Seleccione el seguro"
        }


class SeguroForm(forms.ModelForm):
    nombre=forms.ModelChoiceField(queryset=Seguro.objects.all())
    emision = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tipo_uso=forms.ModelChoiceField(queryset=TipoUso.objects.all())
    class Meta:
       model = Seguro
       fields = ['nombre', 'num_poliza', 'emision', 'vencimiento','tel', 'tel_emergencia', 'tipo_uso']
     
       labels = {
           'nombre': "Ingrese el nombre del seguro",
           'num_poliza': "Ingrese el numero de poliza",
           'emision': "Ingrese la fecha de emision",
           'vencimiento': "Ingrese el vencimiento",
           'tel': "Ingrese un numero de teléfono",
           'tel_emergencia': "Ingrese un numero de teléfono de emergencia",
           'tipo_uso': "Ingrese tipo de uso",
           
       }

