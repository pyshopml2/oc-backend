from django.core.exceptions import ValidationError


class PasswordValidator:
    def check(self, password):
        try:
            self.validate_numeric(password)
            self.validate_length(password)
            result = password
        except ValidationError as err:
            result = err
        return result

    def validate_numeric(self, password):
        if password.isdigit():
            raise ValidationError(
                "This password is entirely numeric.")

    def validate_length(self, password):
        if len(password) < 8:
            raise ValidationError(
                "This password is too short.")
