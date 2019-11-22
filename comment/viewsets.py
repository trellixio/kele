from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(event_id=self.kwargs['event_pk'])
