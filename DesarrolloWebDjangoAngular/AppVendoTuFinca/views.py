# from django.shortcuts import render
# from AppVendoTuFinca.models import Fincas
# from django.http import JsonResponse

# # Create your views here.
# def finca_list(request):
#     fincas=Fincas.objects.all()
#     datafincas={
#         'fincas':list(fincas.values())
#     }
#     return JsonResponse(datafincas)
# def finca_detalle(request, id):
#     fincafiltroId=Fincas.objects.get(pk=id)
#     datafincas={
#         'direccion':fincafiltroId.direccion_finca,
#         'pais': fincafiltroId.pais_finca,
#         'descripcion': fincafiltroId.descripcion_finca,
#         'Imagen': fincafiltroId.imagen_finca,
#         'activo':fincafiltroId.active_finca
#     }
#     return JsonResponse(datafincas)
    
    
