from msilib import sequence
from django.contrib import admin
from .models import Alumnos

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','update')
    list_display = ('matricula', 'nombre', 'carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')


admin.site.register(Alumnos, AdministrarModelo)
