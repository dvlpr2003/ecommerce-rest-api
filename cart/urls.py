from django.urls import *
from .views import *
urlpatterns = [
    path("",GetList.as_view()),
    path("<int:pk>",ModifyList.as_view())
]