from django.contrib import admin

from .models import TempToken, EmailToken


@admin.register(TempToken)
class TempTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailToken)
class EmailTokenAdmin(admin.ModelAdmin):
    pass