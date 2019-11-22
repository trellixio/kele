from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth.authentication import JWTAuthentication
from auth.models import AuthToken
from auth.serializers import AuthTokenSerializer


class ObtainTokenViewSet(viewsets.ViewSet):
    http_method_names = ['post']
    serializer_class = AuthTokenSerializer
    permission_classes = (AllowAny,)
    queryset = AuthToken.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = JWTAuthentication().get_auth_token(user)
        return Response({'token': token}, status.HTTP_200_OK)
