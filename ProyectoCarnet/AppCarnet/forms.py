from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from user.models import Direcciones, Carnet, GrupoSanguineo, TipoCarnet, Marca, Modelo, TipoUso,Seguro, Cedula, Nacionalidad, Usuario, Seguro
from django.core.exceptions import ValidationError
import re


class CarnetForm(forms.ModelForm):
    CHOICES = (('True', 'Si'),('False', 'No'),)    
    otorgamiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    donante = forms.ChoiceField(choices=CHOICES)
    foto_frente = forms.ImageField(required = False)
    class Meta:
        model = Carnet
        fields = ['n_carnet', 'donante', 'otorgamiento', 'vencimiento', 'grupo_s', 'tipo_carnet','foto_frente']
        labels = {
            'n_carnet': "Ingrese el numero de carnet",            
            'donante': "¿Es donante?",
            'otorgamiento': "Ingrese la fecha de otorgamiento",
            'vencimiento': "Ingrese la fecha de vencimiento",
            'grupo_s': "Ingrese seu grupo sanguineo",
            'tipo_carnet': "Ingrese su tipo de carnet",
            'foto_frente': "Cargue una foto del frente de su carnet",
        }
    
    def clean_n_carnet(self):
        n_carnet = self.cleaned_data['n_carnet']
        comprobation = Carnet.objects.filter(n_carnet=n_carnet)
        if len(comprobation) > 0:
            raise ValidationError(f"El Nro de carnet: {n_carnet} ya existe. Ingrese otro numero de carnet.")
        return n_carnet
    
    def clean_vencimiento(self):
        vencimiento = self.cleaned_data['vencimiento']
        otorgamiento = self.cleaned_data['otorgamiento']
        if vencimiento < otorgamiento:
            raise  ValidationError("La fecha de vencimiento debe ser mayor que la fecha de otorgamiento.")
        return vencimiento


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', min_length=4, max_length=35, widget=forms.TextInput)
    email = forms.EmailField(label='Email',widget=forms.TextInput)
    password1 = forms.CharField(label='Ingrese una contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        comprobation = Usuario.objects.filter(username=username)
        if len(comprobation) > 0:
            raise  ValidationError(f"{username} ya existe. Pruebe otro nombre de usuario")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        comprobation = Usuario.objects.filter(email=email)
        if len(comprobation) > 0:
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


class UsuarioForm(forms.ModelForm):
    nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    nacionalidad = forms.ModelChoiceField(queryset=Nacionalidad.objects.defer('cantidad_carnet'))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'dni', 'nacimiento', 'phone', 'nacionalidad']

        labels = {
            'first_name': "Ingrese su nombre",
            'last_name': "Ingrese su apellido",
            'dni': "Ingrese su DNI:",
            'nacimiento': "Ingrese su fecha de nacimiento:",
            'phone': "Ingrese su numero de telefono",
            'nacionalidad': "Ingrese su nacionalidad:",
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if not re.search('^[a-zA-Z]+(?:[\s.]+[a-zA-Z]+)*$', value):
            raise ValidationError("Solo se aceptan letras.")
        return value
    
    def clean_dni(self):
        dni = self.cleaned_data['dni']
        comprobation = Usuario.objects.filter(dni=dni)
        if len(comprobation) > 0:
            raise ValidationError(f"El DNI: {dni} ya existe. Ingrese otro DNI.")
        return dni


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direcciones
        fields = ['nombre', 'numero', 'piso', 'altura']

        labels = {
            'nombre': "Ingrese el nombre de su calle:",
            'numero': "Ingrese el numero de su calle:",
            'piso': "Ingrese piso:",
            'altura': "Ingrese altura de su direccion:",
        }


class CedulaForm(forms.ModelForm):
    emision = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    foto_frente = forms.ImageField(required = False)
    class Meta:
        model = Cedula
        
        fields = ['num_cedula', 'patente', 'marca', 'modelo', 'uso', 'num_motor', 'num_chasis', 'emision', 'vencimiento','foto_frente']

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
            'foto_frente': "Cargue una foto del frente de su carnet"
        }

    def clean_num_cedula(self):
        num_cedula = self.cleaned_data['num_cedula']
        comprobation = Cedula.objects.filter(num_cedula=num_cedula)
        if len(comprobation) > 0:
            raise  ValidationError(f"{num_cedula} ya esta registrado. Pruebe con otro número de cedula.")
        return num_cedula

    def clean_patente(self):
        patente = self.cleaned_data['patente']
        comprobation = Cedula.objects.filter(patente=patente)
        if len(comprobation) > 0:
            raise  ValidationError(f"La patente: {patente} ya esta registrada. Pruebe con otra patente.")
        return patente
    
    def clean_num_motor(self):
        num_motor = self.cleaned_data['num_motor']
        comprobation = Cedula.objects.filter(num_motor=num_motor)
        if len(comprobation) > 0:
            raise  ValidationError(f"El número de motor: {num_motor} ya esta registrado. Pruebe con otro número de motor.")
        return num_motor
    
    def clean_num_chasis(self):
        num_chasis = self.cleaned_data['num_chasis']
        comprobation = Cedula.objects.filter(num_chasis=num_chasis)
        if len(comprobation) > 0:
            raise  ValidationError(f"El número de chasis: {num_chasis} ya esta registrado. Pruebe con otro número de chasis.")
        return num_chasis

    def clean_vencimiento(self):
        vencimiento = self.cleaned_data['vencimiento']
        emision = self.cleaned_data['emision']
        if vencimiento < emision:
            raise  ValidationError("La fecha de vencimiento debe ser mayor que la fecha de emisión.")
        return vencimiento

    #Funcion para el chained dropdown de Marca-Modelo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelo'].queryset = Modelo.objects.none()

        if 'marca' in self.data:
            try:
                marca_id = int(self.data.get('marca'))
                self.fields['modelo'].queryset = Modelo.objects.filter(marca_id=marca_id).order_by('modelo')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['modelo'].queryset = self.instance.marca.modelo_set.order_by('modelo')

class SeguroForm(forms.ModelForm):
    nombre=forms.ModelChoiceField(queryset=Seguro.objects.all())    
    class Meta:
       model = Seguro
       fields = ['nombre', 'num_poliza','tel', 'tel_emergencia']
     
       labels = {
           'nombre': "Ingrese el nombre del seguro",
           'num_poliza': "Ingrese el numero de poliza",
           'tel': "Ingrese un numero de teléfono",
           'tel_emergencia': "Ingrese un numero de teléfono de emergencia",          
           
       }
