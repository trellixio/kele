from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)
