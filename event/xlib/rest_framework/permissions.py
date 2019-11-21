from rest_framework.permissions import BasePermission

from event.user.models import User


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if not isinstance(obj, User):
            return obj.user == request.user

        return obj == request.user
