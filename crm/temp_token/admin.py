from django.contrib import admin

from . import models


@admin.register(models.TempToken)
class TempTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EmailToken)
class EmailTokenAdmin(admin.ModelAdmin):
    pass