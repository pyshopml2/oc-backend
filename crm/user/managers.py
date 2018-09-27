from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import BaseUserManager

from temp_token.models import TempToken, EmailToken


class UserManager(BaseUserManager):
    def create_user(
            self, email, password=None, is_superuser=False,
            first_name=None, middle_name=None, last_name=None,
            is_staff=False):
        if not email:
            raise ValueError('Требуется ввести email')

        user = self.model(
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_staff=is_staff,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        password = password or BaseUserManager().make_random_password()
        user.set_password(password)
        user.save(using=self._db)
        try:
            temp_token = EmailToken.objects.create(user=self)
            confirmation_token_email = \
                TempToken.objects.create(user=self, active=True)

            base64_user_id = urlsafe_base64_encode(
                force_bytes(user.pk)).decode('utf-8')

            subject = 'subject'
            message = {
                'password': password,
                'temp_token': temp_token.token,
                'email_confirmed_token': confirmation_token_email.token,
                'base64_user_id': base64_user_id
            }
            user.email_user(subject=subject, message=message)
        except Exception:
            pass

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
