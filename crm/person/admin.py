from django.contrib import admin
from .models import ContactPerson
from user.admin import UserAdmin

@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Адрес', {'fields': ['region', 'city', 'dialing_code', 'status']}),
        ('Компания', {'fields': ['client']}),
    ]
    fieldsets.insert(0, UserAdmin.fieldsets[0])
    fieldsets.insert(1, UserAdmin.fieldsets[1])
    fieldsets.insert(3, UserAdmin.fieldsets[2])
    fieldsets.insert(4, UserAdmin.fieldsets[3])