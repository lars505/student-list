from curses import meta
from dataclasses import field
from statistics import mode
from .models import Estudiante
from django import forms
from django.contrib.auth.forms import UserCreationForm

class EstudiantesForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        # fields = ["correo","nombre","apellidos"]
        fields = "__all__"


class RegistroForm(UserCreationForm):
    pass