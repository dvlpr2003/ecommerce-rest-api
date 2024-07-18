from django.urls import *
from .views import PdfUploadView


urlpatterns = [
    path("pdf/upload/",PdfUploadView.as_view()),

]