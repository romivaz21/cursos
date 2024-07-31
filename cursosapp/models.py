from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    # profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    # estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')

    def __str__(self):
        return self.titulo