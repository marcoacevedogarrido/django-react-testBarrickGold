from rest_framework import serializers, viewsets
from server.models import Documento
from rest_framework import views


class DocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documento
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_envio']


class DocumentoView(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
