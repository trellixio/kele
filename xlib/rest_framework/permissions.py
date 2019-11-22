from rest_framework.permissions import BasePermission

from user.models import User


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if not isinstance(obj, User):
            return obj.user == request.user

        return obj == request.user


class UpdateOrRetrieveOnlyForAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if view.action in ['retrieve', 'update', 'partial_update', 'delete']:
            return False

        return True
