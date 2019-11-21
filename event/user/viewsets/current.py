from event.user.models import User
from event.user.serializer import UserSerializer
from event.xlib.rest_framework.viewsets import CurrentObjectViewSet


class CurrentUserViewSet(CurrentObjectViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
