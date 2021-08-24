from rest_framework import serializers, viewsets
from server.models import Documento
from rest_framework import views
from server.api.clientes import ClienteSerializer


class DocumentoSerializer(serializers.ModelSerializer):
    cliente_obj = ClienteSerializer(source='cliente', read_only=True)

    class Meta:
        model = Documento
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_envio', 'cliente_obj']

    def create(self, validated_data):
        return Documento.objects.create(**validated_data)


class DocumentoView(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
