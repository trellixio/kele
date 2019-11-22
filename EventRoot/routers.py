from django.urls import path, include

from auth.viewsets import ObtainTokenViewSet, LogoutViewSet, RegisterViewSet
from event.viewsets import EventViewSet
from user.viewsets import UserViewSet
from xlib.rest_framework.router import EventRouter

router = EventRouter()

# Auth
router.register(r'logout',  LogoutViewSet,          base_name='auth')
router.register(r'account', RegisterViewSet,        base_name='auth')
router.register(r'auth',    ObtainTokenViewSet,     base_name='auth')

# user
router.register(r'user',   UserViewSet,            base_name='user')

# event
router.register(r'event',       EventViewSet,               base_name='event')


urlpatterns = [
    path(r'v1/', include(router.urls)),
]
