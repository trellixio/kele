from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from auth.models import AuthToken


class LogoutViewSet(ViewSet):
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except AuthToken.DoesNotExist:
            pass
        return Response({'success': True}, status.HTTP_200_OK)
