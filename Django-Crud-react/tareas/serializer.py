from rest_framework import serializers
from .models import tarea
# Lo campos que quiero dejas de la base de datos de un tabla
class tareaSerializer(serializers.ModelSerializer):
    class Meta:
        model=tarea
        # En este caso salesionamos lo campos por su nombre en una dupla
        #fields=('id','titula','descripcion','Activo')
        # Pero si lo qeremos todo se hace asi:
        fields='__all__' 
