from django.shortcuts import render

# Create your views here.
tareas=['apreder django','estudiar','clases']
def home(request):
    context={'tareas':tareas}
    return render(request,'todo/home.html',context)
