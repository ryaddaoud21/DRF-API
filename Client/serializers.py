from rest_framework import serializers
from .models import Person


class PesronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('Name', 'Username','Age','Sport', 'Email','Gender', 'Train','Weight','Height', 'Hours','Effort','Goal_Type' , 'Goal_Weight' , 'Password','Image')
