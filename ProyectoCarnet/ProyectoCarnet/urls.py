"""ProyectoCarnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCarnet import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from AppCarnet.views import Home, CrearCarnet, Index, DatosPersonales, CrearCedula, ValidarCarnets, ValidarCarnet
from AppCarnet.forms import UsuarioForm, DireccionForm


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/',views.login,  name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('carnet/', CrearCarnet.as_view(), name='carnet'),
    path('cedula/', CrearCedula.as_view(), name='cedula'),
    path('datos-personales/', DatosPersonales.as_view([UsuarioForm, DireccionForm]), name='datos-personales'),
    path('validar-carnets/', ValidarCarnets.as_view(), name='validar-carnets'),
    path('validar-carnets/<int:pk>/', ValidarCarnet.as_view(), name='validar-carnet'),
    path('done/', DatosPersonales.as_view(), name='done'),
    path('validated_carnet', views.validated_carnet, name='validated_carnet'),
    path('admin/', admin.site.urls),
    path('ajax/cargar_modelos/', views.cargar_modelos, name='ajax_cargar_modelos'),  
    path('index/', Index.as_view(), name='index'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'), name='password_reset_complete'),
    path('mostrar/', views.mostrar, name = 'mostrar'),
    path('mostrar_cedula/', views.mostrar_cedula , name = 'mostrar_cedula'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)