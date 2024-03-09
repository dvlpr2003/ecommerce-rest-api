from django.shortcuts import *
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from .models import *

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class GetList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






        

    


        

