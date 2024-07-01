from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view




@api_view(["GET","POST"])
def get_hello(request):
    number = 2 + 3
    return HttpResponseRedirect(reverse("rev",args=[number]))
@api_view(['GET','POST'])
def get_rev (request,number):
    return Response(number)
    