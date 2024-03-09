from django.shortcuts import *
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from .models import *

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class GetList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =["department","age"]






        

    


        

