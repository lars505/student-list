from unicodedata import name
from django.urls import path    

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('agregar-estudiante', views.agregar_estudiante, name='agregar_estudiante'),
    path('listar-estudiante', views.listar_estudiante, name='listar_estudiante'),
    path('editar-estudiante/<int:id>', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar-estudiante/<int:id>', views.eliminar_estudiante, name='eliminar_estudiante'),

]