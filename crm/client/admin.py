from django.contrib import admin

from . import models


@admin.register(models.ClientStatus)
class ClientStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClientGroup)
class ClientAdmin(admin.ModelAdmin):
    pass
