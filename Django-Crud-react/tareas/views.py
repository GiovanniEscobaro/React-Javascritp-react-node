from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TareaSerializer
from .models import tarea
# Create your views here.

class TareaView(viewsets.ModelViewSet):
    serializer_class=TareaSerializer
    queryset=tarea.objects.all()
