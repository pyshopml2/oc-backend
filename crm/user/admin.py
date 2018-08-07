from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

from .models import *

User = get_user_model()

class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    # Показ атрибутов модели
    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('Персональные данные', {'fields': ('first_name', 'middle_name', 'last_name')}),
        ('Контакты', {'fields': ('email', 'phone_number')}),
        ('Общая информация', {'fields': ('role', 'password', 'timezone', )}),
        ('Дополнительная информация', {'fields': ('date_of_birth', 'other_contacts', 'extra_phone_number')}),
        ('Права и должности', {
            'fields': ('is_superuser', 'is_active', 'is_staff')
        }),
    )

    # Показывает поля для создания нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Регистрируем наши новые модели
admin.site.register(User, UserAdmin)

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ['login_skype']}),
        (None, {'fields': ['confirmed_email', 'group', 'status']}),
    ]
    fieldsets.insert(0, UserAdmin.fieldsets[0])
    fieldsets.insert(1, UserAdmin.fieldsets[1])
    fieldsets.insert(3, UserAdmin.fieldsets[2])
    fieldsets.insert(4, UserAdmin.fieldsets[3])
    fieldsets.insert(5, UserAdmin.fieldsets[4])

@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Адрес', {'fields': ['region', 'city', 'dialing_code', 'status']}),
    ]
    fieldsets.insert(0, UserAdmin.fieldsets[0])
    fieldsets.insert(1, UserAdmin.fieldsets[1])
    fieldsets.insert(3, UserAdmin.fieldsets[2])
    fieldsets.insert(4, UserAdmin.fieldsets[3])

@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupEmployee)
class GroupEmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Group)