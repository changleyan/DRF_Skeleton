from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from apps.core.api.v1.example_component.UserSerializar import UserSerializer
from apps.core.api.v1.example_component.UserPermissions import UserPermissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (UserPermissions,)
