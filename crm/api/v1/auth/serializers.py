from rest_framework import serializers
from auth.validators import PasswordValidator


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirmed_password = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get('password')
        confirmed_password = attrs.get('confirmed_password')

        if password == confirmed_password:
            result = PasswordValidator().check(password=password)
            return result
        else:
            return 'Passwords do not match'
