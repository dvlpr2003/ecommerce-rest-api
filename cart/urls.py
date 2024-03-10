from django.urls import *
from .views import *
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("list",GetList)
# route.register("user",GetUser)
urlpatterns = route.urls

