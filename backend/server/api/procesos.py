from rest_framework import serializers, viewsets
from server.models import Proceso, Documento, Producto
from server.api.documentos import DocumentoSerializer
from server.api.productos import ProductoSerializer
from rest_framework import views


class ProcesoSerializer(serializers.ModelSerializer):
    documento_obj = DocumentoSerializer(source='documento')
    producto_obj = ProductoSerializer(source='producto')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Proceso
        fields = ['id', 'cantidad', 'documento_obj', 'producto_obj', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def create(self, validated_data):
        procesos_data = validated_data.pop('documento')
        proceso = Proceso.objects.create(**validated_data)
        for documentos_data in documentos_data:
            Documento.objects.create(proceso=proceso, **validated_data)
        return proceso


    def create(self, validated_data):
        procesos_data = validated_data.pop('producto')
        proceso = Proceso.objects.create(**validated_data)
        for productos_data in productos_data:
            Producto.objects.create(proceso=proceso, **validated_data)
        return proceso


class ProcesoView(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
