from django.urls import include, path

from rest_framework import routers

from .views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)

urlpatterns = [
   path('', include(router.urls)),
]