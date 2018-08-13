from rest_framework import serializers
from person.models import *

class ContactPersonSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'