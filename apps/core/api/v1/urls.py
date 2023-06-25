from django.urls import path, include
from rest_framework import routers

from apps.core.api.v1.example_component import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls), ),
]
