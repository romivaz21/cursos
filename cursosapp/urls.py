from django.urls import path
from . import views

urlpatterns = [
     path('', views.pagina_principal, name='pagina_principal'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesor/<int:pk>/', views.detalle_profesor, name='detalle_profesor'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiante/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:pk>/', views.detalle_curso, name='detalle_curso'),
    path('insertar_profesor/', views.insertar_profesor, name='insertar_profesor'),
    path('insertar_estudiante/', views.insertar_estudiante, name='insertar_estudiante'),
    path('insertar_curso/', views.insertar_curso, name='insertar_curso'),     
    path('cursos/buscar/', views.buscar_cursos, name='buscar_cursos'), 
]