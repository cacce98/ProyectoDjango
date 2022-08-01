from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from msilib import sequence
from django.contrib import admin
from .models import Alumnos, ComentarioContacto
from .models import Comentario


# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','update')
    list_display = ('matricula', 'nombre', 'carrera','turno','created')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="usuarios").exists():
            return('matricula', 'carrera', 'turno')
        else:
            return('created','update')

admin.site.register(Alumnos, AdministrarModelo)

class AdComentarios(admin.ModelAdmin):
    readonly_fields = ('created','id')
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'

admin.site.register(Comentario, AdComentarios)
class AdComentariocontactos(admin.ModelAdmin):
    readonly_fields = ('created','id')
    ist_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'

admin.site.register(ComentarioContacto, AdComentariocontactos)

class AdministrarMdelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')

    list_per_page=2 
    list_display_links=('matricula','nombre')
    list_editable=('turno',)