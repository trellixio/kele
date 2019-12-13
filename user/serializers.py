from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(source='date_joined', read_only=True)

    def create(self, validated_data):
        """
        Without override this method the password is not encrypted
        :param validated_data: dict
        :return: user: User
        """
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        user = super(UserSerializer, self).to_representation(instance)
        if not self.context['request'].user.is_superuser and not self.context['request'].user == instance:
            user.pop('email')
            user.pop('is_active')
            user.pop('username')
        return user

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email',
            'is_active', 'photo', 'created', 'updated', 'password',)

        extra_kwargs = {
            'email': {'required': True, },
            'last_name': {'required': True, },
            'first_name': {'required': True, },
            'id': {'read_only': True, },
            'password': {'write_only': True, },
        }