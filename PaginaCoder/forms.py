from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=40)
    camada = forms.IntegerField(min_value=1000)

class BuscandoCursoForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=40)

class EstudiantesForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=20)
    apellido = forms.CharField(min_length=4, max_length=20)

class ProfesoresForm(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=20)
    apellido = forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField(min_length=4, max_length=20)


