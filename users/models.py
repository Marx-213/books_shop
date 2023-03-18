from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Кастомная модель юзера.'''
    first_name = models.CharField(
        'Имя',
        help_text='Укажите свое имя',
        max_length=150,
    ),
    last_name = models.CharField(
        'Фамилия',
        help_text='Укажите вашу фамилию',
        max_length=150,
    ),
    username = models.CharField(
        'Юзернейм',
        help_text='Укажите юзернейм',
        unique=True,
        max_length=150,
    )
    email = models.EmailField(
        'Адрес электронноый почты',
        help_text='Укажите адрес электронной почты',
        unique=True,
        max_length=150,
    )
    password = models.CharField(
        'Пароль',
        help_text='Укажите ваш пароль',
        max_length=150,
    )
    is_subscribed = models.ManyToManyField(
        'Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False,
    )
    REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
    
    def __str__(self):
        return self.username
