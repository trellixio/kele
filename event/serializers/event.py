from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'location', 'photo', 'created', 'updated')


class EventWithoutUserSerializer(EventSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('organizer')
        return ret
