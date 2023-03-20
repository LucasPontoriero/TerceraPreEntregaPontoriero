
from django.shortcuts import render, redirect
from PaginaCoder.models import Curso, Estudiantes
from PaginaCoder.forms import CursoForm, BuscandoCursoForm, EstudiantesForm

# Create your views here.
def buscando_curso(request):
    mi_formulario = BuscandoCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }
        return render(request,"PaginaCoder/buscando_curso.html", context=context)

def curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_guardar = Curso(
                nombre=informacion['nombre'],
                 camada = informacion['camada'])
            curso_guardar.save()




    todos_cursos = Curso.objects.all()
    context = {
        "cursos": todos_cursos,
        "form": CursoForm(),
        "form_buscar": BuscandoCursoForm()
    }
    return render(request, "PaginaCoder/cursos.html", context=context)

def crear_curso(request, nombre, camada):
    guardar_curso =Curso(nombre=nombre, camada=int(camada))
    guardar_curso.save()
    context = {
        "nombre": nombre
    }
    return render (request, "PaginaCoder/guardar_curso.html",context=context)


def estudiantes(request):
    if request.method == "POST":
        mi_formulario1 = EstudiantesForm(request.POST)
        if mi_formulario1.is_valid():
            informacion1 = mi_formulario1.cleaned_data
            estudiantes_guardar = Estudiantes(
                nombre=informacion1['nombre'],
                apellido=informacion1['apellido'])
            estudiantes_guardar.save()

    todos_estudiantes = Estudiantes.objects.all()
    context = {
        "estudiantes": todos_estudiantes,
        "form": EstudiantesForm(),

    }

    return render(request, "PaginaCoder/Estudiantes.html", context=context)

def guardar_estudiante(request, nombre, apellido):
    guardar_estudiante =Estudiantes(nombre=nombre, apellido=(apellido))
    guardar_estudiante.save()
    context = {
        "nombre": nombre,
        "apellido": apellido
    }
    return render (request, "PaginaCoder/Estudiantes.html",context=context)


def profesores(request):
    return render(request, "base.html")