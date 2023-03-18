from django.http import HttpResponse
from django.shortcuts import render
from PaginaCoder.models import Curso

# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombre="Python",
                  canada=camada)
    curso.save()
    return HttpResponse("usuario creado exitosamente")
