from django_filters.rest_framework import FilterSet


from userinfo.models import *


class STDFilter(FilterSet):
    class Meta:
        model = User_info
        fields ={
            "name":["exact"],
        }