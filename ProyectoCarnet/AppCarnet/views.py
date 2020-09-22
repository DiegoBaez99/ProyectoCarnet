from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse, Http404
from .forms import forms, CustomUserCreationForm, cargarDireccion, cargarPersona, CarnetForm, CedulaForm, UsuarioForm
from .models import Direcciones, Carnet, Cedula, Marca, Modelo
from user.models import Usuario
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse


class Home(TemplateView):
    template_name = "home.html"

class Index(TemplateView):
    template_name = "index.html"

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            messages.success(request, 'Cuenta creada satisfactoriamente.')
            return redirect('datos')
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

class CargarUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'datos1.html'
    success_url = reverse_lazy('carnet')


class CrearCarnet(CreateView):
    model = Carnet
    form_class = CarnetForm
    template_name = 'carnet.html'
    success_url = reverse_lazy('home')
  
class CrearCedula(CreateView):
    model = Cedula
    form_class = CedulaForm
    template_name = 'cedula.html'
    success_url = reverse_lazy('home')

def cargar_modelos(request):
    marca_id = request.GET.get('marca')
    modelos = Modelo.objects.filter(marca_id=marca_id).order_by('modelo')
    return render(request, 'modelo_dropdown_list_options.html', {'modelos': modelos})

def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    
    return render(request,'index.html')