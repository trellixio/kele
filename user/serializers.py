from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(source='date_joined', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'is_active', 'created', 'updated', 'password'

        ]
        extra_kwargs = {
            'email': {'required': True, },
            'last_name': {'required': True, },
            'first_name': {'required': True, },
            'id': {'read_only': True, },
            'password': {'write_only': True, },
        }

    def create(self, validated_data):
        validated_data['is_staff'] = False
        user = User.objects.create_user(**validated_data)
        # user.set_password(validated_data['password'])
        return user
