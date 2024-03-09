from django_filters.rest_framework import FilterSet


from .models import Student


class STDFilter(FilterSet):
    class Meta:
        model = Student
        fields ={
            "department":["exact"],
            "age":["gt","lt"]
        }