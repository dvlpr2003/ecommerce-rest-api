from django.urls import path

from .views import *
urlpatterns = [
    path("get/data",get_hello),
    path("get-reverse/<int:number>/",get_rev,name="rev")
]
