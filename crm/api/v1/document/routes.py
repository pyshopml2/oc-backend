from rest_framework import routers
from .viewsets import *

document_router = routers.SimpleRouter()

document_router.register('catalog', CatalogDocumentsViewSet)
document_router.register('', DocumentViewSet)