from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante

from .forms import EstudiantesForm, RegistroForm

from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, "estudiantes/index.html")

def listar_estudiante(request):
    estudiantes = Estudiante.objects.all()
    context = {
        "estudiantes" : estudiantes
    }
    return render(request, "estudiantes/listar.html", context)

def agregar_estudiante(request):
    data = {
        "form" : EstudiantesForm()
    }
    if request.method == "POST":
        formulario = EstudiantesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
    return render(request, "estudiantes/agregar.html", data)



def editar_estudiante(request,id):
    estudiante = get_object_or_404(Estudiante,pk = id)

    data = {
        "form" : EstudiantesForm(instance = estudiante)
    }

    if request.method == "POST":
        formulario = EstudiantesForm(data=request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_estudiante')
        data["form"] = formulario

    return render(request, "estudiantes/editar.html", data)

def eliminar_estudiante(request,id):
    estudiante = get_object_or_404(Estudiante,pk = id)
    estudiante.delete()
    return redirect(to='listar_estudiante')