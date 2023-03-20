from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"Curso: {self.nombre}, Camada: {self.camada}"

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"Curso: {self.nombre}, Camada: {self.apellido}"

class Profesor(models.Model):
    email = models.EmailField(null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"