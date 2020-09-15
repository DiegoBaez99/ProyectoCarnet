from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from .forms import forms, CreateUserForm, cargarDireccion, cargarPersona
from .models import Direcciones
from user.models import Usuario

# Create your views here.
# Create your views here.
def signup(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        if(request.method == 'POST'):
            form = CreateUserForm(request.POST)
            if(form.is_valid()):
                new_user = form.save()
                new_user = authenticate(
                    username = form.cleaned_data['username'],
                    password = form.cleaned_data['password1']
                )
                login(request, new_user)
                return redirect('login')
        else:
            form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})

def loginPage(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password) #name q esta en el html
            if(user is not None):
                login(request, user)     
                return redirect('index')
            else:
                messages.info(request, "Nombre de usuario o contraseña incorrecto.")

    context = {}
    return render(request, 'login.html', context)


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
    html = '<html><body><h1> Hola. </h1></body></html>'
    return HttpResponse(html)