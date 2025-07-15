from rest_framework.response import Response
from AppVendoTuFinca.models import Fincas
from  AppVendoTuFinca.api.serializers import FincaSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def finca_list(request):
    if request.method == 'GET':
        fincas=Fincas.objects.all()
        serializer_finca=FincaSerializer(fincas,many=True)
        return Response(serializer_finca.data)
 
    if request.method == 'POST':
        de_serializer=FincaSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)
        
@api_view(['GET','PUT', 'DELETE'])
def finca_detalle(request,id):
    if request.method== 'GET':
        try:
            finca=Fincas.objects.get(pk=id)
            serializar_finca=FincaSerializer(finca)
            return Response(serializar_finca.data)

        except Fincas.DoesNotExist:
            return Response({'Error': 'La finca no existe'}, status=status.HTTP_404_NOT_FOUND)
                
    if request.method=='PUT':
        finca=Fincas.objects.get(pk=id)
        de_serializer=FincaSerializer(finca, data=request.data)
        if de_serializer.is_valid():
           de_serializer.save()
           return Response(de_serializer.data)
        else:
           return Response(de_serializer.errors)
           
        
    
    if request.method== 'DELETE': 
        finca=Fincas.objects.get(pk=id)
        finca.delete()
        data = {
            'resultado':True
        }
        return Response(data)
        