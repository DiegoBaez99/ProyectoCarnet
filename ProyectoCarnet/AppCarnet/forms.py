from .models import Direcciones, Carnet, GrupoSanguineo,TipoCarnet
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



class CargarCarnet(forms.Form):
    n_carnet = forms.IntegerField(label='Ingrese su numero de carnet', required=True)
    foto = forms.ImageField(label='Ingrese una foto de su carnet', required=False)
    donante = forms.BooleanField(required=False)
    otorgamiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    grupo_s = forms.ModelChoiceField(queryset=GrupoSanguineo.objects.all(), label='Ingrese su grupo sanguineo')
    tipo_carnet = forms.ModelChoiceField(queryset=TipoCarnet.objects.all(), label='Ingrese su tipo de carnet')

    def clean_n_carnet(self):
        n_carnet = self.cleaned_data['n_carnet']
        return n_carnet

    def clean_foto(self):
        foto = self.cleaned_data['foto']
        return foto
    
    def clean_otorgamiento(self):
        otorgamiento = self.cleaned_data['otorgamiento']
        return otorgamiento
    
    def clean_vencimiento(self):
        vencimiento = self.cleaned_data['vencimiento']
        return vencimiento
    
    def clean_donante(self):
        donante = self.cleaned_data['donante']
        return donante
    
    def clean_grupo_s(self):
        grupo_s = self.cleaned_data['grupo_s']
        return grupo_s
    
    def clean_tipo_carnet(self):
        tipo_carnet = self.cleaned_data['tipo_carnet']
        return tipo_carnet

    def save(self):
        carn = Carnet(
        n_carnet=self.cleaned_data['n_carnet'],
        foto=self.cleaned_data['foto'],
        otorgamiento=self.cleaned_data['otorgamiento'],
        vencimiento=self.cleaned_data['vencimiento'],
        donante=self.cleaned_data['donante'],
        grupo_s = self.cleaned_data['grupo_s'],
        tipo_carnet = self.cleaned_data['tipo_carnet']
        )
        carn.save()
        return carn
    
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






"""class CreateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email',error_messages={'exists': 'This already exists!'})
    password1 = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']"""
