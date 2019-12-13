from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer
from event.models import Event


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        event_pk = self.kwargs['event_pk']
        event = get_object_or_404(Event.objects.filter(id=event_pk), **{'id': event_pk})
        return Comment.objects.filter(event=event)
