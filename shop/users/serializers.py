from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор для юзеров'''

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'last_name',
            'first_name',
            'is_subscribed',
        )
        read_only_fields = ('is_subscribed',)
        extra_kwargs = {'password': {'write_only': True}}
