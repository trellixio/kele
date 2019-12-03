from rest_framework.permissions import BasePermission, SAFE_METHODS

from user.models import User


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            if isinstance(obj, User):
                return obj == request.user
            return True

        if request.user.is_superuser:
            return True

        if not isinstance(obj, User):
            return obj.user == request.user

        return obj == request.user


class ListCreateDeleteOnlyForAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if view.action in ['list', 'destroy', 'create']:
            return False

        return True
