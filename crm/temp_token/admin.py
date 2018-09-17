from django.contrib import admin
from .models import TempToken


@admin.register(TempToken)
class TempTokenAdmin(admin.ModelAdmin):
    pass
