from django.contrib.auth.models import BaseUserManager

from temp_token.models import TempToken
from auth.email_confirmation import CipherEmail

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


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
        user.set_password(password)
        user.save(using=self._db)

        token = TempToken.objects.create(user=user, active=True)

        ce = urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8')

        subject = 'subject'
        message = {
            'password': password,
            'token': token.token,
            'confirmation_email': ce
        }
        user.email_user(subject=subject, message=message)
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
