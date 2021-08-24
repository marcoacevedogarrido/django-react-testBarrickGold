from rest_framework import serializers, viewsets, permissions
from server.models import Proceso
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework import status
from django.db.models import Sum, Count


class SorteoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    total_bruto = serializers.SerializerMethodField()

    class Meta:
        model = Proceso
        fields = ('total', 'cantidad', 'total_bruto')

    def get_total(self, obj):
        precio = Proceso.objects.values('proceso').aggregate(monto_total=Sum('producto__precio'))['monto_total']
        return precion

    def get_total_bruto(self, obj):
        cantidad = int(obj.cantidad)
        precio = int(obj.producto.precio)
        return cantidad * precio


class SorteoView(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = SorteoSerializer
