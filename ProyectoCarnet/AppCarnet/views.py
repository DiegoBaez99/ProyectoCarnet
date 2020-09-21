from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse, Http404
from .forms import forms, CustomUserCreationForm, cargarDireccion, cargarPersona, CargarCarnet, CargarCedula
from .models import Direcciones
from user.models import Usuario
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            messages.success(request, 'Cuenta creada satisfactoriamente.')
            return redirect('login')
    else:
        f = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': f})

def login(request):
    #Si el usuario ya esta logueado que lo mande a la pag principal
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Error nombre de usuario o contraseña incorrecto.')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def carnet(request):
    if request.method == 'POST':
        f = CargarCarnet(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            messages.success(request, 'Carnet creado satisfactoriamente.')
            return redirect('login')
    else:
        f = CargarCarnet()

    return render(request, 'carnet.html', {'form': f})

def cedula(request):
    if request.method == 'POST':
        f = CargarCedula(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Carnet creado satisfactoriamente.')
            return redirect('login')
    else:
        f = CargarCedula()

    return render(request, 'cedula.html', {'form': f})



def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    
    return render(request,'index.html')