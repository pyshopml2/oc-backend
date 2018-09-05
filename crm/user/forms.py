from django.contrib.auth import get_user_model, forms
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from employee.models import Employee


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('email', )

    def save(self, commit=True):
        password1 = Employee.objects.make_random_password()
        user = super().save(commit=False)
        user.set_password(password1)
        subject = 'qwe'
        message = password1
        user.email_user(subject=subject, message=message)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = (
            'email', 'password', 'date_of_birth', 'is_active', 'is_superuser'
        )

    def clean_password(self):
        return self.initial["password"]
