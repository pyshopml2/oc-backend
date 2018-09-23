import base64
from Crypto.Cipher import AES

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class CipherEmail:

    def secret_key(self):
        key = 'IycMDCPst970'
        secret_key = "{: <32}".format(key).encode("utf-8")
        return secret_key

    def cipher_email(self, user=None, cipher_email=None):
        secret_key = self.secret_key()
        cipher = AES.new(secret_key, AES.MODE_ECB)
        if user is not None:
            msg_text = user.email.rjust(32)
            encoded = base64.b64encode(cipher.encrypt(msg_text))
            return encoded
        else:
            decoded = cipher.decrypt(base64.b64decode(cipher_email))
            return decoded.decode('utf-8').strip()


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp))


account_activation_token = TokenGenerator()