from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import forms, CustomUserCreationForm, CarnetForm, CedulaForm, UsuarioForm, DireccionForm
from user.models import Usuario, Direcciones, Carnet, Cedula, Marca, Modelo
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,CreateView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from formtools.wizard.views import SessionWizardView
from django.views.decorators.http import require_http_methods




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
            return redirect('personal_info')
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


class CrearCarnet(CreateView):
    model = Carnet
    form_class = CarnetForm
    template_name = 'carnet.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        current_user = self.request.user
        self.object.user_id = current_user.id
        self.object.save()
        current_user.save()
        return HttpResponseRedirect(self.success_url)

class CrearCedula(CreateView):
    model = Cedula
    form_class = CedulaForm
    template_name = 'cedula.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        current_user = self.request.user
        self.object.user_id = current_user.id
        self.object.save()
        current_user.save()
        return HttpResponseRedirect(self.success_url)

def cargar_modelos(request):
    marca_id = request.GET.get('marca')
    modelos = Modelo.objects.filter(marca_id=marca_id).order_by('modelo')
    return render(request, 'modelo_dropdown_list_options.html', {'modelos': modelos})

#Form para cargar datos personales del usuario, como tambien su direccion, multiple form
class DatosPersonales(SessionWizardView):
    form_list = [UsuarioForm, DireccionForm]
    template_name = "personal_info.html"
    
    def done(self, form_list, **kwargs):
        forms = iter(form_list)
        form_user = next(forms)
        current_user = self.request.user #obtenemos el usuario logueado actualmente
        user = form_user.save(commit=False) #False para no guardar todavia los dats en la db 
        #asignamos manualmente cada uno de los campos del modelo Usuario
        current_user.first_name = user.first_name
        current_user.last_name = user.last_name
        current_user.dni = user.dni
        current_user.nacimiento = user.nacimiento
        current_user.phone = user.phone
        current_user.nacionalidad = user.nacionalidad
    
        form_address = next(forms)
        address = form_address.save() #guardamos los datos del form direccion
        current_user.direccion_id = address.id #mandamos el id del form direcc a user
        current_user.save() #recien ahora guardamos todos los datos del usuario

        return HttpResponseRedirect('/index')

class ValidarCarnets(ListView):
    model = Carnet
    template_name = 'validar-carnets.html'
    context_object_name = 'carnets'
    
class ValidarCarnet(DetailView):
    model = Carnet
    template_name = 'validar-carnet.html'
    def get_context_data(self, *args, **kwargs): 
        context = super(ValidarCarnet, self).get_context_data(*args, **kwargs) 
        # add extra field
        context["carnet"] = Carnet.objects.filter(pk=self.object.pk) 
        return context

@require_http_methods(['POST'])
def validated_carnet(request):
    carnet_id = request.POST['carnet_id'] #obtenemos el id del carnet a traves del input oculto
    carnet = Carnet.objects.get(pk=carnet_id) #obtenemos del modelo el carnet con el id pasado
    if request.POST.get('validar'):
        carnet.validado = True
    else:
        carnet.validado = False
    carnet.save()
    #context = {'validado': True}
    return redirect('validar-carnets')


def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, 'index.html')



def mostrar(request):
    current_user = request.user     
    carnet = Carnet.objects.filter(user_id=current_user.id)
    return render(request, 'mostrar.html',  {'carnet':carnet})

