from django.shortcuts import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import *
from rest_framework import status


@api_view(["GET","POST"])
def index(request):
    if request.method == "GET":
        model = Student.objects.all()
        Serial=StudentSerializer(model,many = True)
        return Response(Serial.data)
    elif request.method == "POST":
        Serial = StudentSerializer(data=request.data)
        if Serial.is_valid():
            Serial.save()
            return Response(Serial.data,status=status.HTTP_201_CREATED)
        return Response(Serial.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
@api_view(["GET","DELETE","PUT"])
def get_Student(request,pk):
    model =get_object_or_404(Student,id=pk)
    print(model)
    if request.method == "GET":
        Serial = StudentSerializer(model)
        return Response(Serial.data)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        Serial = StudentSerializer(model,data =request.data)
        if Serial.is_valid():
            Serial.save()
            return Response(Serial.data)
        else:
            return Response(Serial.errors)
        
        

    


        

