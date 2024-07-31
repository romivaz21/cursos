from django import forms
from .models import Profesor,Estudiante, Curso



class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']



class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']     



class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']                 


class BusquedaCursoForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)        