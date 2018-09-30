from . import models

from django.contrib import admin


@admin.register(models.Position)
class EmployeePositionAdmin(admin.ModelAdmin):
    pass
