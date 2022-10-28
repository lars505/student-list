from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "estudiantes/index.html")

def agregar_estudiante(request):
    return render(request, "estudiantes/agregar.html")

def listar_estudiante(request):
    return render(request, "estudiantes/listar.html")

def editar_estudiante(request,id):
    return render(request, "estudiantes/editar.html")

def eliminar_estudiante(request,id):
    return render(request, "estudiantes/listar.html")

