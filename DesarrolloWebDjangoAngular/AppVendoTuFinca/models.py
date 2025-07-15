from django.db import models

# Create your models here.
class Fincas(models.Model):
    direccion_finca=models.CharField(
        max_length=250
        )
    pais_finca=models.CharField(
        max_length=50
        )
    descripcion_finca=models.CharField(
        max_length=500
        )
    imagen_finca=models.CharField(
        max_length=900
        )
    active_finca=models.BooleanField(
        default=True
        )
    def __str__(self):
        return self.direccion_finca
    
        
    
    
