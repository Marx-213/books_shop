from rest_framework import serializers
from rest_framework.serializers import ValidationError


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


class PasswordSerializer(serializers.ModelSerializer):
    ''''''
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, current_password):
        '''Проверка введённого пароля на допустимую длину.'''
        if len(current_password) > 150:
            raise ValidationError('Недопустимая длина пароля!')
        return current_password

    def validate_new_password(self, new_password):
        '''Проверка нового пароля на допустимую длину.'''
        if len(new_password) > 150:
            raise ValidationError('Недопустимая длина нового пароля!')
        return new_password

