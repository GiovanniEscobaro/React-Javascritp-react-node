from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index' ),
    path('about/', views.about,name='about'),
    path('hello/<str:username>',views.hello,name='hello' ),
    path('Cliente/<int:id>',views.numero,name='cliente' ),
    path('projects/', views.projects,name='proyectos'),
    path('projects/<int:id>', views.project_detail,name='project_detail'),
    path('tareas/', views.tarea,name='tareas'),
    path('create_task/', views.create_task,name='create_task'),
    path('create_projects/', views.create_projects,name='create_projects'),


]