from rest_framework import viewsets

from event.models import Event
from event.serializers import EventWithoutUserSerializer, EventSerializer


class CurrentEventViewSet(viewsets.ModelViewSet):
    serializer_class = EventWithoutUserSerializer
    http_method_names = ['get', 'put', 'delete', 'patch']

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).distinct()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.exclude(user=self.request.user)
