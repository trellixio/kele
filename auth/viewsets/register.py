from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from user.serializers import UserSerializer


class RegisterViewSet(viewsets.ViewSet):
    http_method_names = ['post']
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        return Response({'success': True}, status.HTTP_201_CREATED)
