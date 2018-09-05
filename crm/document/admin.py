from django.contrib import admin
from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(CatalogDocuments)
class CatalogDocumentsAdmin(admin.ModelAdmin):
    pass
