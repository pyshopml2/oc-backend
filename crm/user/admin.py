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
        ('Общая информация', {'fields': ('user_position', 'password', 'timezone', 'status')}),
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

admin.site.unregister(Group)