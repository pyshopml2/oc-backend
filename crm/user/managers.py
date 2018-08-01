from django.contrib.auth.models import BaseUserManager

# Менеджер создания пользователей
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_superuser=False, is_staff=False):
        if not email:
            raise ValueError('Требуется ввести email')

        user = self.model(
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_staff=is_staff
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # Явное указание атрибутов модели is_superuser, is_staff
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
            is_staff=True
        )
        user.save(using=self._db)
        return user
