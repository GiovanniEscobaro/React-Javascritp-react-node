from rest_framework import serializers
from AppVendoTuFinca.models import Fincas


class FincaSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    direccion_finca=serializers.CharField()
    pais_finca=serializers.CharField()
    descripcion_finca=serializers.CharField()
    imagen_finca=serializers.CharField()
    active_finca=serializers.CharField()
    
    def create(self, validated_data):
        return Fincas.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.direccion_finca=validated_data.get('direccion_finca', instance.direccion_finca)
        instance.pais_finca=validated_data.get('pais_finca', instance.pais_finca)
        instance.descripcion_finca=validated_data.get('descripcion_finca', instance.descripcion_finca)
        instance.imagen_finca=validated_data.get('imagen_finca', instance.imagen_finca)
        instance.active_finca==validated_data.get('active_finca', instance.active_finca)
        instance.save()
        return instance
        
        #return super().update(instance, validated_data) 