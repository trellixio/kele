from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter

from auth.viewsets import ObtainTokenViewSet, LogoutViewSet, RegisterViewSet
from user.viewsets import CurrentUserViewSet, UserViewSet
from event.viewsets import EventViewSet, CurrentEventViewSet
from xlib.rest_framework.router import EventRouter
from comment.viewsets import CommentViewSet

router = EventRouter()

# Auth
router.register(r'logout',  LogoutViewSet,          base_name='auth')
router.register(r'account', RegisterViewSet,        base_name='auth')
router.register(r'auth',    ObtainTokenViewSet,     base_name='auth')

# user
router.register(r'users',   UserViewSet,            base_name='user')
router.register(r'me',      CurrentUserViewSet,     base_name='current-user')

# event
router.register(r'events',       EventViewSet,               base_name='event')
router.register(r'me/events',    CurrentEventViewSet,        base_name='me-event')

event_router = NestedSimpleRouter(router, r'users',     lookup='user')
event_router.register(r'events', EventViewSet, base_name='users-events')

# review
current_review_router = NestedSimpleRouter(router, r'me/events', lookup='event')
current_review_router.register(r'comments', CommentViewSet, base_name='event-comment')

user_review_router = NestedSimpleRouter(router, r'events', lookup='event')
user_review_router.register(r'comments', CommentViewSet, base_name='event-comment')


urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/', include(event_router.urls)),
    path(r'v1/', include(current_review_router.urls)),
    path(r'v1/', include(user_review_router.urls)),
]
