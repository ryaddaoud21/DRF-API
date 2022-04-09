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

def BMR (request):
    persons = Person.objects.all()
    context = {"persons" :persons}
    return render(request,'Client/Test.html', context)


import json
import requests
from PIL import Image
import pytesseract


import os
def get_clients(request):

    clients = requests.get("http://127.0.0.1:8000/people/").json()
    for client in clients :
        if client['Gender'] == "M":
            BMR = (10 * client['Weight']) + (6.25 * client['Height']) + (-5 * client['Age']) + 5
        else:
            BMR = (10 * client['Weight']) + (6.25 * client['Height']) + (-5 * client['Age']) - 161
        client['Calculate_BMR']= float(BMR)

        if client['Train'] == 0:
            TDEE = client['Calculate_BMR'] * 1.2
        elif client['Train'] == 1:
            TDEE = client['Calculate_BMR'] * 1.3
        elif client['Train'] == 2:
            TDEE = client['Calculate_BMR'] * 1.4
        elif client['Train'] == 3:
            TDEE = client['Calculate_BMR'] * 1.45
        elif client['Train']== 4:
            TDEE = client['Calculate_BMR'] * 1.5
        elif client['Train'] == 5:
            TDEE = client['Calculate_BMR'] * 1.7
        elif client['Train'] == 6:
            TDEE = client['Calculate_BMR'] * 1.8
        elif client['Train'] == 7:
            TDEE = client['Calculate_BMR'] * 2
        else:
            TDEE = client['Calculate_BMR'] * 2.2

        client['Calculate_TDEE'] = float(TDEE)

        print(client['Calculate_BMR'],client['Calculate_TDEE'])




        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\PycharmProjects\DRF_PROJECT\Tesseract-OCR\tesseract'
        a =client['Image']

        import os

        IMAGE_FILE = 'media/images/cr7.png'

        if os.path.isfile(IMAGE_FILE):
            print('Existe..')
        else:
            print('Existe pas!')

        a =IMAGE_FILE
        
        image_string = pytesseract.image_to_string(Image.open(a))
        client['Image'] = image_string


        print(image_string)
        print(client)


    context = {'clients': clients }
    return render(request, 'Client\Test1.html', context)


from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer