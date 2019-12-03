from rest_framework import serializers

from event.models import Event
from user.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):

    organizer = UserSerializer(many=False, read_only=True, source='user')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'location', 'photo', 'created', 'updated', 'organizer')
