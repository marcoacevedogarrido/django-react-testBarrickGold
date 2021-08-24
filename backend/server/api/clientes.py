
from rest_framework import serializers, viewsets
from server.models import Cliente
from rest_framework import views


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)

class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
