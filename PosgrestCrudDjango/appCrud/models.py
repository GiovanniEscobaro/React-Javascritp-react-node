from django.db import models

# Create your models here.
class Todo(models.Model):
    
    title= models.CharField(max_length=50),
    desciption=models.TextField(blank=True)

