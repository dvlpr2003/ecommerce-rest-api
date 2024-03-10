from django.shortcuts import *
from rest_framework.response import Response
from .serializers import *
from .models import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import STDFilter

from rest_framework.pagination import PageNumberPagination

# Userinfo model 
from userinfo.models import *


class GetList(ModelViewSet):
    queryset = User_info.objects.all()
    serializer_class =userSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = STDFilter
    search_fields = ["name"]
    ordering_fields = [
        "name"
    ]
    pagination_class = PageNumberPagination




# class GetUser(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers

        

    


        

