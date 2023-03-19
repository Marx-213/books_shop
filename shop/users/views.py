from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from .models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''Вьюсет для показа юзера'''
    queryset = User.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
