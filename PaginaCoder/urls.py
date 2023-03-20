
from django.urls import path
from PaginaCoder.views import *

urlpatterns = [
    path('curso', curso, name="PaginaCoderCursos"),
    path('buscando_curso', buscando_curso, name="PaginaCoderBuscandoCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name="PaginaCoderCurso"),
    path('estudiantes', estudiantes, name="PaginaCoderEstudiantes"),
    path('profesores', profesores, name="PaginaCoderProfesores")

]