from django.contrib import admin

from .models import Estudiante

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ["correo","nombre","apellidos","edad"]

admin.site.register(Estudiante, EstudianteAdmin)
