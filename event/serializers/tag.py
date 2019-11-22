from rest_framework import serializers

from event.models import EventTag


class EventTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTag
        fields = '__al__'
