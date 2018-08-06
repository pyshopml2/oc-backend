from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

# Менеджер создания пользователей
class UserManager(BaseUserManager):
    def create_user(self, email, is_superuser=False, is_staff=False):
        if not email:
            raise ValueError('Требуется ввести email')

        user = self.model(
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_staff=is_staff
        )
        password = BaseUserManager().make_random_password()
        user.set_password(password)
        subject = 'qwe' #
        message = password #
        user.email_user(subject=subject, message=message) #
        user.save(using=self._db)
        return user

    # Явное указание атрибутов модели is_superuser, is_staff
    def create_superuser(self, email):
        user = self.create_user(
            email,
            is_superuser=True,
            is_staff=True
        )
        user.save(using=self._db)
        return user
