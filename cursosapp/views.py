from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from .models import Profesor, Estudiante, Curso
from .forms import ProfesorForm, CursoForm, EstudianteForm, BusquedaCursoForm

def pagina_principal(request):
    return render(request, 'cursosapp/pagina_principal.html')

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'cursosapp/lista_profesores.html', {'profesores': profesores})

def detalle_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, 'cursosapp/detalle_profesor.html', {'profesor': profesor})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'cursosapp/lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'cursosapp/detalle_estudiante.html', {'estudiante': estudiante})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursosapp/lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursosapp/detalle_curso.html', {'curso': curso})



def insertar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')  # Redirige a la lista de profesores después de guardar
    else:
        form = ProfesorForm()
    return render(request, 'cursosapp/insertar_profesor.html', {'form': form})


def insertar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')  # Redirige a la lista de profesores después de guardar
    else:
        form = EstudianteForm()
    return render(request, 'cursosapp/insertar_estudiante.html', {'form': form})


def insertar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')  # Redirige a la lista de profesores después de guardar
    else:
        form = CursoForm()
    return render(request, 'cursosapp/insertar_curso.html', {'form': form})



def buscar_cursos(request):
    form = BusquedaCursoForm(request.GET or None)
    cursos = []
    if form.is_valid():
        query = form.cleaned_data['query']
        cursos = Curso.objects.filter(nombre__icontains=query)
    
    return render(request, 'cursosapp/buscar_cursos.html', {'form': form, 'cursos': cursos})