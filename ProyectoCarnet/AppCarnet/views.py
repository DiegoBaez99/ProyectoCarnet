from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import forms, CustomUserCreationForm, CarnetForm, CedulaForm, UsuarioForm, DireccionForm
from user.models import Usuario, Direcciones, Carnet, Cedula, Marca, Modelo, Nacionalidad
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, FormView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from formtools.wizard.views import SessionWizardView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Sum

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
            return redirect('datos-personales')#url.py
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
    return render(request, 'logout.html')


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
    login_required = True
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
    login_required = True
    model = Carnet
    template_name = 'validar-carnets.html'
    context_object_name = 'carnets'
    queryset = Carnet.objects.exclude(validado=1)
    #paginate_by = 5

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

"""def pie_chart(request):
    labels = []
    data = []

    queryset = Nacionalidad.objects.order_by('nacionalidad')
    for nac in queryset:
        labels.append(nac.nacionalidad)
        data.append(len(Carnet.objects.filter(user_id=nac.id)))

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })"""

def mostrar(request):
    return render(request, 'pie_chart.html')

def population_chart(request):
    labels = []
    data = []

    queryset = Nacionalidad.objects.order_by('nacionalidad')
    for nac in queryset:
        nac.cantidad_carnet = len(Carnet.objects.filter(user_id=nac.id))
        nac.save()
    
    queryset = Nacionalidad.objects.values('nacionalidad').annotate(cantidad_carnet=Sum('cantidad_carnet')).order_by('-cantidad_carnet') 
    for entry in queryset:
        labels.append(entry['nacionalidad'])
        data.append(entry['cantidad_carnet'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, 'index.html')