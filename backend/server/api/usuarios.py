from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from server.models import Proceso


class UsuariosSerializer(serializers.ModelSerializer):
    procesos = serializers.PrimaryKeyRelatedField(many=True, queryset=Proceso.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'procesos')
        extra_kwargs = {'password': {'write_only': True}}


class Usuariosview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
