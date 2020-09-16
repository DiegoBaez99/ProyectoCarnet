from django.contrib import admin
from user.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('dni', 'first_name', 'last_name','validado' ,'grupo_s', 'nacimiento',)
    list_filter = ('validado', 'grupo_s',)
    search_fields = ('dni', 'first_name', 'last_name',)
    


admin.site.register(Usuario, UsuarioAdmin)