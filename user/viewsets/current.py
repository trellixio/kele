from user.models import User
from user.serializers import UserSerializer
from xlib.rest_framework.viewsets import CurrentObjectViewSet


class CurrentUserViewSet(CurrentObjectViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'put']
