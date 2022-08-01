from django.shortcuts import render
from .models import Alumnos, Comentario, ComentarioContacto, Archivos
from .forms import ComentarioContactoForm, FormArchivos
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render(request,'registros/comentarios.html', {'comentarios': comentarios})
    form = ComentarioContactoForm()
    return render(request,'registros/contacto.html',{'form': form})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,'registros/comentarios.html', {'comentarios': comentarios})
    return  render(request, confirmacion, {'object':comentario})

def consultarComentario(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, 'registros/formeditcomentario.html', {'comentario': comentario})

def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, 'registros/formeditcomentario.html', {'comentario':comentario })

def contacto(request):
    return render(request,"registros/contacto.html")

def coment(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(equest):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["juan","ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechainicio = datetime.date(2022, 6, 1)
    fechafin = datetime.date(2022, 7, 14)
    alumnos=Alumnos.objects.filter(created__range=(fechainicio,fechafin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="pruebacomentario")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request,"Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('Select id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, 'registros/seguridad.html',
    {'nombre':nombre})

