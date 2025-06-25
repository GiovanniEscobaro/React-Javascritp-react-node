from django import forms

class CreateNewTaskForms(forms.Form):
    titulo=forms.CharField(label='Titulo de tarea',max_length=200)
    descripcion=forms.CharField(label='Descripcion de la tarea',widget=forms.Textarea, required=False)
class CrearProyectoForms(forms.Form):
    Nombre=forms.CharField(label='Nombre del proyecto',max_length=200)
