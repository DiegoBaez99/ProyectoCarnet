from .models import Direcciones
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from user.models import Usuario

class cargarDireccion(forms.ModelForm):
    class Meta:
        model = Direcciones
        fields = ('nombre', 'numero', 'piso', 'altura')


class cargarPersona(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'dni', 'nacimiento')
    

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email',error_messages={'exists': 'This already exists!'})

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
        return self.cleaned_data['email']
