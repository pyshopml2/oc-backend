from django.contrib import admin
from .models import *

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass