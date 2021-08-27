from django.db import models
from django.contrib.auth.models import User


class Proceso(models.Model):
    user = models.ForeignKey(User, related_name='procesos', on_delete=models.CASCADE, null=True)
    documento = models.ForeignKey('server.Documento', related_name='documentos', on_delete=models.CASCADE, null=False, blank=True)
    producto = models.ForeignKey('server.Producto', related_name='productos', on_delete=models.CASCADE, null=False, blank=True)
    cantidad = models.FloatField(null=False, blank=True)

    class Meta:
        ordering = ['id']

    def __int__(self):
        return int(self.id)


class Producto(models.Model):
    nombre = models.CharField(max_length=50,null=True, blank=True)
    codigo = models.CharField(max_length=50,null=True, blank=True)
    precio = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.nombre)


class Documento(models.Model):
    nombre = models.CharField(max_length=50,null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_envio = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.nombre)
