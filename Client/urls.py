from django.urls import include, path

from rest_framework import routers

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('test1/', get_clients , name="test"),
   path('api-auth/', include('rest_framework.urls')),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('register/', RegisterView.as_view(), name='auth_register'),
   path('detail/', PersonAuthToken.as_view(), name='detail'),

]
router = DefaultRouter()
router.register(r"user",UserViewSet, basename="user")
urlpatterns += router.urls