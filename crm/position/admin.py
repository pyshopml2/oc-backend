from django.contrib import admin
from .models import Position

@admin.register(Position)
class EmployeePositionAdmin(admin.ModelAdmin):
    pass