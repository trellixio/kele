from rest_framework import serializers

from comment.models import Comment
from user.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(many=False, source='user', read_only=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['event_id'] = self.context['view'].kwargs['event_pk']
        return super().create(validated_data)

    class Meta:
        model = Comment
        fields = ('id', 'message', 'created', 'updated', 'author', 'event')

        extra_kwargs = {
            'event': {'required': False, 'write_only': True}
        }
