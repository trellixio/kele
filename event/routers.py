from rest_framework.routers import SimpleRouter
from django.urls import path, include

from event.auth.viewsets import ObtainTokenViewSet, LogoutViewSet, RegisterViewSet

auth_router = SimpleRouter()

auth_router.register(r'login', ObtainTokenViewSet, base_name='auth-login')
auth_router.register(r'logout', LogoutViewSet, base_name='auth-logout')
auth_router.register(r'register', RegisterViewSet, base_name='auth-register')

urlpatterns = [
    path(r'v1/', include((auth_router.urls, 'auth'), namespace='v1')),
]

