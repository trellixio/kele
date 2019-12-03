from rest_framework import viewsets

from event.models import Event
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
