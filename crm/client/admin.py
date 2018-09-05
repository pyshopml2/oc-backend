from django.contrib import admin
from .models import *


@admin.register(ClientStatus)
class ClientStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientGroup)
class ClientAdmin(admin.ModelAdmin):
    pass
