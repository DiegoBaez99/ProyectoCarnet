from django.contrib import admin
from .models import *
from user.models import Usuario

def validar_carnet(modeladmin, request, queryset):
        queryset.update(validado=True)
validar_carnet.short_description = 'Validar Carnet Seleccionado'

def invalidar_carnet(modeladmin, request, queryset):
        queryset.update(validado=False)
invalidar_carnet.short_description = 'Invalidar Carnet Seleccionado'

# Register your models here.
class GrupoSanguineoAdmin(admin.ModelAdmin):
    ordering = ('grupo', )
    
class DireccionesAdmin(admin.ModelAdmin):
    pass
class NacionalidadAdmin(admin.ModelAdmin):
    pass
class TipoCarnetAdmin(admin.ModelAdmin):
    pass
class CarnetAdmin(admin.ModelAdmin):
    
    def titular(self):
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.carnet_id == self.n_carnet:
                return f'{usuario.last_name} {usuario.first_name}'.upper()

        
    list_display = ('n_carnet', titular,'validado', 'tipo_carnet', 'otorgamiento', 'vencimiento')
    actions = [validar_carnet, invalidar_carnet]


class MarcaAdmin(admin.ModelAdmin):
    pass
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo')
class TipoVehiculoAdmin(admin.ModelAdmin):
    pass
class TipoSeguroAdmin(admin.ModelAdmin):
    pass
class TipoUsoAdmin(admin.ModelAdmin):
    pass
class SeguroAdmin(admin.ModelAdmin):
    list_display = ('num_poliza', 'nombre', 'tel', 'tel_emergencia')
class CedulaAdmin(admin.ModelAdmin):
    pass





admin.site.register(GrupoSanguineo, GrupoSanguineoAdmin)
admin.site.register(Direcciones, DireccionesAdmin)
admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(TipoCarnet, TipoCarnetAdmin)
admin.site.register(Carnet, CarnetAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
admin.site.register(TipoUso, TipoUsoAdmin)
admin.site.register(Seguro, SeguroAdmin)
admin.site.register(Cedula, CedulaAdmin)