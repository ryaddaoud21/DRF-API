from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PesronSerializer
import json
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)

    queryset = Person.objects.all()
    serializer_class = PesronSerializer


    def post(self, request, pk, format=None):
        return Response("ok")


from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
