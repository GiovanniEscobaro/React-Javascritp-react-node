from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, tareas
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTaskForms, CrearProyectoForms

# Create your views here.


def index(request):
    titulo = 'Django Curso!!'
    return render(request, "index.html", {
        'title': titulo
    })


def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hola Mund %s</h2>' % username)


def about(request):
    username = 'gescobar50'
    return render(request, "about.html", {
        'username': username
    })


def numero(request, id):
    resultado = id+20254
    return HttpResponse('<h1> Este es tu id: %s </h1>' % resultado)


def projects(request):
    # project=list(project.objects.values())
    projects = Project.objects.all()
    return render(request, "proyecto/projects.html", {
        'projects': projects
    })


def tarea(request):
    tarea = tareas.objects.all()
    return render(request, "tareas/tarea.html", {
        'tareas': tarea
    })


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tareas/create_task.html', {
            'form': CreateNewTaskForms()
        })
    else:
        tareas.objects.create(titulo=request.POST['titulo'],
                              descripcion=request.POST['descripcion'], Project_id=2)
        return redirect('tareas')


def create_projects(request):
    if request.method == 'GET':
        return render(request, 'proyecto/createProyecto.html', {
            'form': CrearProyectoForms()
        })
    else:
        Project.objects.create(nombre=request.POST['Nombre'])
        return redirect('proyectos')
