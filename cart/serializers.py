from rest_framework import serializers
from .models import Student
from userinfo.models import *

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = "__all__"
    # category = serializers.StringRelatedField()
    category = categorySerializer()
        
        
