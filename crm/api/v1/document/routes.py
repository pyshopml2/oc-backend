from rest_framework import routers

from .viewsets import *

document_router = routers.SimpleRouter()

document_router.register(
    'catalog', CatalogDocumentsViewSet, base_name='catalog'
)
document_router.register('', DocumentViewSet, base_name='document')
