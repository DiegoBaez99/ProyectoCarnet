from django.contrib import admin
from .models import *
from user.models import Usuario

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
    pass
class MarcaAdmin(admin.ModelAdmin):
    pass
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio')
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