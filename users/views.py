from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()