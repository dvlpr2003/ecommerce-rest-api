from django.shortcuts import *
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView


class GetList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






class ModifyList(APIView):
    def put(self,request,pk):
        model =get_object_or_404(Student,id=pk)
        Serial = StudentSerializer(model,data =request.data)
        Serial.is_valid(raise_exception=True)
        Serial.save()
        return Response(Serial.data)
    def delete(self,request,pk):
        model =get_object_or_404(Student,id=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get(self,request,pk):
        model =get_object_or_404(Student,id=pk)
        Serial = StudentSerializer(model)
        return Response(Serial.data)



        

    


        

