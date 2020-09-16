from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse, Http404
from .forms import forms, CustomUserCreationForm, cargarDireccion, cargarPersona, CargarCarnet
from .models import Direcciones
from user.models import Usuario
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
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
    return render(request,'logout.html')

def carnet(request):
    if request.method == 'POST':
        f = CargarCarnet(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Carnet creado satisfactoriamente.')
            return redirect('login')
    else:
        f = CargarCarnet()

    return render(request, 'carnet.html', {'form': f})


def persona(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        form = cargarPersona()
        if(request.method == 'POST'):
            form = cargarPersona(request.POST)
            if(form.is_valid()):
                person = Usuario(first_name=request.POST.get('first_name', False), last_name=request.POST.get('last_name', False), dni=request.POST.get('dni', False), nacimiento=request.POST.get('nacimiento', False))
                person.save(commit=False)
                messages.success(request, "Datos cargados satisfatoriamente.")
                if(person == None):    
                    messages.info(request, "Datos Incompleto.")
            return redirect('index')
        else:
            form = cargarPersona()

        return render(request, 'datos1.html', {'form': form})

def direccion(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        form = cargarDireccion()
        if(request.method == 'POST'):
            form = cargarDireccion(request.POST)
            if(form.is_valid()):
                #form.save()
                direccion = Direcciones(nombre=request.POST['nombre'], numero=request.POST['numero'], piso=request.POST['piso'], altura=request.POST['altura'])
                direccion.save()
                messages.success(request, "Direccion creada satisfatoriamente.")
            return redirect('index')
        else:
            form = cargarDireccion()

        return render(request, 'direccion.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    
    return render(request,'index.html')