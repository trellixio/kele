from rest_framework import viewsets

from .mixins import CurrentRetrieveModelMixin, CurrentUpdateModelMixin


class CurrentObjectViewSet(CurrentRetrieveModelMixin, CurrentUpdateModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get', 'put']

    def get_object(self):
        obj = self.request.user

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
