from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from user.models import User
from user.serializers import UserSerializer
from xlib.permissions import ListCreateDeleteOnlyForAdmin, IsOwnerOrAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [ListCreateDeleteOnlyForAdmin, IsOwnerOrAdminOrReadOnly]

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

    def get_object(self):
        if self.kwargs[self.lookup_field] == 'current':
            obj = self.request.user
        else:
            obj = get_object_or_404(self.get_queryset(), **{self.lookup_field: self.kwargs[self.lookup_field]})

        self.check_object_permissions(self.request, obj)

        return obj
