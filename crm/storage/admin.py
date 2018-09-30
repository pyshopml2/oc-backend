from . import models
from django.contrib import admin


@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    pass
