from django.urls import *
from .views import *
urlpatterns = [
    path("",index),
    path("<int:pk>",get_Student)
]