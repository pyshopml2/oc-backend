from django.contrib import admin
from .models import Employee, GroupEmployee
from user.admin import UserAdmin

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ['login_skype']}),
        (None, {'fields': ['confirmed_email', 'employee_group']}),
    ]
    fieldsets.insert(0, UserAdmin.fieldsets[0])
    fieldsets.insert(1, UserAdmin.fieldsets[1])
    fieldsets.insert(3, UserAdmin.fieldsets[2])
    fieldsets.insert(4, UserAdmin.fieldsets[3])
    fieldsets.insert(5, UserAdmin.fieldsets[4])

@admin.register(GroupEmployee)
class GroupEmployeeAdmin(admin.ModelAdmin):
    pass