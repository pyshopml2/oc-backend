from rest_framework import routers

from . import viewsets

document_router = routers.SimpleRouter()

document_router.register(
    'catalog', viewsets.CatalogDocumentsViewSet, base_name='catalog'
)
document_router.register('', viewsets.DocumentViewSet, base_name='document')
