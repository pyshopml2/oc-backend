from django.contrib.auth.password_validation \
    import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(help_text='New user password')
    confirmed_password = serializers.CharField(help_text='Confirmed password')

    def validate(self, attrs):
        password = attrs.get('password')
        confirmed_password = attrs.get('confirmed_password')

        if password == confirmed_password:
            try:
                print('1', validate_password(password=password))
                return password
            except ValidationError as err:
                raise serializers.ValidationError(
                    {'detail': 'This is bad password'}
                )
        else:
            raise serializers.ValidationError(
                'Passwords do not match'
            )