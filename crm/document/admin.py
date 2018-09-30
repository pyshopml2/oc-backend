from django.contrib import admin

from . import models


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CatalogDocuments)
class CatalogDocumentsAdmin(admin.ModelAdmin):
    pass
