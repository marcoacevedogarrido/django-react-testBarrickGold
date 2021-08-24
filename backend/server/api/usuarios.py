from rest_framework import serializers, viewsets
from django.contrib.auth.models import User


class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'cliente')
        extra_kwargs = {'password': {'write_only': True}}


class Usuariosview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
