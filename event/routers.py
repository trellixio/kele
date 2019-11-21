from rest_framework.routers import SimpleRouter
from django.urls import path, include

from event.auth.viewsets import ObtainTokenViewSet, LogoutViewSet, RegisterViewSet
from event.user.viewsets import CurrentUserViewSet


# Auth
from event.xlib.rest_framework.router import EventRouter

auth_router = SimpleRouter()

auth_router.register(r'login', ObtainTokenViewSet, base_name='auth-login')
auth_router.register(r'logout', LogoutViewSet, base_name='auth-logout')
auth_router.register(r'register', RegisterViewSet, base_name='auth-register')

# user

user_router = EventRouter()

user_router.register(r'me', CurrentUserViewSet, base_name='user-current')

urlpatterns = [
    path(r'v1/', include((auth_router.urls, 'auth'), namespace='auth')),
    path(r'v1/', include((user_router.urls, 'user'), namespace='user')),
]
