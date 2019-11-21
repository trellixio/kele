from rest_framework import status
from rest_framework.response import Response


class CurrentModelMixin:
    """
    Retrieve a model instance.
    """

    def current(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status.HTTP_200_OK)


class CurrentUpdateModelMixin:
    pass
