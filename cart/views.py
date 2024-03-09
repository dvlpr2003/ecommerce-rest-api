from django.shortcuts import *
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from .models import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import STDFilter


class GetList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = STDFilter
    search_fields = ["name","address","college"]
    ordering_fields = [
        "name"
    ]






        

    


        

