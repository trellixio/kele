from rest_framework import viewsets

from event.models import EventTag
from event.serializers import EventTagSerializer


class EventTagViewSet(viewsets.ModelViewSet):
    queryset = EventTag.objects.all()
    serializer_class = EventTagSerializer
