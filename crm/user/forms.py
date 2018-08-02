from django.contrib.auth import get_user_model, forms
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    # Создание нового пользователя

    class Meta:
        model = User
        fields = ('email', 'date_of_birth')

    def save(self, commit=True):
        password1 = User.objects.make_random_password() # Генерация случайного пароля
        user = super().save(commit=False)
        user.set_password(password1)
        subject = 'qwe'
        message = password1
        user.email_user(subject=subject, message=message)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]