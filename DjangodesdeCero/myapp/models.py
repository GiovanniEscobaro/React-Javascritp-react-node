from django.db import models

# Create your models here.
class Project(models.Model):
    nombre=models.CharField(
        max_length=200
    )
    def __str__(self):
        return self.nombre
    
class tareas(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    Project=models.ForeignKey(Project, on_delete=models.CASCADE)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.titulo + '-' + self.descripcion