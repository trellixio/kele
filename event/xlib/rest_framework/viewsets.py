from rest_framework import viewsets, mixins

from .mixins import CurrentModelMixin


class CurrentObjectViewSet(CurrentModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get', 'put']

    def get_object(self):
        obj = self.request.user

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
