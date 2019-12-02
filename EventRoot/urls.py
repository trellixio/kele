from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from auth.viewsets import ObtainTokenViewSet, LogoutViewSet, RegisterViewSet
from event.viewsets import EventViewSet
from user.viewsets import UserViewSet
from comment.viewsets import CommentViewSet

router = SimpleRouter()

# Auth
router.register(r'logout',  LogoutViewSet,          base_name='auth')
router.register(r'account', RegisterViewSet,        base_name='auth')
router.register(r'auth',    ObtainTokenViewSet,     base_name='auth')

# user
router.register(r'user',   UserViewSet,            base_name='user')

# event
router.register(r'event',       EventViewSet,               base_name='event')

event_router = NestedSimpleRouter(router, r'event', lookup='event')
event_router.register(r'comment', CommentViewSet,   base_name='event-comment')


urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/', include(event_router.urls)),
]

