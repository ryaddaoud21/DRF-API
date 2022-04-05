from django.urls import include, path

from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('test/', BMR , name="bmr"),
   path('test1/', get_clients , name="test"),
]