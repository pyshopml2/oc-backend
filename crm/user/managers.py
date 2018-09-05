from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(
            self, email, password=None,
            is_superuser=False, is_staff=False):
        if not email:
            raise ValueError('Требуется ввести email')

        user = self.model(
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_staff=is_staff
        )
        if password:
            password = password
        else:
            password = BaseUserManager().make_random_password()
            subject = 'qwe'
            message = password
            user.email_user(subject=subject, message=message)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, email):
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
            is_staff=True
        )
        user.save(using=self._db)
        return user
