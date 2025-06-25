from django.urls import path
from .views import lista_tareas
urlpatterns=[
    path('',lista_tareas)
]