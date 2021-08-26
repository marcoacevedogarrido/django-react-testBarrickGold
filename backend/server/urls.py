from django.urls import path
from rest_framework import routers
from server.api.procesos import ProcesoView
from server.api.productos import ProductoView
from server.api.documentos import DocumentoView
from server.api.usuarios import Usuariosview
from server.api.sorteos import SorteoView

router = routers.SimpleRouter()

router.register(r'api/procesos', ProcesoView, 'procesos')
router.register(r'api/productos', ProductoView, 'productos')
router.register(r'api/documentos', DocumentoView, 'documentos'),
router.register(r'api/sorteos', SorteoView, 'sorteos'),
router.register(r'api/usuarios', Usuariosview, 'usuarios')

urlpatterns = router.urls
