from rest_framework import serializers
from .models import Person


class PesronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'Age', 'Email','Gender', 'Weight','Height', 'Phone', 'Password','Image')
